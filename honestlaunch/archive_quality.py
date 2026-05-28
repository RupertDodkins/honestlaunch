from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from statistics import mean
from typing import Any

from .archive_registry import load_archive_manifest
from .ingest import load_document
from .schemas import AuditReport, ClaimAudit, Verdict


def load_report(path: Path) -> AuditReport:
    from .canonical_hardening import harden_report

    report = AuditReport.model_validate(json.loads(path.read_text(encoding="utf-8")))
    return harden_report(report)


def hydrate_report_document(report: AuditReport) -> AuditReport:
    snapshot = report.document.snapshot
    if snapshot is not None and snapshot.blocks:
        return report
    try:
        hydrated = load_document(report.document.source)
    except Exception:
        return report
    report.document.snapshot = hydrated.snapshot
    if hydrated.text:
        report.document.text = hydrated.text
    if hydrated.title and report.document.title != hydrated.title:
        report.document.title = hydrated.title
    return report


def report_metrics(report: AuditReport) -> dict[str, Any]:
    audits = report.audits
    rewritten = [audit for audit in audits if audit.verdict != Verdict.SUPPORTED]
    verdicts = verdict_counts(audits)
    rewritten_count = len(rewritten)
    cited_count = sum(1 for audit in rewritten if audit.tooltip_citations)
    anchored_count = sum(1 for audit in rewritten if audit.anchor is not None)
    blocks_preserved = len(report.launch_page.blocks) if report.launch_page else len(report.document.snapshot.blocks) if report.document.snapshot else 0
    evidence_depth = sum(len(audit.supporting_evidence) + len(audit.counter_evidence) for audit in audits)
    return {
        "claimsAudited": len(audits),
        "rewrittenClaims": rewritten_count,
        "averageStretch": round(mean(audit.stretch_score for audit in audits)) if audits else 0,
        "verdictCounts": verdicts,
        "tooltipCitationCoveragePct": _pct(cited_count, rewritten_count),
        "anchorCoveragePct": _pct(anchored_count, rewritten_count),
        "blocksPreserved": blocks_preserved,
        "explicitReferenceCount": len(report.reference_urls),
        "evidenceItemCount": evidence_depth,
    }


def publication_gate(report: AuditReport) -> dict[str, Any]:
    metrics = report_metrics(report)
    publication = report.publication
    checks = {
        "hasModifiedNotice": bool(publication and publication.disclaimer),
        "hasOriginalLink": bool((publication and publication.original_url) or report.document.source),
        "hasEvidencePacketLink": bool(publication and publication.evidence_packet_url),
        "allEditedClaimsAnchored": metrics["rewrittenClaims"] == 0 or metrics["anchorCoveragePct"] == 100,
        "allEditedClaimsCited": metrics["rewrittenClaims"] == 0 or metrics["tooltipCitationCoveragePct"] == 100,
        "hasPreservedBlocks": metrics["blocksPreserved"] > 0,
    }
    return {
        "overallPass": all(checks.values()),
        "checks": checks,
    }


def build_evidence_packet(
    entry: dict[str, Any],
    report: AuditReport,
    *,
    artifact_html: str,
    artifact_json: str,
    artifact_md: str,
    published_at: str,
) -> dict[str, Any]:
    publication = report.publication
    original_url = (publication.original_url if publication else None) or entry.get("originalUrl") or report.document.source
    snapshot = report.document.snapshot
    source_kind = snapshot.source_kind if snapshot else _source_kind_from_source(report.document.source)
    rendered_from = "original_source"
    if report.document.source and not str(report.document.source).startswith(("http://", "https://")):
        rendered_from = "local_proxy_or_fixture"
    if source_kind == "pdf":
        rendered_from = "canonical_pdf"
    return {
        "slug": entry.get("slug"),
        "lab": entry.get("lab"),
        "title": entry.get("title"),
        "publishedAt": published_at,
        "status": entry.get("status", "reviewed"),
        "primarySource": {
            "title": report.document.title,
            "url": original_url,
            "sourceKind": source_kind,
            "renderedFrom": rendered_from,
            "documentSource": report.document.source,
            "sourceNote": entry.get("sourceNote", ""),
        },
        "auditRuntime": {
            "mode": report.mode,
            "runtime": report.runtime,
            "model": report.model,
            "contrastEnabled": report.contrast_enabled,
        },
        "references": {
            "policy": "explicit_reference_urls",
            "count": len(report.reference_urls),
            "urls": list(report.reference_urls),
        },
        "artifacts": {
            "html": artifact_html,
            "json": artifact_json,
            "markdown": artifact_md,
        },
        "metrics": report_metrics(report),
    }


