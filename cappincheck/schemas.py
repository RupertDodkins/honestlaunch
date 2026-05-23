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


Confidence = Literal["low", "medium", "high"]
SourceType = Literal[
    "official_doc",
    "paper",
    "standard",
    "dataset",
    "benchmark",
    "government",
    "academic",
    "vendor_doc",
    "blog",
    "unknown",
]
SourceStance = Literal["supports", "narrows", "contradicts", "irrelevant", "unclear"]
DeltaType = Literal[
    "same",
    "narrower_than_claim",
    "broader_than_claim",
    "missing_context",
    "contradicted",
    "not_checkable",
]


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


class ReferenceSource(BaseModel):
    url: str | None = None
    title: str = "Reference source"
    source_type: SourceType = "unknown"
    why_relevant: str = ""
    authority_score: int = Field(default=50, ge=0, le=100)


class ContrastSource(BaseModel):
    url: str | None = None
    title: str = "Reference source"
    stance: SourceStance = "unclear"
    evidence_summary: str
    key_qualification: str = ""


class EvidenceContrast(BaseModel):
    claim_id: str
    claim_text: str
    reference_sources: list[ReferenceSource] = Field(default_factory=list)
    best_sources: list[ContrastSource] = Field(default_factory=list)
    delta_type: DeltaType = "not_checkable"
    delta_explanation: str
    suggested_rewrite: str
    recommended_verdict: Verdict = Verdict.NOT_CHECKABLE
    confidence: Confidence = "medium"


class ClaimAudit(BaseModel):
    claim: RiskyClaim
    verdict: Verdict
    confidence: Confidence
    stretch_score: int = Field(ge=0, le=100)
    why: str
    weaker_supported_rewrite: str
    supporting_evidence: list[EvidenceItem] = Field(default_factory=list)
    counter_evidence: list[EvidenceItem] = Field(default_factory=list)
    missing_context: list[str] = Field(default_factory=list)
    numeric_findings: list[str] = Field(default_factory=list)
    agent_outputs: list[AgentAudit] = Field(default_factory=list)
    contrast: EvidenceContrast | None = None


class AuditReport(BaseModel):
    document: Document
    claims: list[RiskyClaim]
    audits: list[ClaimAudit]
    runtime: str = "mock"
    mode: str = "deterministic_fallback"
    model: str | None = None
    contrast_enabled: bool = False
    reference_urls: list[str] = Field(default_factory=list)
