"""Starter utilities for local explanation analysis.

This module is designed to support explanation of individual battery
observation windows. The structure is intentionally model-agnostic so it can
later be connected to:

- SHAP for tree-based models;
- gradient-based attribution for neural models;
- perturbation-based analysis for time-series models.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(frozen=True)
class LocalExplanation:
    """Represent one local prediction explanation."""

    observation_id: str
    local_table: pd.DataFrame
    notes: tuple[str, ...]


def build_local_explanation(
    observation_id: str,
    feature_row: pd.Series,
    attribution_row: pd.Series,
) -> LocalExplanation:
    """Create a ranked local explanation for one observation.

    Parameters
    ----------
    observation_id:
        Stable identifier for the explained observation window.
    feature_row:
        Observed feature values for the selected instance.
    attribution_row:
        Attribution values for the same instance.
    """
    common_features = feature_row.index.intersection(attribution_row.index)
    if len(common_features) == 0:
        raise ValueError("No overlapping features between data row and attribution row.")

    local_table = pd.DataFrame(
        {
            "feature_name": common_features,
            "feature_value": [feature_row[name] for name in common_features],
            "attribution": [attribution_row[name] for name in common_features],
        }
    )
    local_table["absolute_attribution"] = local_table["attribution"].abs()
    local_table = local_table.sort_values("absolute_attribution", ascending=False)

    notes = (
        "Created a ranked local explanation from supplied attribution values.",
        "Interpret local attributions as model-specific influence, not causality.",
        "Add instance-level plotting once the project plot standard is defined.",
    )
    return LocalExplanation(
        observation_id=observation_id,
        local_table=local_table,
        notes=notes,
    )


def save_local_explanation(explanation: LocalExplanation, output_path: Path) -> Path:
    """Save a local explanation table."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    explanation.local_table.to_csv(output_path, index=False)
    return output_path


def placeholder_local_plot(output_path: Path) -> Path:
    """Reserve a file path for a future local explanation plot."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        "Placeholder for local explanation plot output.\n",
        encoding="utf-8",
    )
    return output_path
