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


class SnapshotBlock(BaseModel):
    block_id: str
    kind: str
    text: str
    section_heading: str | None = None
    source_order: int = 0


class SourceSnapshot(BaseModel):
    title: str = "Untitled document"
    source_url: str
    source_kind: str = "text"
    blocks: list[SnapshotBlock] = Field(default_factory=list)


class Document(BaseModel):
    title: str = "Untitled document"
    source: str
    text: str
    snapshot: SourceSnapshot | None = None


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
    duration_ms: int | None = None
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


class ClaimTimingProfile(BaseModel):
    claim_id: str
    total_duration_ms: int = 0
    verifier_ms: int = 0
    contradiction_finder_ms: int = 0
    numeric_calibrator_ms: int = 0
    aggregator_ms: int = 0
    contrast_ms: int = 0


class ClaimAnchor(BaseModel):
    claim_id: str
    block_id: str
    matched_text: str
    start_char: int = 0
    end_char: int = 0
    match_type: str = "none"
    match_confidence: float = Field(default=0.0, ge=0.0, le=1.0)


class TooltipCitation(BaseModel):
    title: str
    url: str | None = None
    snippet: str = ""
    why_relevant: str = ""


class RewriteDecoration(BaseModel):
    claim_id: str
    verdict: Verdict
    original_text: str
    rewritten_text: str
    reason: str
    citations: list[TooltipCitation] = Field(default_factory=list)
    anchor: ClaimAnchor


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
    claim_timing: ClaimTimingProfile | None = None
    anchor: ClaimAnchor | None = None
    tooltip_citations: list[TooltipCitation] = Field(default_factory=list)


class RunTimingProfile(BaseModel):
    total_duration_ms: int = 0
    load_document_ms: int = 0
    extract_claims_ms: int = 0
    audit_claims_ms: int = 0
    contrast_duration_ms: int = 0
    claims_extracted: int = 0
    claims_audited: int = 0
    agent_passes: int = 0
    contrast_claims: int = 0
    unique_source_count: int = 0
    claim_profiles: list[ClaimTimingProfile] = Field(default_factory=list)


class LaunchPageView(BaseModel):
    source_title: str
    source_url: str
    blocks: list[SnapshotBlock] = Field(default_factory=list)
    decorations: list[RewriteDecoration] = Field(default_factory=list)
    rewritten_claim_count: int = 0
    explicit_reference_count: int = 0
    primary_view: str = "audited_launch_page"


class PublicationInfo(BaseModel):
    slug: str
    lab: str = ""
    launch_name: str = ""
    original_url: str | None = None
    original_label: str | None = None
    source_note: str | None = None
    status: str = "reviewed"
    published_at: str | None = None
    evidence_packet_url: str | None = None
    gate_status: str | None = None
    disclaimer: str = (
        "Audited modified version of the original source. This page is provided for analysis "
        "and commentary and is not the original publisher's page."
    )


class AuditReport(BaseModel):
    document: Document
    claims: list[RiskyClaim]
    audits: list[ClaimAudit]
    runtime: str = "mock"
    mode: str = "deterministic_fallback"
    model: str | None = None
    contrast_enabled: bool = False
    reference_urls: list[str] = Field(default_factory=list)
    run_profile: RunTimingProfile | None = None
    launch_page: LaunchPageView | None = None
    publication: PublicationInfo | None = None
