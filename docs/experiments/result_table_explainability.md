# Result Table Template: Explainability Analysis

## Purpose

This table is intended for publication-friendly reporting of explainability results across model families and tasks.

## Table

| Model | Task | Explanation Method | Global Explanation Available | Local Explanation Available | Dominant Feature Groups | Explanation Stability | Safety-Relevant Interpretability | Main Limitation | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model A | RUL | `[Insert]` | `[Yes / No]` | `[Yes / No]` | `[Electrical / Thermal / Degradation / Usage]` | `[High / Moderate / Low]` | `[High / Moderate / Low]` | `[Insert]` | `[Insert]` |
| Model B | Safety | `[Insert]` | `[Yes / No]` | `[Yes / No]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` |
| Model C | Multitask | `[Insert]` | `[Yes / No]` | `[Yes / No]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` |

## Interpretation Notes

- `Global Explanation Available` indicates whether the model supports dataset-level interpretation of dominant predictors.
- `Local Explanation Available` indicates whether individual high-risk or low-RUL cases can be explained in a case-specific way.
- `Dominant Feature Groups` should summarize the main explanatory domains rather than list every variable.
- `Explanation Stability` should reflect whether explanation patterns remain consistent across validation splits, repeated runs, or comparable cases.
- `Safety-Relevant Interpretability` should capture whether the explanation is sufficiently clear and plausible for safety-oriented interpretation, not merely whether an attribution method exists.
- Models with high predictive performance but weak explanation stability should be interpreted cautiously in a safety-critical context.
