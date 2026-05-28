from __future__ import annotations

from pathlib import Path

from honestlaunch.anchor_map import enrich_report_for_launch_page
from honestlaunch.archive_quality import hydrate_report_document, load_report, refresh_archive_metadata
from honestlaunch.archive_registry import archive_entries, publication_info_for_report
from honestlaunch.report import write_html, write_json


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    rebuilt = 0
    refresh_archive_metadata(ROOT)
    for entry in archive_entries():
        json_path = ROOT / "examples" / str(entry.get("artifactJson", ""))
        html_path = ROOT / "examples" / str(entry.get("artifactHtml", ""))
        if not json_path.exists() or not html_path.name:
            continue
        report = load_report(json_path)
        report = hydrate_report_document(report)
        if not report.reference_urls and entry.get("referenceUrls"):
            report.reference_urls = list(entry.get("referenceUrls", []))
        report = enrich_report_for_launch_page(report)
        report.publication = publication_info_for_report(report)
        write_json(report, json_path)
        write_html(report, html_path)
        rebuilt += 1
        print(f"rebuilt {html_path.relative_to(ROOT)}")
    print(f"rebuilt {rebuilt} archive html files")


if __name__ == "__main__":
    main()
