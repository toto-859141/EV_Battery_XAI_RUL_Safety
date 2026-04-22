# Result Table Template: RUL Prediction

## Purpose

This table is intended for publication-friendly reporting of Remaining Useful Life prediction results.

## Table

| Model | Input Representation | Feature Set | MAE | RMSE | R-squared | Late-Life Error Note | Interpretability Level | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline model | Engineered features | Baseline feature set | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[High / Moderate / Low]` | `[Insert]` |
| Model A | Engineered features | Full feature set | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` |
| Model B | Sequence only | Raw time-series window | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` |
| Model C | Hybrid | Sequence + engineered features | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` |

## Interpretation Notes

- Lower `MAE` and `RMSE` indicate better average RUL prediction accuracy.
- `R-squared` should be interpreted as a secondary descriptive metric rather than the sole basis for model selection.
- `Late-Life Error Note` should summarize whether the model remains reliable near end-of-life, where large errors may be operationally more problematic.
- `Interpretability Level` should reflect how easily the model’s RUL predictions can be explained using the project’s XAI framework.
- A model with slightly weaker aggregate performance may still be preferable if it offers materially better interpretability and more stable late-life behavior.
