from __future__ import annotations

from copy import deepcopy
from typing import Any

from .archive_registry import archive_entries


DEFAULT_DISCOVERY_PROVIDERS = [
    "anthropic_deep_research",
    "openai_deep_research",
]


def find_archive_entry_by_slug(slug: str) -> dict[str, Any] | None:
    for entry in archive_entries():
        if entry.get("slug") == slug:
            return deepcopy(entry)
    return None


def build_qa_packet(
    slug: str,
    *,
    discovery_providers: list[str] | None = None,
) -> dict[str, Any]:
    entry = find_archive_entry_by_slug(slug)
    if entry is None:
        raise ValueError(f"Unknown archive slug: {slug}")
    providers = discovery_providers or list(DEFAULT_DISCOVERY_PROVIDERS)
    return {
        "version": "qa-v1",
        "slug": entry["slug"],
        "launch": {
            "lab": entry.get("lab", ""),
            "title": entry.get("title", ""),
            "model": entry.get("model", ""),
            "originalUrl": entry.get("originalUrl", ""),
            "originalLabel": entry.get("originalLabel", ""),
            "sourceNote": entry.get("sourceNote", ""),
        },
        "archiveArtifacts": {
            "html": entry.get("artifactHtml", ""),
            "json": entry.get("artifactJson", ""),
            "markdown": entry.get("artifactMd", ""),
            "evidencePacket": entry.get("evidencePacketFile", ""),
        },
        "references": list(entry.get("referenceUrls", [])),
        "discovery": {
            "providers": [
                {
                    "provider": provider,
                    "status": "pending",
                    "suspectClaims": [],
                    "notes": "",
                }
                for provider in providers
            ],
            "mergedReview": {
                "status": "pending",
                "mustCatchClaims": [],
                "niceToCatchClaims": [],
                "nonIssues": [],
                "reviewerNotes": "",
            },
        },
        "adjudication": {
            "claims": [],
        },
        "humanDecision": {
            "publishStatus": "pending",
            "decisionNotes": "",
            "reviewer": "",
            "reviewedAt": "",
        },
    }
