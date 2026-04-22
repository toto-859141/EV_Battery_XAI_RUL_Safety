"""Evaluation utilities for Remaining Useful Life prediction.

This module provides a small, reusable evaluation layer for RUL regression.
The design emphasizes:

- explicit metric computation;
- structured return values for experiment tracking;
- markdown-ready summaries for later report generation.

Dataset- or experiment-specific logic, such as life-stage grouping, should be
added by extending the helper functions below.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass

import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


@dataclass(frozen=True)
class RULEvaluationResult:
    """Structured result for RUL regression evaluation."""

    model_name: str
    mae: float
    rmse: float
    r2: float
    n_samples: int
    notes: tuple[str, ...] = ()


def evaluate_rul_predictions(
    y_true: pd.Series,
    y_pred: pd.Series,
    model_name: str = "unnamed_model",
    notes: tuple[str, ...] = (),
) -> RULEvaluationResult:
    """Evaluate continuous RUL predictions.

    Parameters
    ----------
    y_true:
        Ground-truth RUL values.
    y_pred:
        Predicted RUL values aligned to ``y_true``.
    model_name:
        Name used in reports and result tables.
    notes:
        Optional evaluation notes for reproducibility.
    """
    mse = mean_squared_error(y_true, y_pred)
    return RULEvaluationResult(
        model_name=model_name,
        mae=mean_absolute_error(y_true, y_pred),
        rmse=mse**0.5,
        r2=r2_score(y_true, y_pred),
        n_samples=len(y_true),
        notes=notes,
    )


def evaluation_to_frame(result: RULEvaluationResult) -> pd.DataFrame:
    """Convert a structured evaluation result to a one-row DataFrame."""
    row = asdict(result)
    row["notes"] = " | ".join(result.notes)
    return pd.DataFrame([row])


def to_markdown_summary(result: RULEvaluationResult) -> str:
    """Render a short markdown summary suitable for reports."""
    lines = [
        f"### RUL Evaluation: {result.model_name}",
        "",
        f"- MAE: `{result.mae:.4f}`",
        f"- RMSE: `{result.rmse:.4f}`",
        f"- R-squared: `{result.r2:.4f}`",
        f"- Number of samples: `{result.n_samples}`",
    ]
    if result.notes:
        lines.append("- Notes:")
        lines.extend([f"  - {note}" for note in result.notes])
    return "\n".join(lines) + "\n"


def placeholder_life_stage_analysis(frame: pd.DataFrame) -> pd.DataFrame:
    """Placeholder for life-stage-specific RUL error analysis.

    Extend this function once the project defines early-, mid-, and late-life
    segmentation rules for a chosen dataset.
    """
    return pd.DataFrame(
        {
            "life_stage": ["placeholder"],
            "metric_note": [
                "Add dataset-specific life-stage error analysis here."
            ],
        }
    )
