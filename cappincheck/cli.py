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
    mock: bool = typer.Option(False, "--mock", help="Run deterministic no-key demo mode."),
) -> None:
    """Audit risky factual claims in a dense document."""
    document = load_document(source)
    typer.echo(f"Loaded: {document.title}")
    typer.echo("Extracting risky claims...")
    claims = extract_claims(document, mock=mock, limit=max(limit, 8))
    typer.echo(f"Extracted {len(claims)} risky claims.")
    typer.echo(f"Auditing top {min(limit, len(claims))} claims...")
    audits = asyncio.run(audit_claims(document, claims, mock=mock, limit=limit))
    report = AuditReport(document=document, claims=claims, audits=audits)

    write_markdown(report, out)
    typer.echo(f"Wrote markdown report: {out}")
    if json_out:
        write_json(report, json_out)
        typer.echo(f"Wrote JSON report: {json_out}")
    if html_out:
        write_html(report, html_out)
        typer.echo(f"Wrote HTML dashboard: {html_out}")


if __name__ == "__main__":
    app()
