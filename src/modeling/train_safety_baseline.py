"""Train baseline models for battery safety risk prediction.

This module mirrors the RUL baseline structure so both prediction tasks
can be extended and compared consistently. The current implementation
assumes that a safety label is already available in the feature table.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


@dataclass(frozen=True)
class SafetyTrainingResult:
    """Structured baseline classification result."""

    model_name: str
    accuracy: float
    f1_macro: float
    n_train: int
    n_test: int


def load_modeling_table(path: Path) -> pd.DataFrame:
    """Load a feature table for safety modeling."""
    return pd.read_parquet(path)


def select_safety_columns(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Select features and the safety-risk target."""
    if "target_safety_risk" not in frame.columns:
        raise ValueError(
            "Expected `target_safety_risk` in the modeling table. "
            "Add safety-label logic before training."
        )

    excluded = {"target_rul", "target_safety_risk", "target_eol"}
    feature_columns = [
        column
        for column in frame.columns
        if column not in excluded and pd.api.types.is_numeric_dtype(frame[column])
    ]
    x = frame[feature_columns].fillna(0.0)
    y = frame["target_safety_risk"]
    return x, y


def train_safety_baselines(frame: pd.DataFrame) -> list[SafetyTrainingResult]:
    """Train simple baseline classifiers for safety risk prediction."""
    x, y = select_safety_columns(frame)
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y if y.nunique() > 1 else None,
    )

    models = {
        "logistic_regression": LogisticRegression(max_iter=1000),
        "random_forest_classifier": RandomForestClassifier(
            n_estimators=200,
            random_state=42,
        ),
    }

    results: list[SafetyTrainingResult] = []
    for name, model in models.items():
        model.fit(x_train, y_train)
        predictions = pd.Series(model.predict(x_test), index=y_test.index)
        results.append(
            SafetyTrainingResult(
                model_name=name,
                accuracy=accuracy_score(y_test, predictions),
                f1_macro=f1_score(y_test, predictions, average="macro"),
                n_train=len(x_train),
                n_test=len(x_test),
            )
        )
    return results
