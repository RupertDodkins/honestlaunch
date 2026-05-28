from __future__ import annotations

from pydantic import BaseModel, Field

from .gemini import GeminiClient
from .schemas import ClaimType, Document, RiskyClaim


class ClaimSet(BaseModel):
    claims: list[RiskyClaim] = Field(default_factory=list)


def extract_claims(document: Document, *, mock: bool, limit: int = 8) -> list[RiskyClaim]:
    if mock:
        return _mock_claims(document)[:limit]

    client = GeminiClient()
    prompt = f"""
You are HonestLaunch, an adversarial claim extractor for dense expert documents.

Extract the {limit} riskiest factual claims from the document below. Do not summarize.
Prefer claims with numeric improvements, novelty language, broad generalization,
safety/reliability language, causal language, or benchmark claims.

For each claim, include an audit question that states what would need to be true
for the claim to be justified.

Document title: {document.title}
Document source: {document.source}

DOCUMENT:
{document.text[:60000]}
"""
    return client.structured(prompt, ClaimSet, tools=False).claims[:limit]


def _mock_claims(document: Document | None = None) -> list[RiskyClaim]:
    text = (document.text if document else "").lower()
    if "careful scientific claim" in text:
        return _careful_claims()
    if "unauditable fixture" in text:
        return _needs_receipts_claims()
    return [
        RiskyClaim(
            id="c1",
            claim="Our method improves performance by 30% over prior work on real-world tasks.",
            claim_type=ClaimType.NUMERIC,
            source_location="Abstract",
            why_risky="The claim combines a large numeric improvement with broad real-world language.",
            audit_question="Do the reported benchmark numbers justify a 30% improvement and real-world generalization?",
        ),
        RiskyClaim(
            id="c2",
            claim="The system robustly generalizes across domains.",
            claim_type=ClaimType.GENERALIZATION,
            source_location="Conclusion",
            why_risky="Generalization language is stronger than typical benchmark evidence.",
            audit_question="Were multiple domains and out-of-distribution settings actually tested?",
        ),
        RiskyClaim(
            id="c3",
            claim="This is the first agentic workflow for scientific claim auditing.",
            claim_type=ClaimType.NOVELTY,
            source_location="Introduction",
            why_risky="First/novelty claims require broad literature comparison.",
            audit_question="Does prior work include similar scientific fact-checking or claim-audit systems?",
        ),
    ]


def _careful_claims() -> list[RiskyClaim]:
    return [
        RiskyClaim(
            id="careful_1",
            claim=(
                "HonestLaunch improved from 84.1% to 87.3% on Benchmark X, "
                "a 3.2 percentage-point gain under the benchmark conditions."
            ),
            claim_type=ClaimType.NUMERIC,
            source_location="Results",
            why_risky="Numeric claims are worth checking even when they appear carefully scoped.",
            audit_question="Do the reported table values support the stated absolute improvement?",
        ),
        RiskyClaim(
            id="careful_2",
            claim="The evaluation does not establish real-world deployment performance.",
            claim_type=ClaimType.DEPLOYMENT,
            source_location="Limitations",
            why_risky="This is a caveat claim; the audit should preserve it if the document states the limitation.",
            audit_question="Does the document explicitly limit the conclusion to benchmark evaluation?",
        ),
        RiskyClaim(
            id="careful_3",
            claim="The result is limited to the curated Benchmark X dataset.",
            claim_type=ClaimType.GENERALIZATION,
            source_location="Discussion",
            why_risky="Scope-limiting claims should be supported by the document's evaluation description.",
            audit_question="Does the document avoid broad generalization beyond Benchmark X?",
        ),
    ]


def _needs_receipts_claims() -> list[RiskyClaim]:
    return [
        RiskyClaim(
            id="receipts_1",
            claim="Users strongly prefer HonestLaunch over existing review tools.",
            claim_type=ClaimType.OTHER,
            source_location="Abstract",
            why_risky="Preference claims need user study data or survey evidence.",
            audit_question="Does the document report a user study, sample size, or preference measurement?",
        ),
        RiskyClaim(
            id="receipts_2",
            claim="HonestLaunch is safe for production use in regulated environments.",
            claim_type=ClaimType.SAFETY,
            source_location="Deployment",
            why_risky="Safety and regulated-production claims require concrete validation and scope.",
            audit_question="Does the document provide safety evaluation, threat model, or deployment evidence?",
        ),
        RiskyClaim(
            id="receipts_3",
            claim="HonestLaunch is the first tool to audit scientific claims with agents.",
            claim_type=ClaimType.NOVELTY,
            source_location="Introduction",
            why_risky="First/novelty claims require prior-work search.",
            audit_question="Does the document provide a literature or product comparison supporting the firstness claim?",
        ),
    ]
