"""Starter uncertainty evaluation utilities.

This module provides simple placeholders for uncertainty summaries so the
project can later connect:

- predictive intervals for RUL;
- classification confidence or calibration for safety risk;
- ensemble disagreement analysis.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class UncertaintySummary:
    """Structured output for uncertainty analysis."""

    task_name: str
    summary_table: pd.DataFrame
    notes: tuple[str, ...]


def summarize_regression_uncertainty(
    frame: pd.DataFrame,
    prediction_column: str = "prediction_rul",
    lower_column: str = "prediction_rul_lower",
    upper_column: str = "prediction_rul_upper",
) -> UncertaintySummary:
    """Summarize interval-style uncertainty for RUL predictions.

    Placeholder:
    This function assumes lower and upper bounds already exist. Add
    model-specific interval generation later once the uncertainty method is
    finalized.
    """
    required = {prediction_column, lower_column, upper_column}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(
            "Missing regression uncertainty columns: "
            f"{sorted(missing)}"
        )

    widths = frame[upper_column] - frame[lower_column]
    summary = pd.DataFrame(
        [
            {
                "mean_interval_width": widths.mean(),
                "median_interval_width": widths.median(),
                "n_samples": len(frame),
            }
        ]
    )
    notes = (
        "Computed summary statistics for precomputed RUL prediction intervals.",
        "Add empirical coverage analysis once interval logic is available.",
    )
    return UncertaintySummary(task_name="rul", summary_table=summary, notes=notes)


def summarize_classification_uncertainty(
    frame: pd.DataFrame,
    confidence_column: str = "prediction_safety_confidence",
) -> UncertaintySummary:
    """Summarize confidence-style uncertainty for safety-risk predictions.

    Placeholder:
    Extend with calibration or reliability analysis once probabilistic outputs
    are available from the chosen classifier.
    """
    if confidence_column not in frame.columns:
        raise ValueError(
            f"Expected `{confidence_column}` in the input frame."
        )

    summary = pd.DataFrame(
        [
            {
                "mean_confidence": frame[confidence_column].mean(),
                "median_confidence": frame[confidence_column].median(),
                "min_confidence": frame[confidence_column].min(),
                "max_confidence": frame[confidence_column].max(),
                "n_samples": len(frame),
            }
        ]
    )
    notes = (
        "Computed basic confidence statistics for safety-risk predictions.",
        "Add calibration and reliability plots in a later project iteration.",
    )
    return UncertaintySummary(
        task_name="safety",
        summary_table=summary,
        notes=notes,
    )


def to_markdown_summary(summary: UncertaintySummary) -> str:
    """Render an uncertainty summary as markdown."""
    lines = [
        f"### Uncertainty Summary: {summary.task_name}",
        "",
        summary.summary_table.to_markdown(index=False),
    ]
    if summary.notes:
        lines.extend(["", "Notes:"])
        lines.extend([f"- {note}" for note in summary.notes])
    return "\n".join(lines) + "\n"
