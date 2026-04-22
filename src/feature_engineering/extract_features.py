"""Starter feature extraction for EV battery monitoring data.

The functions in this module produce interpretable, window-level features
from preprocessed battery records. The current implementation focuses on
simple descriptive features so the project has a reproducible baseline
before dataset-specific feature formulas are finalized.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


@dataclass(frozen=True)
class FeatureExtractionResult:
    """Feature table and extraction notes for reproducibility."""

    features: pd.DataFrame
    notes: tuple[str, ...]


def _group_keys(frame: pd.DataFrame) -> list[str]:
    """Choose grouping keys that approximate an observation window."""
    candidate_keys = ["battery_id", "cycle_index", "window_id"]
    return [key for key in candidate_keys if key in frame.columns]


def _safe_aggregate(frame: pd.DataFrame, column: str) -> dict[str, pd.Series]:
    """Build a minimal aggregation dictionary for a numeric column."""
    return {
        f"{column}_mean": frame.groupby(_group_keys(frame))[column].mean(),
        f"{column}_min": frame.groupby(_group_keys(frame))[column].min(),
        f"{column}_max": frame.groupby(_group_keys(frame))[column].max(),
        f"{column}_std": frame.groupby(_group_keys(frame))[column].std(),
    }


def extract_baseline_features(frame: pd.DataFrame) -> FeatureExtractionResult:
    """Extract a small, interpretable baseline feature set.

    The grouping logic is intentionally simple and should be replaced or
    extended once a formal observation-window definition is fixed.
    """
    keys = _group_keys(frame)
    if not keys:
        raise ValueError(
            "No grouping keys found. Expected at least one of: "
            "`battery_id`, `cycle_index`, or `window_id`."
        )

    grouped = frame.groupby(keys, dropna=False)
    features = grouped.size().rename("row_count").reset_index()
    notes = [
        f"Grouped records using keys: {keys}.",
        "Extracted simple descriptive features as an initial baseline.",
    ]

    for column in ["voltage", "current", "temperature"]:
        if column in frame.columns:
            stats = grouped[column].agg(["mean", "min", "max", "std"]).reset_index()
            stats = stats.rename(
                columns={
                    "mean": f"{column}_mean",
                    "min": f"{column}_min",
                    "max": f"{column}_max",
                    "std": f"{column}_std",
                }
            )
            features = features.merge(stats, on=keys, how="left")

    if "timestamp" in frame.columns:
        duration = grouped["timestamp"].agg(["min", "max"]).reset_index()
        duration["window_duration_seconds"] = (
            duration["max"] - duration["min"]
        ).dt.total_seconds()
        features = features.merge(
            duration[keys + ["window_duration_seconds"]],
            on=keys,
            how="left",
        )
        notes.append("Computed window duration from the timestamp range.")

    # Placeholder: add degradation indicators, safety indicators,
    # and dataset-specific engineered variables here.
    notes.append(
        "Dataset-specific degradation, safety, and operational features "
        "remain to be added."
    )

    return FeatureExtractionResult(features=features, notes=tuple(notes))


def load_preprocessed_frame(path: Path) -> pd.DataFrame:
    """Load a preprocessed battery table."""
    return pd.read_parquet(path)


def save_feature_table(features: pd.DataFrame, output_path: Path) -> Path:
    """Save extracted features to parquet."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    features.to_parquet(output_path, index=False)
    return output_path
