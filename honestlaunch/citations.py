from __future__ import annotations

import re
from urllib.parse import urlparse

from .schemas import ClaimAudit, ContrastSource, ReferenceSource, TooltipCitation


def build_tooltip_citations(audit: ClaimAudit, reference_urls: list[str]) -> list[TooltipCitation]:
    citations: list[TooltipCitation] = []
    explicit_references = audit.contrast.reference_sources if audit.contrast else []
    best_sources = audit.contrast.best_sources if audit.contrast else []
    seen: set[str] = set()
    if reference_urls:
        for explicit_url in _select_explicit_reference_urls(audit, reference_urls):
            if explicit_url in seen:
                continue
            seen.add(explicit_url)
            reference = _best_reference_for_explicit_url(explicit_url, explicit_references)
            best = _best_matching_source(reference, best_sources) if reference else _best_source_for_explicit_url(explicit_url, best_sources)
            citations.append(
                TooltipCitation(
                    title=canonical_source_title("", explicit_url),
                    url=explicit_url,
                    snippet=best.evidence_summary if best and _same_host(best.url, explicit_url) else "",
                    why_relevant=(
                        best.key_qualification
                        if best and best.key_qualification
                        else reference.why_relevant
                        if reference and reference.why_relevant
                        else "Explicit reference URL supplied for the contrast pass."
                    ),
                )
            )
        return citations
    if explicit_references:
        for reference in explicit_references:
            key = reference.url or reference.title
            if key in seen:
                continue
            seen.add(key)
            best = _best_matching_source(reference, best_sources)
            citations.append(
                TooltipCitation(
                    title=canonical_source_title(reference.title, reference.url),
                    url=reference.url,
                    snippet=best.evidence_summary if best else "",
                    why_relevant=(best.key_qualification if best and best.key_qualification else reference.why_relevant),
                )
            )
    else:
        for url in reference_urls[:2]:
            if url in seen:
                continue
            seen.add(url)
            citations.append(
                TooltipCitation(
                    title=canonical_source_title("", url),
                    url=url,
                    snippet="",
                    why_relevant="Explicit reference URL supplied for the contrast pass.",
                )
            )
    return citations


def canonical_source_title(title: str | None, url: str | None) -> str:
    cleaned = _clean_title(title or "")
    if cleaned and not _is_placeholder_title(cleaned):
        return cleaned
    if not url:
        return "Reference source"
    parsed = urlparse(url)
    host = parsed.netloc.replace("www.", "")
    path = parsed.path.strip("/")
    if "evals-methodology" in path:
        tail = path.split("/")[-1]
        tail = re.sub(r"[-_]+", " ", tail).strip()
        return f"{_title_case(tail)} evaluations methodology - {host}" if host else f"{_title_case(tail)} evaluations methodology"
    if path.endswith("docs/pricing"):
        return f"Gemini API pricing - {host}" if host else "Gemini API pricing"
    if "api/pricing" in path:
        return f"API pricing - {host}" if host else "API pricing"
    if "mcp_atlas" in path:
        return "MCP Atlas - Scale Labs"
    if host == "charxiv.github.io":
        return "CharXiv benchmark"
    if not path:
        return host or "Reference source"
    tail = path.split("/")[-1]
    tail = re.sub(r"\.(html|htm|pdf|md)$", "", tail, flags=re.I)
    tail = re.sub(r"[-_]+", " ", tail).strip()
    tail = re.sub(r"\b(\d+)\s+(\d+)\b", r"\1.\2", tail)
    if not tail:
        return host or "Reference source"
    return f"{_title_case(tail)} - {host}" if host else _title_case(tail)


def _best_matching_source(reference: ReferenceSource, best_sources: list[ContrastSource]) -> ContrastSource | None:
    if not best_sources:
        return None
    reference_url = (reference.url or "").strip().lower()
    reference_title = canonical_source_title(reference.title, reference.url).lower()
    for source in best_sources:
        if reference_url and source.url and source.url.strip().lower() == reference_url:
            return source
    for source in best_sources:
        source_title = canonical_source_title(source.title, source.url).lower()
        if source_title == reference_title:
            return source
    return best_sources[0]


