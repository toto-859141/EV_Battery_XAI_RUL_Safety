"""Starter robustness evaluation utilities.

This module provides subgroup-based evaluation helpers so model performance
can be compared across operating conditions, degradation stages, or other
battery-specific regimes.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from src.evaluation.evaluate_rul import evaluate_rul_predictions
from src.evaluation.evaluate_safety_risk import evaluate_safety_predictions


@dataclass(frozen=True)
class RobustnessSliceResult:
    """Store one subgroup robustness result."""

    subgroup_name: str
    task_name: str
    metric_summary: dict[str, object]


def evaluate_rul_by_subgroup(
    frame: pd.DataFrame,
    subgroup_column: str,
    truth_column: str = "target_rul",
    prediction_column: str = "prediction_rul",
) -> pd.DataFrame:
    """Evaluate RUL performance across subgroup slices.

    Placeholder:
    The subgroup column should be created earlier in the workflow, for example
    from temperature regime, battery ID group, or degradation stage.
    """
    results: list[pd.DataFrame] = []
    for subgroup, subgroup_frame in frame.groupby(subgroup_column):
        result = evaluate_rul_predictions(
            subgroup_frame[truth_column],
            subgroup_frame[prediction_column],
            model_name=f"rul_{subgroup}",
            notes=(f"Subgroup evaluation for `{subgroup_column}={subgroup}`.",),
        )
        subgroup_result = pd.DataFrame(
            [
                {
                    "task_name": "rul",
                    "subgroup_name": subgroup,
                    **result.__dict__,
                }
            ]
        )
        subgroup_result["notes"] = " | ".join(result.notes)
        results.append(subgroup_result)
    return pd.concat(results, ignore_index=True) if results else pd.DataFrame()


def evaluate_safety_by_subgroup(
    frame: pd.DataFrame,
    subgroup_column: str,
    truth_column: str = "target_safety_risk",
    prediction_column: str = "prediction_safety_risk",
) -> pd.DataFrame:
    """Evaluate safety-risk classification across subgroup slices."""
    results: list[pd.DataFrame] = []
    for subgroup, subgroup_frame in frame.groupby(subgroup_column):
        result = evaluate_safety_predictions(
            subgroup_frame[truth_column],
            subgroup_frame[prediction_column],
            model_name=f"safety_{subgroup}",
            notes=(f"Subgroup evaluation for `{subgroup_column}={subgroup}`.",),
        )
        subgroup_result = pd.DataFrame(
            [
                {
                    "task_name": "safety",
                    "subgroup_name": subgroup,
                    **result.__dict__,
                }
            ]
        )
        subgroup_result["notes"] = " | ".join(result.notes)
        results.append(subgroup_result)
    return pd.concat(results, ignore_index=True) if results else pd.DataFrame()


def to_markdown_summary(frame: pd.DataFrame) -> str:
    """Render robustness results as a markdown table."""
    if frame.empty:
        return "No robustness results available.\n"
    columns = [col for col in frame.columns if col != "notes"]
    return frame[columns].to_markdown(index=False) + "\n"