def refresh_archive_metadata(root: Path) -> dict[str, Any]:
    from .anchor_map import enrich_report_for_launch_page
    from .archive_registry import publication_info_for_report

    manifest_path = root / "examples" / "archive_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    evidence_dir = root / "examples" / "evidence_packets"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    featured_metrics: list[dict[str, Any]] = []

    for entry in manifest.get("entries", []):
        artifact_json = str(entry.get("artifactJson", ""))
        if not artifact_json:
            continue
        report_path = root / "examples" / artifact_json
        if not report_path.exists():
            continue
        report = load_report(report_path)
        report = hydrate_report_document(report)
        if not report.reference_urls and entry.get("referenceUrls"):
            report.reference_urls = list(entry.get("referenceUrls", []))
        report = enrich_report_for_launch_page(report)
        report.publication = publication_info_for_report(report)
        metrics = report_metrics(report)
        published_at = _mtime_date(report_path)
        evidence_packet_file = f"evidence_packets/{entry['slug']}.json"
        if report.publication is not None:
            report.publication.published_at = published_at
            report.publication.evidence_packet_url = evidence_packet_file
            gate = publication_gate(report)
            report.publication.gate_status = "pass" if gate["overallPass"] else "needs_review"
        else:
            gate = publication_gate(report)
        evidence_packet = build_evidence_packet(
            entry,
            report,
            artifact_html=str(entry.get("artifactHtml", "")),
            artifact_json=artifact_json,
            artifact_md=str(entry.get("artifactMd", "")),
            published_at=published_at,
        )
        (evidence_dir / f"{entry['slug']}.json").write_text(
            json.dumps(evidence_packet, indent=2) + "\n",
            encoding="utf-8",
        )
        entry["publishedAt"] = published_at
        entry["evidencePacketFile"] = evidence_packet_file
        entry["referenceUrls"] = list(report.reference_urls)
        entry["metrics"] = metrics
        entry["publicationGate"] = gate
        entry["evidencePacket"] = {
            "primarySourceKind": evidence_packet["primarySource"]["sourceKind"],
            "renderedFrom": evidence_packet["primarySource"]["renderedFrom"],
            "referenceCount": evidence_packet["references"]["count"],
        }
        if entry.get("category") == "featured":
            featured_metrics.append(metrics)

    manifest["site"]["metrics"] = collection_metrics(manifest)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def collection_metrics(manifest: dict[str, Any]) -> dict[str, Any]:
    entries = [entry for entry in manifest.get("entries", []) if entry.get("category") == "featured"]
    if not entries:
        return {
            "featuredCount": 0,
            "labsCovered": 0,
            "averageStretch": 0,
            "gatePassRatePct": 0,
            "tooltipCitationCoveragePct": 0,
        }
    gate_passes = sum(1 for entry in entries if entry.get("publicationGate", {}).get("overallPass"))
    tooltip_coverage = [entry.get("metrics", {}).get("tooltipCitationCoveragePct", 0) for entry in entries]
    average_stretch = [entry.get("metrics", {}).get("averageStretch", 0) for entry in entries]
    return {
        "featuredCount": len(entries),
        "labsCovered": len({entry.get("lab") for entry in entries if entry.get("lab")}),
        "averageStretch": round(mean(average_stretch)) if average_stretch else 0,
        "gatePassRatePct": _pct(gate_passes, len(entries)),
        "tooltipCitationCoveragePct": round(mean(tooltip_coverage)) if tooltip_coverage else 0,
    }


def gold_set_results(root: Path, gold_set_path: Path) -> dict[str, Any]:
    if not gold_set_path.exists():
        return {
            "reviewedCount": 0,
            "verdictAgreementPct": 0,
            "rewriteCoveragePct": 0,
            "entries": [],
        }
    manifest = load_archive_manifest()
    entry_lookup = {entry["slug"]: entry for entry in manifest.get("entries", [])}
    gold = json.loads(gold_set_path.read_text(encoding="utf-8"))
    rows: list[dict[str, Any]] = []
    verdict_matches = 0
    rewrite_matches = 0
    reviewed_count = 0
    for item in gold.get("claims", []):
        if item.get("reviewState") not in {"reviewed", "seed_reviewed"}:
            continue
        reviewed_count += 1
        entry = entry_lookup.get(item.get("slug"))
        if not entry:
            continue
        report = load_report(root / "examples" / str(entry.get("artifactJson")))
        audit = next((candidate for candidate in report.audits if candidate.claim.id == item.get("claimId")), None)
        if audit is None:
            rows.append({"claimId": item.get("claimId"), "slug": item.get("slug"), "status": "missing_claim"})
            continue
        verdict_match = audit.verdict.value == item.get("expectedVerdict")
        verdict_matches += 1 if verdict_match else 0
        rewrite_expectations = item.get("rewriteMustContain", [])
        rewrite_match = all(token.lower() in audit.weaker_supported_rewrite.lower() for token in rewrite_expectations)
        rewrite_matches += 1 if rewrite_match else 0
        rows.append(
            {
                "slug": item.get("slug"),
                "claimId": item.get("claimId"),
                "expectedVerdict": item.get("expectedVerdict"),
                "actualVerdict": audit.verdict.value,
                "verdictMatch": verdict_match,
                "rewriteMatch": rewrite_match,
            }
        )
    return {
        "reviewedCount": reviewed_count,
        "verdictAgreementPct": _pct(verdict_matches, reviewed_count),
        "rewriteCoveragePct": _pct(rewrite_matches, reviewed_count),
        "entries": rows,
    }