def _best_reference_for_explicit_url(
    explicit_url: str, references: list[ReferenceSource]
) -> ReferenceSource | None:
    if not references:
        return None
    for reference in references:
        if _urls_match(reference.url, explicit_url):
            return reference
    for reference in references:
        if _same_host(reference.url, explicit_url):
            return reference
    return references[0]


def _best_source_for_explicit_url(
    explicit_url: str, best_sources: list[ContrastSource]
) -> ContrastSource | None:
    if not best_sources:
        return None
    for source in best_sources:
        if _urls_match(source.url, explicit_url):
            return source
    for source in best_sources:
        if _same_host(source.url, explicit_url):
            return source
    return best_sources[0]


def _clean_title(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    return value


def _is_placeholder_title(value: str) -> bool:
    normalized = value.strip().lower().rstrip(".")
    if normalized in {"reference source", "source returned by gemini grounding metadata"}:
        return True
    return False


def _title_case(value: str) -> str:
    words = value.split()
    return " ".join(word.capitalize() if not word.isupper() else word for word in words)


def _urls_match(left: str | None, right: str | None) -> bool:
    if not left or not right:
        return False
    return left.strip().rstrip("/") == right.strip().rstrip("/")


def _same_host(left: str | None, right: str | None) -> bool:
    if not left or not right:
        return False
    return urlparse(left).netloc.replace("www.", "") == urlparse(right).netloc.replace("www.", "")


def _select_explicit_reference_urls(audit: ClaimAudit, reference_urls: list[str]) -> list[str]:
    if len(reference_urls) <= 2:
        return reference_urls
    ranked = sorted(
        reference_urls,
        key=lambda url: (_score_explicit_reference_url(audit, url), -reference_urls.index(url)),
        reverse=True,
    )
    selected: list[str] = []
    for url in ranked:
        if url in selected:
            continue
        selected.append(url)
        if len(selected) == 2:
            break
    return selected or reference_urls[:2]


def _score_explicit_reference_url(audit: ClaimAudit, url: str) -> int:
    normalized_url = (url or "").lower()
    claim_text = audit.claim.claim.lower()
    score = 0
    if "model-card" in normalized_url or "model-cards" in normalized_url:
        score += 3
    if "evals-methodology" in normalized_url:
        score += 2
    if "pricing" in normalized_url:
        score += 1
    if audit.claim.claim_type.value == "benchmark":
        if any(token in normalized_url for token in ("model-card", "model-cards", "evals-methodology", "mcp_atlas", "gdpval", "charxiv")):
            score += 5
    if audit.claim.claim_type.value == "numeric":
        if any(token in normalized_url for token in ("artificialanalysis", "pricing", "models", "gemini-3-5/")):
            score += 5
    if audit.claim.claim_type.value == "safety":
        if any(token in normalized_url for token in ("model-card", "model-cards", "gemini-3-5/")):
            score += 5
    if audit.claim.claim_type.value == "deployment":
        if any(token in normalized_url for token in ("gemini-3-5/", "model-card", "model-cards", "mcp_atlas", "models")):
            score += 5
    if any(token in claim_text for token in ("cost", "pricing", "half the cost")):
        if "pricing" in normalized_url:
            score += 8
    if any(token in claim_text for token in ("faster", "tokens per second", "latency")):
        if any(token in normalized_url for token in ("artificialanalysis", "gemini-3-5/", "models")):
            score += 8
    if any(token in claim_text for token in ("reliably", "multi-step workflows", "agentic")):
        if any(token in normalized_url for token in ("mcp_atlas", "model-card", "model-cards", "evals-methodology")):
            score += 8
    if any(token in claim_text for token in ("cyber", "cbrn", "harmful content", "refuse")):
        if any(token in normalized_url for token in ("model-card", "model-cards", "gemini-3-5/")):
            score += 8
    if any(token in claim_text for token in ("macquarie", "xero", "shopify", "databricks", "salesforce")):
        if any(token in normalized_url for token in ("gemini-3-5/", "model-card", "model-cards")):
            score += 8
    return score
