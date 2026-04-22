"""Train baseline models for Remaining Useful Life prediction.

This starter module is designed for academically reproducible experiments:
- feature loading is explicit;
- train/validation splits are centralized;
- metrics are returned in structured form;
- dataset-specific label construction is intentionally left as a placeholder.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


@dataclass(frozen=True)
class RULTrainingResult:
    """Store model metrics for transparent experiment reporting."""

    model_name: str
    mae: float
    rmse: float
    n_train: int
    n_test: int


def load_modeling_table(path: Path) -> pd.DataFrame:
    """Load a feature table for RUL modeling."""
    return pd.read_parquet(path)


def select_rul_columns(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Select features and the RUL target.

    Placeholder:
    This function assumes that a `target_rul` column already exists in the
    modeling table. Update this logic once label construction is finalized.
    """
    if "target_rul" not in frame.columns:
        raise ValueError(
            "Expected `target_rul` in the modeling table. "
            "Add target-construction logic before training."
        )

    excluded = {"target_rul", "target_safety_risk", "target_eol"}
    feature_columns = [
        column
        for column in frame.columns
        if column not in excluded and pd.api.types.is_numeric_dtype(frame[column])
    ]
    x = frame[feature_columns].fillna(0.0)
    y = frame["target_rul"]
    return x, y


def evaluate_regressor(model_name: str, y_true: pd.Series, y_pred: pd.Series) -> RULTrainingResult:
    """Compute the baseline regression metrics used in the project."""
    mse = mean_squared_error(y_true, y_pred)
    return RULTrainingResult(
        model_name=model_name,
        mae=mean_absolute_error(y_true, y_pred),
        rmse=mse**0.5,
        n_train=0,
        n_test=len(y_true),
    )


def train_rul_baselines(frame: pd.DataFrame) -> list[RULTrainingResult]:
    """Train simple starter baselines for RUL regression."""
    x, y = select_rul_columns(frame)
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    models = {
        "ridge_regression": Ridge(),
        "random_forest_regressor": RandomForestRegressor(
            n_estimators=200,
            random_state=42,
        ),
    }

    results: list[RULTrainingResult] = []
    for name, model in models.items():
        model.fit(x_train, y_train)
        predictions = pd.Series(model.predict(x_test), index=y_test.index)
        result = evaluate_regressor(name, y_test, predictions)
        results.append(
            RULTrainingResult(
                model_name=result.model_name,
                mae=result.mae,
                rmse=result.rmse,
                n_train=len(x_train),
                n_test=len(x_test),
            )
        )
    return results