def archive_scorecard(root: Path, gold_set_path: Path) -> dict[str, Any]:
    manifest = json.loads((root / "examples" / "archive_manifest.json").read_text(encoding="utf-8"))
    site_metrics = manifest.get("site", {}).get("metrics", {})
    featured = [entry for entry in manifest.get("entries", []) if entry.get("category") == "featured"]
    report_html_paths = [root / "examples" / str(entry.get("artifactHtml", "")) for entry in featured]
    report_markup = [path.read_text(encoding="utf-8") for path in report_html_paths if path.exists()]
    original_link_coverage = _pct(
        sum(1 for entry in featured if entry.get("originalUrl")),
        len(featured),
    )
    notice_coverage = _pct(sum(1 for markup in report_markup if "Audited modified version" in markup), len(featured))
    method_exists = 100 if (root / "examples" / "methodology.html").exists() else 0
    archive_exists = 100 if (root / "examples" / "index.html").exists() else 0
    report_surface_coverage = _pct(
        sum(1 for markup in report_markup if "Audited Launch Page" in markup and "Audit Ledger" in markup),
        len(featured),
    )
    citation_coverage = round(mean(entry.get("metrics", {}).get("tooltipCitationCoveragePct", 0) for entry in featured)) if featured else 0
    anchor_coverage = round(mean(entry.get("metrics", {}).get("anchorCoveragePct", 0) for entry in featured)) if featured else 0
    evidence_packet_coverage = _pct(sum(1 for entry in featured if entry.get("evidencePacketFile")), len(featured))
    gate_pass_rate = site_metrics.get("gatePassRatePct", 0)
    source_note_coverage = _pct(sum(1 for entry in featured if entry.get("sourceNote")), len(featured))
    gold_results = gold_set_results(root, gold_set_path)
    gold_set_coverage_factor = min(gold_results["reviewedCount"] / 20, 1.0)
    blocks_coverage = _pct(sum(1 for entry in featured if entry.get("metrics", {}).get("blocksPreserved", 0) > 0), len(featured))

    first_glance = round((archive_exists * 0.2) + (method_exists * 0.15) + (original_link_coverage * 0.3) + (notice_coverage * 0.2) + (report_surface_coverage * 0.15))
    trust = round((citation_coverage * 0.35) + (anchor_coverage * 0.25) + (evidence_packet_coverage * 0.2) + (gate_pass_rate * 0.2))
    raw_judgment = round((gold_results["verdictAgreementPct"] * 0.7) + (gold_results["rewriteCoveragePct"] * 0.3))
    judgment = round(raw_judgment * gold_set_coverage_factor)
    fidelity = round((blocks_coverage * 0.35) + (anchor_coverage * 0.35) + (source_note_coverage * 0.15) + (report_surface_coverage * 0.15))
    archive_usefulness = round((_pct(len(featured), 4) * 0.25) + (method_exists * 0.15) + (evidence_packet_coverage * 0.2) + (gate_pass_rate * 0.2) + (archive_exists * 0.2))

    overall = round(
        (first_glance * 0.2)
        + (trust * 0.25)
        + (judgment * 0.25)
        + (fidelity * 0.15)
        + (archive_usefulness * 0.15)
    )
    return {
        "overallScore": overall,
        "categories": {
            "firstGlanceLegibility": first_glance,
            "trustInspectability": trust,
            "judgmentQuality": judgment,
            "pageFidelityPolish": fidelity,
            "archiveUsefulnessCoherence": archive_usefulness,
        },
        "proxies": {
            "originalLinkCoveragePct": original_link_coverage,
            "modifiedNoticeCoveragePct": notice_coverage,
            "reportSurfaceCoveragePct": report_surface_coverage,
            "tooltipCitationCoveragePct": citation_coverage,
            "anchorCoveragePct": anchor_coverage,
            "evidencePacketCoveragePct": evidence_packet_coverage,
            "gatePassRatePct": gate_pass_rate,
            "sourceNoteCoveragePct": source_note_coverage,
            "blocksPreservedCoveragePct": blocks_coverage,
            "featuredCount": len(featured),
            "featuredAverageStretch": site_metrics.get("averageStretch", 0),
            "goldSetCoverageFactorPct": round(gold_set_coverage_factor * 100),
        },
        "goldSet": gold_results,
        "entries": [
            {
                "slug": entry.get("slug"),
                "title": entry.get("title"),
                "metrics": entry.get("metrics", {}),
                "publicationGate": entry.get("publicationGate", {}),
            }
            for entry in featured
        ],
    }


