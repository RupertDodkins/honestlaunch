from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from .schemas import AuditReport, PublicationInfo


_MANIFEST_PATH = Path(__file__).resolve().parent.parent / "examples" / "archive_manifest.json"


@lru_cache(maxsize=1)
def load_archive_manifest() -> dict[str, Any]:
    return json.loads(_MANIFEST_PATH.read_text(encoding="utf-8"))


def archive_entries() -> list[dict[str, Any]]:
    manifest = load_archive_manifest()
    return list(manifest.get("entries", []))


def publication_info_for_report(report: AuditReport) -> PublicationInfo | None:
    if report.publication is not None:
        return report.publication
    entry = match_archive_entry(report.document.source, report.document.title)
    if entry is None:
        return None
    return PublicationInfo(
        slug=str(entry.get("slug", "")),
        lab=str(entry.get("lab", "")),
        launch_name=str(entry.get("title") or entry.get("model") or report.document.title),
        original_url=_optional_text(entry.get("originalUrl")),
        original_label=_optional_text(entry.get("originalLabel")),
        source_note=_optional_text(entry.get("sourceNote")),
        status=str(entry.get("status", "reviewed")),
        published_at=_optional_text(entry.get("publishedAt")),
        evidence_packet_url=_optional_text(entry.get("evidencePacketFile")),
        gate_status="pass" if entry.get("publicationGate", {}).get("overallPass") else "needs_review" if entry.get("publicationGate") else None,
    )


def match_archive_entry(source: str, title: str) -> dict[str, Any] | None:
    normalized_source = _normalize(source)
    normalized_title = _normalize(title)
    for entry in archive_entries():
        match = entry.get("match", {})
        source_tokens = [_normalize(value) for value in match.get("sourceContains", [])]
        title_tokens = [_normalize(value) for value in match.get("titleContains", [])]
        if source_tokens and any(token and token in normalized_source for token in source_tokens):
            return entry
        if title_tokens and any(token and token in normalized_title for token in title_tokens):
            return entry
    return None


def _normalize(value: str | None) -> str:
    return (value or "").strip().lower()


def _optional_text(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None
