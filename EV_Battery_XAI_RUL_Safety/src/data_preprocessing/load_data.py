"""Utilities for loading raw EV battery monitoring data.

This module provides a dataset-agnostic entry point for reading raw files
into pandas DataFrames. The implementation is intentionally conservative:
it standardizes only basic file loading behavior and leaves dataset-specific
schema interpretation to project-level preprocessing code.

For academic reproducibility, each loader function is structured so that:
- input paths are explicit;
- assumptions are localized;
- the returned data can be traced to raw source files.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


SUPPORTED_SUFFIXES = {".csv", ".parquet"}


@dataclass(frozen=True)
class LoadedDataset:
    """Container for a loaded raw dataset and basic provenance metadata."""

    name: str
    path: Path
    frame: pd.DataFrame


def infer_dataset_name(path: Path) -> str:
    """Infer a simple dataset name from a file path."""
    return path.stem.lower().replace(" ", "_")


def load_file(path: Path, **read_kwargs: object) -> pd.DataFrame:
    """Load a single raw file into a DataFrame.

    Dataset-specific column parsing should be added by extending this
    function or by applying a follow-up normalization step.
    """
    suffix = path.suffix.lower()
    if suffix not in SUPPORTED_SUFFIXES:
        raise ValueError(
            f"Unsupported file type: {suffix}. "
            f"Supported types are: {sorted(SUPPORTED_SUFFIXES)}"
        )

    if suffix == ".csv":
        return pd.read_csv(path, **read_kwargs)
    if suffix == ".parquet":
        return pd.read_parquet(path, **read_kwargs)

    raise ValueError(f"Unhandled file type: {suffix}")


def load_dataset(path: Path, name: str | None = None) -> LoadedDataset:
    """Load one dataset file and attach minimal provenance metadata."""
    frame = load_file(path)
    dataset_name = name or infer_dataset_name(path)
    return LoadedDataset(name=dataset_name, path=path, frame=frame)


def discover_data_files(raw_dir: Path) -> list[Path]:
    """Return supported raw data files under a directory."""
    if not raw_dir.exists():
        raise FileNotFoundError(f"Raw data directory does not exist: {raw_dir}")

    files = [
        path
        for path in sorted(raw_dir.rglob("*"))
        if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES
    ]
    return files


def load_all_datasets(raw_dir: Path) -> list[LoadedDataset]:
    """Load all supported files from a raw data directory."""
    return [load_dataset(path) for path in discover_data_files(raw_dir)]
