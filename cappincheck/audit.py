from __future__ import annotations

import asyncio
from pydantic import BaseModel, Field

from .gemini import GeminiClient
from .schemas import AgentAudit, ClaimAudit, Document, EvidenceItem, RiskyClaim, Verdict
from .skills import load_skill


class AgentAuditSet(BaseModel):
    audits: list[AgentAudit] = Field(default_factory=list)


class ClaimAuditSet(BaseModel):
    audits: list[ClaimAudit] = Field(default_factory=list)


async def audit_claims(
    document: Document,
    claims: list[RiskyClaim],
    *,
    mock: bool,
    limit: int = 5,
) -> list[ClaimAudit]:
    selected = claims[:limit]
    if mock:
        return [_mock_audit(claim) for claim in selected]

    per_claim = await asyncio.gather(*[_audit_one(document, claim) for claim in selected])
    return list(per_claim)


async def _audit_one(document: Document, claim: RiskyClaim) -> ClaimAudit:
    print(f"Auditing {claim.id}: {claim.claim[:90]}")
    agent_results = await asyncio.gather(
        _run_skill("verifier", document, claim),
        _run_skill("contradiction-finder", document, claim),
        _run_skill("numeric-calibrator", document, claim),
    )
    print(f"Aggregating {claim.id}")
    return await _aggregate(document, claim, list(agent_results))


async def _run_skill(skill_name: str, document: Document, claim: RiskyClaim) -> AgentAudit:
    print(f"  Running {skill_name} for {claim.id}")
    skill = load_skill(skill_name)
    client = GeminiClient()
    prompt = f"""
{skill}

Return only JSON matching the AgentAudit schema.

Document title: {document.title}
Document source: {document.source}

Claim ID: {claim.id}
Claim: {claim.claim}
Claim type: {claim.claim_type}
Audit question: {claim.audit_question}

Relevant document text:
{document.text[:50000]}
"""
    return await asyncio.to_thread(client.structured, prompt, AgentAudit)


async def _aggregate(document: Document, claim: RiskyClaim, audits: list[AgentAudit]) -> ClaimAudit:
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
    return await asyncio.to_thread(client.structured, prompt, ClaimAudit)


def _mock_audit(claim: RiskyClaim) -> ClaimAudit:
    if claim.id == "c1":
        supporting = [
            EvidenceItem(
                source_title="Demo document benchmark table",
                url=None,
                snippet="Baseline: 84.1%. CappinCheck: 87.3%.",
                relevance="The table supports a 3.2-point absolute gain, not a 30% relative improvement.",
            )
        ]
        baseline, method = 84.1, 87.3
        absolute = method - baseline
        relative = (absolute / baseline) * 100
        return ClaimAudit(
            claim=claim,
            verdict=Verdict.OVERSTATED,
            vibe="cap",
            confidence="high",
            cap_score=88,
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

    vibe = "sus" if claim.claim_type.value in {"generalization", "novelty"} else "needs receipts"
    verdict = Verdict.MISSING_CONTEXT if vibe == "sus" else Verdict.NOT_CHECKABLE
    return ClaimAudit(
        claim=claim,
        verdict=verdict,
        vibe=vibe,
        confidence="medium",
        cap_score=64 if vibe == "sus" else 55,
        why="The claim may be plausible, but the demo document does not provide enough scope or external evidence.",
        weaker_supported_rewrite="The document provides preliminary evidence for a narrower version of this claim.",
        supporting_evidence=[],
        counter_evidence=[],
        missing_context=["Additional external grounding would be needed for a production verdict."],
        numeric_findings=[],
    )
