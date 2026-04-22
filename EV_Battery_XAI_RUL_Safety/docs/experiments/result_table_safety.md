# Result Table Template: Safety Risk Prediction

## Purpose

This table is intended for publication-friendly reporting of safety risk classification results.

## Table

| Model | Input Representation | Feature Set | F1-score | High-Risk Recall | High-Risk Precision | AUPRC / AUROC | False Negative Note | False Positive Note | Interpretability Level | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline model | Engineered features | Baseline feature set | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[High / Moderate / Low]` | `[Insert]` |
| Model A | Engineered features | Full feature set | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` |
| Model B | Sequence only | Raw time-series window | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` |
| Model C | Hybrid | Sequence + engineered features | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` |

## Interpretation Notes

- `High-Risk Recall` is especially important in safety-critical monitoring because low recall means elevated-risk cases may be missed.
- `High-Risk Precision` should be considered together with recall to understand the false-alarm trade-off.
- `AUPRC` is generally preferable to `AUROC` when the high-risk class is rare; if both are reported, make clear which metric is emphasized.
- `False Negative Note` should summarize the safety relevance of missed high-risk cases.
- `False Positive Note` should summarize the operational burden of unnecessary alerts.
- The preferred safety model should not be chosen on overall accuracy alone.