def write_scorecard_markdown(scorecard: dict[str, Any], path: Path) -> None:
    lines = [
        "# Archive Quality Score",
        "",
        f"- Overall score: `{scorecard['overallScore']}/100`",
        f"- First-glance legibility: `{scorecard['categories']['firstGlanceLegibility']}/100`",
        f"- Trust and inspectability: `{scorecard['categories']['trustInspectability']}/100`",
        f"- Judgment quality: `{scorecard['categories']['judgmentQuality']}/100`",
        f"- Page fidelity and polish: `{scorecard['categories']['pageFidelityPolish']}/100`",
        f"- Archive usefulness and coherence: `{scorecard['categories']['archiveUsefulnessCoherence']}/100`",
        "",
        "## Proxy Metrics",
        "",
        f"- Featured pages: `{scorecard['proxies']['featuredCount']}`",
        f"- Original-link coverage: `{scorecard['proxies']['originalLinkCoveragePct']}%`",
        f"- Modified-notice coverage: `{scorecard['proxies']['modifiedNoticeCoveragePct']}%`",
        f"- Tooltip-citation coverage on rewritten claims: `{scorecard['proxies']['tooltipCitationCoveragePct']}%`",
        f"- Anchor coverage on rewritten claims: `{scorecard['proxies']['anchorCoveragePct']}%`",
        f"- Evidence-packet coverage: `{scorecard['proxies']['evidencePacketCoveragePct']}%`",
        f"- Publication-gate pass rate: `{scorecard['proxies']['gatePassRatePct']}%`",
        f"- Average stretch across featured archive: `{scorecard['proxies']['featuredAverageStretch']}/100`",
        f"- Gold-set coverage factor: `{scorecard['proxies']['goldSetCoverageFactorPct']}%`",
        "",
        "## Gold Set",
        "",
        f"- Reviewed claims: `{scorecard['goldSet']['reviewedCount']}`",
        f"- Verdict agreement: `{scorecard['goldSet']['verdictAgreementPct']}%`",
        f"- Rewrite expectation coverage: `{scorecard['goldSet']['rewriteCoveragePct']}%`",
        "",
        "## Per-Entry Snapshot",
        "",
    ]
    for entry in scorecard["entries"]:
        metrics = entry["metrics"]
        gate = entry["publicationGate"]
        lines.extend(
            [
                f"### {entry['title']}",
                "",
                f"- Claims audited: `{metrics.get('claimsAudited', 0)}`",
                f"- Rewritten claims: `{metrics.get('rewrittenClaims', 0)}`",
                f"- Average stretch: `{metrics.get('averageStretch', 0)}/100`",
                f"- Tooltip-citation coverage: `{metrics.get('tooltipCitationCoveragePct', 0)}%`",
                f"- Anchor coverage: `{metrics.get('anchorCoveragePct', 0)}%`",
                f"- Publication gate: `{'pass' if gate.get('overallPass') else 'needs_review'}`",
                "",
            ]
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def improvement_recommendations(scorecard: dict[str, Any]) -> list[str]:
    recs: list[str] = []
    if scorecard["goldSet"]["reviewedCount"] < 12:
        recs.append("Expand the reviewed gold set beyond the current seed claims so judgment quality stops resting on a tiny sample.")
    if scorecard["proxies"]["tooltipCitationCoveragePct"] < 100:
        recs.append("Bring tooltip-citation coverage on rewritten claims to 100% before treating the archive as a durable reference.")
    if scorecard["proxies"]["anchorCoveragePct"] < 100:
        recs.append("Fix any remaining unanchored rewritten claims so every visible change maps to a concrete source span.")
    if scorecard["proxies"]["gatePassRatePct"] < 100:
        recs.append("Do not add more launches until every featured page passes the publication gate end to end.")
    if scorecard["proxies"]["sourceNoteCoveragePct"] < 100:
        recs.append("Document every proxy or PDF fallback clearly so skeptical readers understand what was actually rendered.")
    return recs


def verdict_counts(audits: list[ClaimAudit]) -> dict[str, int]:
    counts = {verdict.value: 0 for verdict in Verdict}
    for audit in audits:
        counts[audit.verdict.value] += 1
    return counts


def _pct(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        return 100 if numerator <= 0 else 0
    return round((numerator / denominator) * 100)


def _source_kind_from_source(source: str) -> str:
    lower = source.lower()
    if lower.endswith(".pdf"):
        return "pdf"
    if lower.startswith(("http://", "https://")):
        return "html"
    return "text"


def _mtime_date(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime).date().isoformat()
