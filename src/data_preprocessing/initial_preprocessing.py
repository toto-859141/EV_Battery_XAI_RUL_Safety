"""Starter preprocessing script for EV battery datasets.

This module provides a small, dataset-agnostic baseline:
- scan the raw data directory
- collect basic file metadata
- write a dataset manifest into the processed directory

It is intentionally lightweight so the project has a runnable first step
before a specific dataset schema has been selected.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RAW_DIR = PROJECT_ROOT / "data" / "raw"
DEFAULT_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
DEFAULT_MANIFEST_NAME = "dataset_manifest.csv"


@dataclass(frozen=True)
class FileRecord:
    """Basic metadata for a discovered raw data file."""

    relative_path: str
    suffix: str
    size_bytes: int


def collect_file_records(raw_dir: Path) -> list[FileRecord]:
    """Recursively collect metadata for files under the raw data directory."""
    if not raw_dir.exists():
        raise FileNotFoundError(f"Raw data directory does not exist: {raw_dir}")

    records: list[FileRecord] = []
    for path in sorted(raw_dir.rglob("*")):
        if path.is_file() and not path.name.startswith("."):
            records.append(
                FileRecord(
                    relative_path=str(path.relative_to(raw_dir)),
                    suffix=path.suffix.lower(),
                    size_bytes=path.stat().st_size,
                )
            )
    return records


def write_manifest(records: list[FileRecord], output_path: Path) -> None:
    """Write the discovered file metadata to a CSV manifest."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["relative_path", "suffix", "size_bytes"],
        )
        writer.writeheader()
        for record in records:
            writer.writerow(
                {
                    "relative_path": record.relative_path,
                    "suffix": record.suffix,
                    "size_bytes": record.size_bytes,
                }
            )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a simple manifest for files stored in data/raw."
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=DEFAULT_RAW_DIR,
        help="Directory containing raw dataset files.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_PROCESSED_DIR / DEFAULT_MANIFEST_NAME,
        help="CSV output path for the generated manifest.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    records = collect_file_records(args.raw_dir)
    write_manifest(records, args.output)
    print(
        f"Wrote manifest with {len(records)} file(s) to "
        f"{args.output.resolve()}"
    )


if __name__ == "__main__":
    main()
