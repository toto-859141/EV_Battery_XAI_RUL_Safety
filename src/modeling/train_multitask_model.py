"""Starter multi-task learning scaffold for RUL and safety prediction.

This module does not implement a final deep multi-task architecture yet.
Instead, it provides a clear experimental skeleton so the project can later
compare:
- separate single-task baselines;
- shared-input multi-task baselines;
- richer neural multi-task models.

The current implementation uses shared inputs with two simple estimators as
an academically transparent placeholder for future multi-task development.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, f1_score, mean_absolute_error
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


@dataclass(frozen=True)
class MultiTaskTrainingResult:
    """Minimal result structure for a shared-input multi-task experiment."""

    rul_mae: float
    safety_accuracy: float
    safety_f1_macro: float
    n_train: int
    n_test: int
    notes: tuple[str, ...]


def load_modeling_table(path: Path) -> pd.DataFrame:
    """Load a joint modeling table for multi-task experiments."""
    return pd.read_parquet(path)


def select_multitask_columns(
    frame: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.Series, pd.Series]:
    """Select shared inputs and both task labels."""
    required = {"target_rul", "target_safety_risk"}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(
            f"Missing required multitask columns: {sorted(missing)}. "
            "Construct both labels before training."
        )

    feature_columns = [
        column
        for column in frame.columns
        if column not in {"target_rul", "target_safety_risk", "target_eol"}
        and pd.api.types.is_numeric_dtype(frame[column])
    ]
    x = frame[feature_columns].fillna(0.0)
    y_rul = frame["target_rul"]
    y_safety = frame["target_safety_risk"]
    return x, y_rul, y_safety


def train_shared_input_multitask_baseline(
    frame: pd.DataFrame,
) -> MultiTaskTrainingResult:
    """Train a simple shared-input multi-task baseline.

    Placeholder:
    This is not yet a true shared-representation neural model. Instead, it
    keeps the same input matrix for both tasks so the research workflow can
    compare shared-input training with later multi-task architectures.
    """
    x, y_rul, y_safety = select_multitask_columns(frame)
    (
        x_train,
        x_test,
        y_rul_train,
        y_rul_test,
        y_safety_train,
        y_safety_test,
    ) = train_test_split(
        x,
        y_rul,
        y_safety,
        test_size=0.2,
        random_state=42,
    )

    rul_model = RandomForestRegressor(n_estimators=200, random_state=42)
    safety_model = RandomForestClassifier(n_estimators=200, random_state=42)

    rul_model.fit(x_train, y_rul_train)
    safety_model.fit(x_train, y_safety_train)

    rul_predictions = pd.Series(rul_model.predict(x_test), index=y_rul_test.index)
    safety_predictions = pd.Series(
        safety_model.predict(x_test), index=y_safety_test.index
    )

    notes = (
        "Used a shared input matrix with separate task heads as a starter.",
        "Replace this scaffold with a true shared-representation model later.",
    )

    return MultiTaskTrainingResult(
        rul_mae=mean_absolute_error(y_rul_test, rul_predictions),
        safety_accuracy=accuracy_score(y_safety_test, safety_predictions),
        safety_f1_macro=f1_score(
            y_safety_test,
            safety_predictions,
            average="macro",
        ),
        n_train=len(x_train),
        n_test=len(x_test),
        notes=notes,
    )
