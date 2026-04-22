"""Utilities for aggregating and comparing feature importance results.

This module is intended to support the comparison of:

- built-in model feature importance;
- permutation importance;
- SHAP-style global summaries;
- cross-task importance patterns for RUL and safety risk prediction.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(frozen=True)
class ImportanceSummary:
    """Store an importance ranking and related metadata."""

    importance_table: pd.DataFrame
    notes: tuple[str, ...]


def build_importance_summary(
    feature_names: list[str],
    importance_values: list[float],
    source_name: str,
) -> ImportanceSummary:
    """Create a normalized importance summary table."""
    if len(feature_names) != len(importance_values):
        raise ValueError("Feature names and importance values must have equal length.")

    table = pd.DataFrame(
        {
            "feature_name": feature_names,
            "importance_value": importance_values,
            "importance_source": source_name,
        }
    )
    total = table["importance_value"].abs().sum()
    table["normalized_importance"] = (
        table["importance_value"].abs() / total if total else 0.0
    )
    table = table.sort_values("normalized_importance", ascending=False)

    notes = (
        f"Built importance summary from source: {source_name}.",
        "Normalized importance values for easier comparison across methods.",
        "Use caution when comparing methods with different attribution semantics.",
    )
    return ImportanceSummary(importance_table=table, notes=notes)


def compare_importance_tables(
    left: pd.DataFrame,
    right: pd.DataFrame,
    left_label: str,
    right_label: str,
) -> pd.DataFrame:
    """Compare two importance tables by feature name.

    This is useful for:
    - comparing RUL and safety explanations;
    - comparing baseline and advanced models;
    - comparing SHAP and permutation importance outputs.
    """
    merged = left[["feature_name", "normalized_importance"]].rename(
        columns={"normalized_importance": f"{left_label}_importance"}
    ).merge(
        right[["feature_name", "normalized_importance"]].rename(
            columns={"normalized_importance": f"{right_label}_importance"}
        ),
        on="feature_name",
        how="outer",
    )
    return merged.fillna(0.0)


def save_importance_summary(summary: ImportanceSummary, output_path: Path) -> Path:
    """Save an importance summary table."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    summary.importance_table.to_csv(output_path, index=False)
    return output_path
