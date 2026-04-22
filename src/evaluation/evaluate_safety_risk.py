"""Evaluation utilities for safety risk classification.

This module computes core classification metrics and preserves explicit support
for safety-relevant error interpretation, especially false negatives and false
positives in elevated-risk classes.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass

import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)


@dataclass(frozen=True)
class SafetyEvaluationResult:
    """Structured classification result for safety-risk evaluation."""

    model_name: str
    accuracy: float
    f1_macro: float
    precision_macro: float
    recall_macro: float
    n_samples: int
    notes: tuple[str, ...] = ()


def evaluate_safety_predictions(
    y_true: pd.Series,
    y_pred: pd.Series,
    model_name: str = "unnamed_model",
    notes: tuple[str, ...] = (),
) -> SafetyEvaluationResult:
    """Evaluate safety-risk predictions with general multi-class metrics."""
    return SafetyEvaluationResult(
        model_name=model_name,
        accuracy=accuracy_score(y_true, y_pred),
        f1_macro=f1_score(y_true, y_pred, average="macro"),
        precision_macro=precision_score(
            y_true,
            y_pred,
            average="macro",
            zero_division=0,
        ),
        recall_macro=recall_score(
            y_true,
            y_pred,
            average="macro",
            zero_division=0,
        ),
        n_samples=len(y_true),
        notes=notes,
    )


def build_confusion_matrix_frame(
    y_true: pd.Series,
    y_pred: pd.Series,
) -> pd.DataFrame:
    """Return a labeled confusion matrix as a DataFrame."""
    labels = sorted(pd.Index(y_true).append(pd.Index(y_pred)).unique())
    matrix = confusion_matrix(y_true, y_pred, labels=labels)
    index = [f"true_{label}" for label in labels]
    columns = [f"pred_{label}" for label in labels]
    return pd.DataFrame(matrix, index=index, columns=columns)


def evaluation_to_frame(result: SafetyEvaluationResult) -> pd.DataFrame:
    """Convert a safety evaluation result to a one-row DataFrame."""
    row = asdict(result)
    row["notes"] = " | ".join(result.notes)
    return pd.DataFrame([row])


def to_markdown_summary(result: SafetyEvaluationResult) -> str:
    """Render a short markdown summary suitable for experiment reports."""
    lines = [
        f"### Safety Evaluation: {result.model_name}",
        "",
        f"- Accuracy: `{result.accuracy:.4f}`",
        f"- Macro F1-score: `{result.f1_macro:.4f}`",
        f"- Macro precision: `{result.precision_macro:.4f}`",
        f"- Macro recall: `{result.recall_macro:.4f}`",
        f"- Number of samples: `{result.n_samples}`",
    ]
    if result.notes:
        lines.append("- Notes:")
        lines.extend([f"  - {note}" for note in result.notes])
    return "\n".join(lines) + "\n"


def placeholder_high_risk_error_review(frame: pd.DataFrame) -> pd.DataFrame:
    """Placeholder for high-risk false-negative and false-positive review.

    Extend this function after the project fixes the exact encoding of the
    high-risk class and its decision-support consequences.
    """
    return pd.DataFrame(
        {
            "error_type": ["placeholder"],
            "note": ["Add safety-critical FN/FP subgroup analysis here."],
        }
    )
