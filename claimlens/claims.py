from __future__ import annotations

from pydantic import BaseModel, Field

from .gemini import GeminiClient
from .schemas import ClaimType, Document, RiskyClaim


class ClaimSet(BaseModel):
    claims: list[RiskyClaim] = Field(default_factory=list)


def extract_claims(document: Document, *, mock: bool, limit: int = 8) -> list[RiskyClaim]:
    if mock:
        return _mock_claims()

    client = GeminiClient()
    prompt = f"""
You are ClaimLens, an adversarial claim extractor for dense expert documents.

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
    return client.structured(prompt, ClaimSet).claims[:limit]


def _mock_claims() -> list[RiskyClaim]:
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

