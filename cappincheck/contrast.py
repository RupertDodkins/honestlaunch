from __future__ import annotations

import asyncio

from pydantic import BaseModel, Field

from .gemini import GeminiClient
from .schemas import ClaimAudit, ContrastSource, Document, EvidenceContrast, ReferenceSource, Verdict


class ContrastSet(BaseModel):
    contrasts: list[EvidenceContrast] = Field(default_factory=list)


def top_contrast_candidates(audits: list[ClaimAudit], limit: int) -> list[ClaimAudit]:
    return sorted(audits, key=lambda audit: audit.cap_score, reverse=True)[:limit]


async def apply_contrast(
    document: Document,
    audits: list[ClaimAudit],
    *,
    mock: bool,
    reference_urls: list[str],
    contrast_top: int,
) -> list[ClaimAudit]:
    if contrast_top < 1:
        return audits
    candidates = top_contrast_candidates(audits, contrast_top)
    if mock:
        contrasts = [_mock_contrast(audit) for audit in candidates]
    else:
        contrasts = await _live_contrasts(document, candidates, reference_urls)
    by_claim_id = {contrast.claim_id: contrast for contrast in contrasts}
    for audit in audits:
        contrast = by_claim_id.get(audit.claim.id)
        if contrast is None:
            continue
        audit.contrast = contrast
        _merge_contrast_verdict(audit, contrast)
    return audits


async def _live_contrasts(
    document: Document,
    audits: list[ClaimAudit],
    reference_urls: list[str],
) -> list[EvidenceContrast]:
    if not reference_urls:
        raise ValueError("--contrast requires at least one --reference URL unless --mock is used.")
    return list(
        await asyncio.gather(
            *[_live_contrast(document, audit, reference_urls) for audit in audits],
        )
    )


async def _live_contrast(document: Document, audit: ClaimAudit, reference_urls: list[str]) -> EvidenceContrast:
    client = GeminiClient()
    references = "\n".join(f"- {url}" for url in reference_urls)
    prompt = f"""
You are CappinCheck Evidence Contrast Mode.

Compare the exact claim wording against the provided reference URLs. Your task is reference fidelity, not universal truth.
Use URL Context and Google Search only to inspect the provided references and resolve the referenced pages when needed.

Focus on:
- scope overreach
- causality vs correlation
- benchmark limitations
- sample size or dataset limitations
- dates and version drift
- numeric mismatch
- uncertainty language
- missing qualifiers

Return only JSON matching the EvidenceContrast schema.

Document title: {document.title}
Document source: {document.source}

Claim ID: {audit.claim.id}
Claim text: {audit.claim.claim}
Current audit verdict: {audit.verdict.value}
Current audit reason: {audit.why}
Current rewrite: {audit.weaker_supported_rewrite}

Reference URLs:
{references}

Relevant document context:
{document.text[:20000]}
"""
    return await asyncio.to_thread(client.structured, prompt, EvidenceContrast)


def _merge_contrast_verdict(audit: ClaimAudit, contrast: EvidenceContrast) -> None:
    if contrast.recommended_verdict == Verdict.NOT_CHECKABLE:
        return
    audit.verdict = contrast.recommended_verdict
    audit.confidence = contrast.confidence
    audit.why = contrast.delta_explanation
    audit.weaker_supported_rewrite = contrast.suggested_rewrite
    if contrast.recommended_verdict == Verdict.SUPPORTED:
        audit.vibe = "no cap"
        audit.cap_score = min(audit.cap_score, 20)
    elif contrast.recommended_verdict == Verdict.MISSING_CONTEXT:
        audit.vibe = "sus"
        audit.cap_score = max(audit.cap_score, 60)
    elif contrast.recommended_verdict in {Verdict.OVERSTATED, Verdict.CONTRADICTED}:
        audit.vibe = "cap"
        audit.cap_score = max(audit.cap_score, 80)


def _mock_contrast(audit: ClaimAudit) -> EvidenceContrast:
    if audit.claim.id == "c1":
        return EvidenceContrast(
            claim_id=audit.claim.id,
            claim_text=audit.claim.claim,
            reference_sources=[
                ReferenceSource(
                    url="https://example.org/benchmark-x-report",
                    title="Benchmark X Report",
                    source_type="benchmark",
                    why_relevant="Contains the baseline and CappinCheck benchmark scores used by the claim.",
                    authority_score=85,
                )
            ],
            best_sources=[
                ContrastSource(
                    url="https://example.org/benchmark-x-report",
                    title="Benchmark X Report",
                    stance="narrows",
                    evidence_summary="The reference reports 84.1% for the baseline and 87.3% for CappinCheck on Benchmark X.",
                    key_qualification="The evidence is one curated benchmark, not real-world tasks; the computed gain is 3.2 percentage points and 3.8% relative.",
                )
            ],
            delta_type="narrower_than_claim",
            delta_explanation=(
                "The reference supports a narrower benchmark improvement, but not a 30% improvement on real-world tasks."
            ),
            suggested_rewrite=(
                "CappinCheck improves from 84.1% to 87.3% on Benchmark X, "
                "a 3.2 percentage-point gain and 3.8% relative improvement under the benchmark conditions."
            ),
            recommended_verdict=Verdict.OVERSTATED,
            confidence="high",
        )
    if audit.claim.claim_type.value == "generalization":
        return EvidenceContrast(
            claim_id=audit.claim.id,
            claim_text=audit.claim.claim,
            reference_sources=[
                ReferenceSource(
                    url="https://example.org/benchmark-x-report",
                    title="Benchmark X Report",
                    source_type="benchmark",
                    why_relevant="Defines the evaluation setting and its limitations.",
                    authority_score=85,
                )
            ],
            best_sources=[
                ContrastSource(
                    url="https://example.org/benchmark-x-report",
                    title="Benchmark X Report",
                    stance="narrows",
                    evidence_summary="The reference describes curated technical claims from public documents.",
                    key_qualification="It does not evaluate clinical, legal, private-enterprise, or real-world deployment settings.",
                )
            ],
            delta_type="missing_context",
            delta_explanation=(
                "The claim generalizes beyond the reference, which only supports performance on curated Benchmark X."
            ),
            suggested_rewrite=(
                "CappinCheck generalizes across the curated domains represented in Benchmark X; "
                "real-world deployment performance was not evaluated."
            ),
            recommended_verdict=Verdict.MISSING_CONTEXT,
            confidence="high",
        )
    return EvidenceContrast(
        claim_id=audit.claim.id,
        claim_text=audit.claim.claim,
        reference_sources=[],
        best_sources=[],
        delta_type="not_checkable",
        delta_explanation="No deterministic contrast fixture is available for this claim.",
        suggested_rewrite=audit.weaker_supported_rewrite,
        recommended_verdict=Verdict.NOT_CHECKABLE,
        confidence="low",
    )
