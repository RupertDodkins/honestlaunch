from __future__ import annotations

import asyncio
from pathlib import Path

import typer

from .audit import audit_claims
from .claims import extract_claims
from .ingest import load_document
from .report import write_html, write_json, write_markdown
from .schemas import AuditReport


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
    contrast: bool = typer.Option(False, "--contrast", help="Compare top claims against reference URLs."),
    reference: list[str] | None = typer.Option(
        None,
        "--reference",
        help="Reference URL for Evidence Contrast Mode. Repeat for multiple sources.",
    ),
    contrast_top: int = typer.Option(2, "--contrast-top", min=1, max=8, help="Number of claims to contrast."),
) -> None:
    """Audit risky factual claims in a dense document."""
    if runtime not in {"local", "managed"}:
        raise typer.BadParameter("--runtime must be local or managed")
    reference_urls = reference or []
    if contrast and not mock and not reference_urls:
        raise typer.BadParameter("--contrast requires at least one --reference URL unless --mock is used.")
    document = load_document(source)
    typer.echo(f"Loaded: {document.title}")
    typer.echo("Extracting risky claims...")
    try:
        claims = extract_claims(document, mock=mock, limit=max(limit, 8))
    except Exception as exc:
        _fail_with_context("claim extraction", exc)
    typer.echo(f"Extracted {len(claims)} risky claims.")
    typer.echo(f"Auditing top {min(limit, len(claims))} claims...")
    try:
        audits = asyncio.run(
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
    report = AuditReport(document=document, claims=claims, audits=audits)

    write_markdown(report, out)
    typer.echo(f"Wrote markdown report: {out}")
    if json_out:
        write_json(report, json_out)
        typer.echo(f"Wrote JSON report: {json_out}")
    if html_out:
        write_html(report, html_out)
        typer.echo(f"Wrote HTML dashboard: {html_out}")


def _fail_with_context(stage: str, exc: Exception) -> None:
    typer.secho(f"Failed during {stage}: {exc}", fg=typer.colors.RED, err=True)
    typer.echo(
        "Fallback: cappincheck audit examples/demo_document.md --mock "
        "--out examples/demo_report.md --json examples/demo_report.json "
        "--html examples/demo_report.html",
        err=True,
    )
    raise typer.Exit(1)


if __name__ == "__main__":
    app()
