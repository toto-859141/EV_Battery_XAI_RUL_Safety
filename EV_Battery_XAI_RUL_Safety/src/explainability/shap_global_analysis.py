"""Starter utilities for global SHAP-style analysis.

This module provides a lightweight scaffold for dataset-level explanation of
tree-based or other tabular models. The functions are intentionally generic so
they can later be connected to:

- tree-based estimators with TreeSHAP support;
- neural or hybrid models through alternative SHAP explainers;
- project-specific plotting and report-generation code.

The current implementation focuses on reproducible data structures rather than
on a fixed dependency on the `shap` package.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(frozen=True)
class GlobalExplanationSummary:
    """Container for global feature-attribution outputs."""

    summary_table: pd.DataFrame
    notes: tuple[str, ...]


def summarize_attributions(
    feature_names: list[str],
    attributions: pd.DataFrame,
) -> GlobalExplanationSummary:
    """Create a global feature-importance summary from attribution values.

    Parameters
    ----------
    feature_names:
        Ordered list of feature names corresponding to the attribution matrix.
    attributions:
        DataFrame of attribution values with one row per observation and one
        column per feature.

    Notes
    -----
    This function assumes attributions have already been produced by an
    explainer. Dataset- and model-specific SHAP computation should be added
    later in a wrapper function once the project selects exact libraries.
    """
    missing = set(feature_names).difference(attributions.columns)
    if missing:
        raise ValueError(
            "Attribution matrix does not contain all requested features: "
            f"{sorted(missing)}"
        )

    summary = pd.DataFrame(
        {
            "feature_name": feature_names,
            "mean_absolute_attribution": [
                attributions[name].abs().mean() for name in feature_names
            ],
            "mean_signed_attribution": [
                attributions[name].mean() for name in feature_names
            ],
        }
    ).sort_values("mean_absolute_attribution", ascending=False)

    notes = (
        "Computed global explanation summary from precomputed attribution values.",
        "This summary is compatible with SHAP-like additive explanation methods.",
        "Add model-specific explainer construction in a project extension layer.",
    )
    return GlobalExplanationSummary(summary_table=summary, notes=notes)


def save_global_summary(summary: GlobalExplanationSummary, output_path: Path) -> Path:
    """Save the global explanation summary for downstream reporting."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    summary.summary_table.to_csv(output_path, index=False)
    return output_path


def placeholder_global_plot(output_path: Path) -> Path:
    """Reserve a file path for a future global explanation plot.

    Placeholder:
    Replace this function with SHAP summary plotting or an equivalent plotting
    routine once the visualization stack is finalized.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        "Placeholder for global explanation plot output.\n",
        encoding="utf-8",
    )
    return output_path
