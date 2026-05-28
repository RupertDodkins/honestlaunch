from __future__ import annotations

import asyncio
from dataclasses import dataclass
from time import perf_counter

from pydantic import BaseModel, Field

from .contrast import apply_contrast
from .gemini import GeminiClient
from .numeric import calibrate_numeric_claim
from .schemas import AgentAudit, ClaimAudit, ClaimTimingProfile, Document, EvidenceItem, RiskyClaim, Verdict
from .skills import load_skill


class AgentAuditSet(BaseModel):
    audits: list[AgentAudit] = Field(default_factory=list)


class ClaimAuditSet(BaseModel):
    audits: list[ClaimAudit] = Field(default_factory=list)


@dataclass
class AuditExecutionProfile:
    total_duration_ms: int
    contrast_duration_ms: int
    agent_passes: int
    contrast_claims: int
    claim_profiles: list[ClaimTimingProfile]


async def audit_claims(
    document: Document,
    claims: list[RiskyClaim],
    *,
    mock: bool,
    limit: int = 5,
    runtime: str = "local",
    contrast: bool = False,
    reference_urls: list[str] | None = None,
    contrast_top: int = 2,
) -> tuple[list[ClaimAudit], AuditExecutionProfile]:
    started_at = perf_counter()
    if runtime not in {"local", "managed"}:
        raise ValueError("runtime must be local or managed")
    selected = claims[:limit]
    if mock:
        audits = [_mock_audit(document, claim) for claim in selected]
        for audit in audits:
            audit.agent_outputs = _mock_agent_outputs(audit)
            audit.contrast = None
        if contrast:
            audits, contrast_profile = await apply_contrast(
                document,
                audits,
                mock=True,
                reference_urls=reference_urls or [],
                contrast_top=contrast_top,
            )
        else:
            contrast_profile = None
        claim_profiles = []
        for audit in audits:
            profile = audit.claim_timing or ClaimTimingProfile(claim_id=audit.claim.id)
            contrast_ms = contrast_profile.by_claim_id.get(audit.claim.id, 0) if contrast_profile else 0
            profile.contrast_ms = contrast_ms
            profile.total_duration_ms += contrast_ms
            audit.claim_timing = profile
            claim_profiles.append(profile)
        return audits, AuditExecutionProfile(
            total_duration_ms=_elapsed_ms(started_at),
            contrast_duration_ms=contrast_profile.total_duration_ms if contrast_profile else 0,
            agent_passes=len(audits) * 3,
            contrast_claims=len(contrast_profile.by_claim_id) if contrast_profile else 0,
            claim_profiles=claim_profiles,
        )

    per_claim = await asyncio.gather(*[_audit_one(document, claim, runtime=runtime) for claim in selected])
    audits = list(per_claim)
    if contrast:
        audits, contrast_profile = await apply_contrast(
            document,
            audits,
            mock=False,
            reference_urls=reference_urls or [],
            contrast_top=contrast_top,
        )
        for audit in audits:
            if not audit.claim_timing:
                continue
            contrast_ms = contrast_profile.by_claim_id.get(audit.claim.id, 0)
            audit.claim_timing.contrast_ms = contrast_ms
            audit.claim_timing.total_duration_ms += contrast_ms
    else:
        contrast_profile = None
        for audit in audits:
            audit.contrast = None
    claim_profiles = [audit.claim_timing for audit in audits if audit.claim_timing is not None]
    return audits, AuditExecutionProfile(
        total_duration_ms=_elapsed_ms(started_at),
        contrast_duration_ms=contrast_profile.total_duration_ms if contrast_profile else 0,
        agent_passes=len(audits) * 3,
        contrast_claims=len(contrast_profile.by_claim_id) if contrast_profile else 0,
        claim_profiles=claim_profiles,
    )


async def _audit_one(document: Document, claim: RiskyClaim, *, runtime: str) -> ClaimAudit:
    started_at = perf_counter()
    print(f"Auditing {claim.id}: {claim.claim[:90]}")
    agent_results = await asyncio.gather(
        _run_skill("verifier", document, claim, runtime=runtime),
        _run_skill("contradiction-finder", document, claim, runtime=runtime),
        _run_skill("numeric-calibrator", document, claim, runtime=runtime),
    )
    print(f"Aggregating {claim.id}")
    aggregate_started_at = perf_counter()
    aggregated = await _aggregate(document, claim, list(agent_results), runtime=runtime)
    aggregate_duration_ms = _elapsed_ms(aggregate_started_at)
    aggregated = _merge_numeric_calibration(document, aggregated)
    aggregated.agent_outputs = list(agent_results) + [
        AgentAudit(
            agent="claim-aggregator",
            claim_id=claim.id,
            summary=(
                f"Combined specialist outputs into final verdict `{aggregated.verdict.value}` "
                f"with `{aggregated.confidence}` confidence."
            ),
            duration_ms=aggregate_duration_ms,
            supporting_evidence=aggregated.supporting_evidence,
            counter_evidence=aggregated.counter_evidence,
            missing_context=aggregated.missing_context,
            numeric_findings=aggregated.numeric_findings,
        )
    ]
    aggregated.claim_timing = ClaimTimingProfile(
        claim_id=claim.id,
        total_duration_ms=_elapsed_ms(started_at),
        verifier_ms=agent_results[0].duration_ms or 0,
        contradiction_finder_ms=agent_results[1].duration_ms or 0,
        numeric_calibrator_ms=agent_results[2].duration_ms or 0,
        aggregator_ms=aggregate_duration_ms,
    )
    return aggregated


