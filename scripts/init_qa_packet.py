from __future__ import annotations

import json
from pathlib import Path

import typer

from honestlaunch.research_qa import build_qa_packet


app = typer.Typer(help="Initialize a deep-research QA packet for one archive launch.")


@app.command()
def main(
    slug: str = typer.Argument(..., help="Archive slug, for example gemini-35-flash."),
    out: Path | None = typer.Option(
        None,
        "--out",
        help="Optional output path. Defaults to evaluations/packets/<slug>.json",
    ),
) -> None:
    packet = build_qa_packet(slug)
    output = out or Path("evaluations/packets") / f"{slug}.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    typer.echo(f"Wrote QA packet: {output}")


if __name__ == "__main__":
    app()
