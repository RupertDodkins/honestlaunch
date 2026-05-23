from __future__ import annotations

from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field


class ClaimType(str, Enum):
    BENCHMARK = "benchmark"
    NOVELTY = "novelty"
    CAUSAL = "causal"
    GENERALIZATION = "generalization"
    SAFETY = "safety"
    DEPLOYMENT = "deployment"
    NUMERIC = "numeric"
    CITATION_STRETCH = "citation_stretch"
    OTHER = "other"


class Verdict(str, Enum):
    SUPPORTED = "supported"
    OVERSTATED = "overstated"
    MISSING_CONTEXT = "missing_context"
    CONTRADICTED = "contradicted"
    NOT_CHECKABLE = "not_checkable"


Vibe = Literal["no cap", "mostly no cap", "sus", "cap", "needs receipts"]
Confidence = Literal["low", "medium", "high"]


class Document(BaseModel):
    title: str = "Untitled document"
    source: str
    text: str


class RiskyClaim(BaseModel):
    id: str
    claim: str
    claim_type: ClaimType = ClaimType.OTHER
    source_location: str = "unknown"
    why_risky: str
    audit_question: str


class EvidenceItem(BaseModel):
    source_title: str
    url: str | None = None
    date: str | None = None
    snippet: str
    relevance: str


class AgentAudit(BaseModel):
    agent: str
    claim_id: str
    summary: str
    supporting_evidence: list[EvidenceItem] = Field(default_factory=list)
    counter_evidence: list[EvidenceItem] = Field(default_factory=list)
    missing_context: list[str] = Field(default_factory=list)
    numeric_findings: list[str] = Field(default_factory=list)


class ClaimAudit(BaseModel):
    claim: RiskyClaim
    verdict: Verdict
    vibe: Vibe
    confidence: Confidence
    cap_score: int = Field(ge=0, le=100)
    why: str
    weaker_supported_rewrite: str
    supporting_evidence: list[EvidenceItem] = Field(default_factory=list)
    counter_evidence: list[EvidenceItem] = Field(default_factory=list)
    missing_context: list[str] = Field(default_factory=list)
    numeric_findings: list[str] = Field(default_factory=list)


class AuditReport(BaseModel):
    document: Document
    claims: list[RiskyClaim]
    audits: list[ClaimAudit]