async def _run_skill(skill_name: str, document: Document, claim: RiskyClaim, *, runtime: str) -> AgentAudit:
    print(f"  Running {skill_name} for {claim.id}")
    started_at = perf_counter()
    skill = load_skill(skill_name)
    client = GeminiClient()
    prompt = f"""
Document title: {document.title}
Document source: {document.source}

Claim ID: {claim.id}
Claim: {claim.claim}
Claim type: {claim.claim_type}
Audit question: {claim.audit_question}

Relevant document text:
{document.text[:50000]}
"""
    if runtime == "managed":
        result = await asyncio.to_thread(
            client.structured_interaction,
            input_text=prompt,
            system_instruction=f"{skill}\n\nReturn only JSON matching the AgentAudit schema.",
            schema=AgentAudit,
            tools=skill_name != "numeric-calibrator",
        )
    else:
        result = await asyncio.to_thread(
            client.structured,
            f"{skill}\n\nReturn only JSON matching the AgentAudit schema.\n\n{prompt}",
            AgentAudit,
        )
    result.duration_ms = _elapsed_ms(started_at)
    return result


async def _aggregate(
    document: Document,
    claim: RiskyClaim,
    audits: list[AgentAudit],
    *,
    runtime: str,
) -> ClaimAudit:
    skill = load_skill("claim-aggregator")
    client = GeminiClient()
    audit_json = "\n".join(audit.model_dump_json(indent=2) for audit in audits)
    prompt = f"""
{skill}

Return only JSON matching the ClaimAudit schema.

Document title: {document.title}
Document source: {document.source}

Claim:
{claim.model_dump_json(indent=2)}

Specialist agent results:
{audit_json}
"""
    if runtime == "managed":
        return await asyncio.to_thread(
            client.structured_interaction,
            input_text=prompt,
            system_instruction=f"{skill}\n\nReturn only JSON matching the ClaimAudit schema.",
            schema=ClaimAudit,
            tools=False,
        )
    return await asyncio.to_thread(client.structured, prompt, ClaimAudit)


def _mock_audit(document: Document, claim: RiskyClaim) -> ClaimAudit:
    if claim.id.startswith("careful_"):
        return _mock_careful_audit(claim)
    if claim.id.startswith("receipts_"):
        return _mock_needs_receipts_audit(claim)
    if claim.id == "c1":
        supporting = [
            EvidenceItem(
                source_title="Demo document benchmark table",
                url=None,
                snippet="Baseline: 84.1%. HonestLaunch: 87.3%.",
                relevance="The table supports a 3.2-point absolute gain, not a 30% relative improvement.",
            )
        ]
        baseline, method = 84.1, 87.3
        absolute = method - baseline
        relative = (absolute / baseline) * 100
        return ClaimAudit(
            claim=claim,
            verdict=Verdict.OVERSTATED,
            confidence="high",
            stretch_score=88,
            why=(
                "The reported benchmark numbers show improvement, but the stated 30% improvement "
                "does not match the arithmetic and the evidence is a curated benchmark, not real-world tasks."
            ),
            weaker_supported_rewrite=(
                f"Our method improves performance from {baseline:.1f}% to {method:.1f}% on Benchmark X, "
                f"a {absolute:.1f}-point absolute gain and {relative:.1f}% relative improvement."
            ),
            supporting_evidence=supporting,
            counter_evidence=[],
            missing_context=["No real-world deployment task is reported in the demo document."],
            numeric_findings=[
                f"Absolute gain: {method:.1f} - {baseline:.1f} = {absolute:.1f} points.",
                f"Relative gain: ({absolute:.1f} / {baseline:.1f}) * 100 = {relative:.1f}%.",
            ],
        )

    needs_context = claim.claim_type.value in {"generalization", "novelty"}
    verdict = Verdict.MISSING_CONTEXT if needs_context else Verdict.NOT_CHECKABLE
    return ClaimAudit(
        claim=claim,
        verdict=verdict,
        confidence="medium",
        stretch_score=64 if needs_context else 55,
        why="The claim may be plausible, but the demo document does not provide enough scope or external evidence.",
        weaker_supported_rewrite="The document provides preliminary evidence for a narrower version of this claim.",
        supporting_evidence=[],
        counter_evidence=[],
        missing_context=["Additional external grounding would be needed for a production verdict."],
        numeric_findings=[],
    )


