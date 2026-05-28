from __future__ import annotations

import difflib
import re

from .citations import build_tooltip_citations
from .schemas import (
    AuditReport,
    ClaimAnchor,
    ClaimAudit,
    LaunchPageView,
    RewriteDecoration,
    SnapshotBlock,
    SourceSnapshot,
)


def enrich_report_for_launch_page(report: AuditReport) -> AuditReport:
    snapshot = report.document.snapshot or SourceSnapshot(
        title=report.document.title,
        source_url=report.document.source,
        source_kind="text",
        blocks=[],
    )
    decorations: list[RewriteDecoration] = []
    citation_keys: set[str] = set()
    for audit in _editable_audits(report.audits):
        block = _best_block_for_audit(audit, snapshot.blocks)
        if block is None:
            continue
        anchor = _best_anchor(block, audit.claim.claim)
        anchor.claim_id = audit.claim.id
        citations = build_tooltip_citations(audit, report.reference_urls)
        audit.anchor = anchor
        audit.tooltip_citations = citations
        for citation in citations:
            key = (citation.url or citation.title).strip()
            if key:
                citation_keys.add(key)
        decorations.append(
            RewriteDecoration(
                claim_id=audit.claim.id,
                verdict=audit.verdict,
                original_text=audit.claim.claim,
                rewritten_text=audit.weaker_supported_rewrite,
                reason=audit.why,
                citations=citations,
                anchor=anchor,
            )
        )
    report.launch_page = LaunchPageView(
        source_title=snapshot.title,
        source_url=snapshot.source_url,
        blocks=snapshot.blocks,
        decorations=decorations,
        rewritten_claim_count=len(decorations),
        explicit_reference_count=len(citation_keys),
    )
    return report


def _editable_audits(audits: list[ClaimAudit]) -> list[ClaimAudit]:
    severity_order = {
        "contradicted": 0,
        "overstated": 1,
        "missing_context": 2,
        "not_checkable": 3,
        "supported": 4,
    }
    candidates = []
    for audit in audits:
        rewrite = audit.weaker_supported_rewrite.strip()
        if audit.verdict.value == "supported":
            continue
        if not rewrite:
            continue
        candidates.append(audit)
    return sorted(
        candidates,
        key=lambda audit: (severity_order.get(audit.verdict.value, 9), -audit.stretch_score),
    )


def _best_block_for_audit(audit: ClaimAudit, blocks: list[SnapshotBlock]) -> SnapshotBlock | None:
    best_block: SnapshotBlock | None = None
    best_score = -1.0
    source_location = audit.claim.source_location.strip().lower()
    for block in blocks:
        _, score, _ = _best_match_candidate(block.text, audit.claim.claim)
        if source_location and block.section_heading and source_location in block.section_heading.lower():
            score += 0.15
        if block.kind.startswith("h"):
            score -= 0.05
        if score > best_score:
            best_score = score
            best_block = block
    return best_block


def _best_anchor(block: SnapshotBlock, claim_text: str) -> ClaimAnchor:
    matched_text, score, match_type = _best_match_candidate(block.text, claim_text)
    if matched_text and matched_text in block.text:
        start = block.text.find(matched_text)
        end = start + len(matched_text)
    else:
        matched_text = block.text
        start = 0
        end = len(block.text)
        match_type = "block_fallback"
        score = max(score, 0.35 if block.text else 0.0)
    return ClaimAnchor(
        claim_id="",
        block_id=block.block_id,
        matched_text=matched_text,
        start_char=start,
        end_char=end,
        match_type=match_type,
        match_confidence=round(score, 4),
    )


def _best_match_candidate(block_text: str, claim_text: str) -> tuple[str, float, str]:
    if claim_text in block_text:
        return claim_text, 1.0, "exact_claim"
    candidates = _split_match_units(block_text)
    best_candidate = ""
    best_score = 0.0
    best_type = "none"
    for candidate, candidate_type in candidates:
        score = _similarity(candidate, claim_text)
        if score > best_score or (
            score == best_score and best_candidate and len(candidate) < len(best_candidate)
        ):
            best_candidate = candidate
            best_score = score
            best_type = candidate_type
    if best_candidate and best_score >= 0.45:
        return best_candidate, best_score, best_type
    block_score = _similarity(block_text, claim_text)
    if block_score >= 0.35:
        return block_text, block_score, "block_fuzzy"
    return block_text, block_score, "block_fallback"


def _split_match_units(block: str) -> list[tuple[str, str]]:
    units: list[tuple[str, str]] = []
    seen: set[str] = set()
    for sentence in _split_sentences(block):
        normalized_sentence = _normalized(sentence)
        if normalized_sentence and normalized_sentence not in seen:
            units.append((sentence, "sentence_fuzzy"))
            seen.add(normalized_sentence)
        fragments = re.split(
            r"(?i)\s+\band\b\s+|\s+\bbut\b\s+|\s+\bwhile\b\s+|,\s+|;\s+|:\s+",
            sentence,
        )
        for fragment in fragments:
            cleaned = fragment.strip()
            normalized_fragment = _normalized(cleaned)
            if len(cleaned.split()) < 4 or not normalized_fragment or normalized_fragment in seen:
                continue
            units.append((cleaned, "clause_fuzzy"))
            seen.add(normalized_fragment)
    return units


def _split_sentences(block: str) -> list[str]:
    if not block.strip():
        return []
    if "\n" in block:
        return [line.strip() for line in block.splitlines() if line.strip()]
    parts = re.split(r"(?<=[.!?])\s+", block)
    return [part.strip() for part in parts if part.strip()]


def _similarity(left: str, right: str) -> float:
    return difflib.SequenceMatcher(None, _normalized(left), _normalized(right)).ratio()


def _normalized(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().lower()
