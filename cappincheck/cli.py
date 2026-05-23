from __future__ import annotations

import asyncio
import os
from pathlib import Path
from time import perf_counter

import typer

from .audit import audit_claims
from .claims import extract_claims
from .ingest import load_document
from .report import write_html, write_json, write_markdown
from .schemas import AuditReport, ClaimAudit, RunTimingProfile


app = typer.Typer(help="Grounded claim audit for dense expert documents.")


@app.callback()
def main() -> None:
    """CappinCheck command line interface."""


@app.command()
def audit(
    source: str = typer.Argument(..., help="PDF path, markdown/text path, or URL."),
    out: Path = typer.Option(Path("cappincheck_report.md"), "--out", help="Markdown report path."),
    json_out: Path | None = typer.Option(None, "--json", help="Optional JSON report path."),
    html_out: Path | None = typer.Option(None, "--html", help="Optional static HTML dashboard path."),
    limit: int = typer.Option(5, "--limit", min=1, max=12, help="Number of claims to audit."),
    runtime: str = typer.Option("local", "--runtime", help="Runtime adapter: local or managed."),
    mock: bool = typer.Option(False, "--mock", help="Run deterministic no-key demo mode."),
    profile: bool = typer.Option(False, "--profile", help="Print run timing summary."),
    contrast: bool = typer.Option(False, "--contrast", help="Compare top claims against reference URLs."),
    reference: list[str] | None = typer.Option(
        None,
        "--reference",
        help="Reference URL for Evidence Contrast Mode. Repeat for multiple sources.",
    ),
    contrast_top: int = typer.Option(2, "--contrast-top", min=1, max=8, help="Number of claims to contrast."),
) -> None:
    """Audit risky factual claims in a dense document."""
    run_started_at = perf_counter()
    if runtime not in {"local", "managed"}:
        raise typer.BadParameter("--runtime must be local or managed")
    reference_urls = reference or []
    if contrast and not mock and not reference_urls:
        raise typer.BadParameter("--contrast requires at least one --reference URL unless --mock is used.")
    load_started_at = perf_counter()
    document = load_document(source)
    load_duration_ms = _elapsed_ms(load_started_at)
    typer.echo(f"Loaded: {document.title}")
    typer.echo("Extracting risky claims...")
    extract_started_at = perf_counter()
    try:
        claims = extract_claims(document, mock=mock, limit=max(limit, 8))
    except Exception as exc:
        _fail_with_context("claim extraction", exc)
    extract_duration_ms = _elapsed_ms(extract_started_at)
    typer.echo(f"Extracted {len(claims)} risky claims.")
    typer.echo(f"Auditing top {min(limit, len(claims))} claims...")
    audit_started_at = perf_counter()
    try:
        audits, audit_execution = asyncio.run(
            audit_claims(
                document,
                claims,
                mock=mock,
                limit=limit,
                runtime=runtime,
                contrast=contrast,
                reference_urls=reference_urls,
                contrast_top=contrast_top,
            )
        )
    except Exception as exc:
        _fail_with_context("claim audit", exc)
    audit_duration_ms = _elapsed_ms(audit_started_at)
    run_profile = RunTimingProfile(
        total_duration_ms=_elapsed_ms(run_started_at),
        load_document_ms=load_duration_ms,
        extract_claims_ms=extract_duration_ms,
        audit_claims_ms=audit_duration_ms,
        contrast_duration_ms=audit_execution.contrast_duration_ms,
        claims_extracted=len(claims),
        claims_audited=len(audits),
        agent_passes=audit_execution.agent_passes,
        contrast_claims=audit_execution.contrast_claims,
        unique_source_count=_unique_source_count(audits),
        claim_profiles=audit_execution.claim_profiles,
    )
    report = AuditReport(
        document=document,
        claims=claims,
        audits=audits,
        runtime=runtime,
        mode="deterministic_fallback" if mock else "live_gemini",
        model=None if mock else os.getenv("CLAIMLENS_MODEL", "gemini-3.5-flash"),
        contrast_enabled=contrast,
        reference_urls=reference_urls,
        run_profile=run_profile,
    )

    markdown_started_at = perf_counter()
    write_markdown(report, out)
    markdown_duration_ms = _elapsed_ms(markdown_started_at)
    typer.echo(
        f"Wrote markdown report: {out}"
        + (f" ({_format_ms(markdown_duration_ms)})" if profile else "")
    )
    if json_out:
        json_started_at = perf_counter()
        write_json(report, json_out)
        json_duration_ms = _elapsed_ms(json_started_at)
        typer.echo(
            f"Wrote JSON report: {json_out}"
            + (f" ({_format_ms(json_duration_ms)})" if profile else "")
        )
    if html_out:
        html_started_at = perf_counter()
        write_html(report, html_out)
        html_duration_ms = _elapsed_ms(html_started_at)
        typer.echo(
            f"Wrote HTML dashboard: {html_out}"
            + (f" ({_format_ms(html_duration_ms)})" if profile else "")
        )
    if profile:
        _print_profile(run_profile, audits)