def _mock_careful_audit(claim: RiskyClaim) -> ClaimAudit:
    supporting = [
        EvidenceItem(
            source_title="Careful document benchmark table",
            url=None,
            snippet="Baseline: 84.1%. HonestLaunch: 87.3%. The document calls this a 3.2 percentage-point gain.",
            relevance="The source wording matches the table and keeps the scope limited to Benchmark X.",
        )
    ]
    if claim.id == "careful_1":
        numeric_findings = [
            "Absolute gain: 87.3 - 84.1 = 3.2 percentage points.",
            "Relative gain: (3.2 / 84.1) * 100 = 3.8%.",
            "The document uses percentage-point wording, so the numeric claim is properly scoped.",
        ]
    else:
        numeric_findings = []
    return ClaimAudit(
        claim=claim,
        verdict=Verdict.SUPPORTED,
        confidence="high",
        stretch_score=8 if claim.id == "careful_1" else 14,
        why="The claim is narrow, scoped, and supported by the document's own evidence and caveats.",
        weaker_supported_rewrite=claim.claim,
        supporting_evidence=supporting,
        counter_evidence=[],
        missing_context=[],
        numeric_findings=numeric_findings,
    )


def _mock_needs_receipts_audit(claim: RiskyClaim) -> ClaimAudit:
    return ClaimAudit(
        claim=claim,
        verdict=Verdict.NOT_CHECKABLE,
        confidence="medium",
        stretch_score=58 if claim.claim_type.value != "safety" else 72,
        why="The claim may be true, but the document does not provide the evidence needed to audit it.",
        weaker_supported_rewrite="The document presents this as an aspiration or positioning claim, not an evidenced result.",
        supporting_evidence=[],
        counter_evidence=[],
        missing_context=[
            "No measurement method is reported.",
            "No sample size, benchmark, user study, or external validation is attached to the claim.",
        ],
        numeric_findings=[],
    )


def _mock_agent_outputs(audit: ClaimAudit) -> list[AgentAudit]:
    support_summary = (
        "Found direct benchmark support for the narrower table values."
        if audit.supporting_evidence
        else "No direct supporting evidence was available in the deterministic fixture."
    )
    contradiction_summary = (
        "Found scope limitations, missing deployment evidence, or wording that narrows the claim."
        if audit.counter_evidence or audit.missing_context
        else "No contradictions were found for the scoped claim."
    )
    numeric_summary = (
        "Computed the absolute and relative difference from the benchmark values."
        if audit.numeric_findings
        else "No numeric calibration was applicable."
    )
    return [
        AgentAudit(
            agent="verifier",
            claim_id=audit.claim.id,
            summary=support_summary,
            duration_ms=0,
            supporting_evidence=audit.supporting_evidence,
            counter_evidence=[],
            missing_context=[],
            numeric_findings=[],
        ),
        AgentAudit(
            agent="contradiction-finder",
            claim_id=audit.claim.id,
            summary=contradiction_summary,
            duration_ms=0,
            supporting_evidence=[],
            counter_evidence=audit.counter_evidence,
            missing_context=audit.missing_context,
            numeric_findings=[],
        ),
        AgentAudit(
            agent="numeric-calibrator",
            claim_id=audit.claim.id,
            summary=numeric_summary,
            duration_ms=0,
            supporting_evidence=[],
            counter_evidence=[],
            missing_context=[],
            numeric_findings=audit.numeric_findings,
        ),
        AgentAudit(
            agent="claim-aggregator",
            claim_id=audit.claim.id,
            summary=(
                f"Combined specialist outputs into final verdict `{audit.verdict.value}` "
                f"with `{audit.confidence}` confidence."
            ),
            duration_ms=0,
            supporting_evidence=audit.supporting_evidence,
            counter_evidence=audit.counter_evidence,
            missing_context=audit.missing_context,
            numeric_findings=audit.numeric_findings,
        ),
    ]


def _merge_numeric_calibration(document: Document, audit: ClaimAudit) -> ClaimAudit:
    calibration = calibrate_numeric_claim(document.text, audit.claim)
    if calibration is None:
        return audit
    existing = set(audit.numeric_findings)
    for finding in calibration.findings:
        if finding not in existing:
            audit.numeric_findings.append(finding)
    if calibration.suggested_rewrite and audit.verdict == Verdict.OVERSTATED:
        audit.weaker_supported_rewrite = calibration.suggested_rewrite
    return audit


def _elapsed_ms(started_at: float) -> int:
    elapsed_ms = (perf_counter() - started_at) * 1000
    if elapsed_ms > 0:
        return max(1, int(elapsed_ms + 0.999))
    return 0
