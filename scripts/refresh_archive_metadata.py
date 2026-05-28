from __future__ import annotations

from pathlib import Path

from honestlaunch.archive_quality import refresh_archive_metadata


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    manifest = refresh_archive_metadata(ROOT)
    featured = manifest.get("site", {}).get("metrics", {}).get("featuredCount", 0)
    print(f"refreshed archive manifest and evidence packets for {featured} featured pages")


if __name__ == "__main__":
    main()