def _fail_with_context(stage: str, exc: Exception) -> None:
    typer.secho(f"Failed during {stage}: {exc}", fg=typer.colors.RED, err=True)
    typer.echo(
        "Fallback: cappincheck audit examples/demo_document.md --mock "
        "--out examples/demo_report.md --json examples/demo_report.json "
        "--html examples/demo_report.html",
        err=True,
    )
    raise typer.Exit(1)


def _elapsed_ms(started_at: float) -> int:
    elapsed_ms = (perf_counter() - started_at) * 1000
    if elapsed_ms > 0:
        return max(1, int(elapsed_ms + 0.999))
    return 0


def _format_ms(duration_ms: int) -> str:
    if duration_ms >= 1000:
        return f"{duration_ms / 1000:.2f}s"
    return f"{duration_ms}ms"


def _print_profile(run_profile: RunTimingProfile, audits: list[ClaimAudit]) -> None:
    typer.echo("Timing profile:")
    typer.echo(
        "  "
        + " · ".join(
            [
                f"pipeline {_format_ms(run_profile.total_duration_ms)}",
                f"load {_format_ms(run_profile.load_document_ms)}",
                f"extract {_format_ms(run_profile.extract_claims_ms)}",
                f"audit {_format_ms(run_profile.audit_claims_ms)}",
                f"contrast {_format_ms(run_profile.contrast_duration_ms)}",
                f"{run_profile.claims_audited} claims",
                f"{run_profile.agent_passes} specialist passes",
                f"{run_profile.unique_source_count} unique sources",
            ]
        )
    )
    for audit in audits:
        timing = audit.claim_timing
        if timing is None:
            continue
        typer.echo(
            "  "
            + " · ".join(
                [
                    f"{audit.claim.id} {_format_ms(timing.total_duration_ms)}",
                    f"verifier {_format_ms(timing.verifier_ms)}",
                    f"contradiction {_format_ms(timing.contradiction_finder_ms)}",
                    f"numeric {_format_ms(timing.numeric_calibrator_ms)}",
                    f"aggregate {_format_ms(timing.aggregator_ms)}",
                    f"contrast {_format_ms(timing.contrast_ms)}",
                ]
            )
        )


def _unique_source_count(audits: list[ClaimAudit]) -> int:
    urls: set[str] = set()
    for audit in audits:
        for item in audit.supporting_evidence:
            if item.url:
                urls.add(item.url)
        for item in audit.counter_evidence:
            if item.url:
                urls.add(item.url)
        if audit.contrast:
            for item in audit.contrast.reference_sources:
                if item.url:
                    urls.add(item.url)
            for item in audit.contrast.best_sources:
                if item.url:
                    urls.add(item.url)
    return len(urls)


if __name__ == "__main__":
    app()
