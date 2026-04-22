# Result Table Template: Robustness Analysis

## Purpose

This table is intended for publication-friendly reporting of robustness results across operating conditions and battery regimes.

## Table

| Model | Task | Test Condition / Subgroup | Primary Metric | Secondary Metric | Performance Change vs Reference | Explanation Shift | Safety-Relevant Concern | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model A | RUL | Nominal condition | `[Insert]` | `[Insert]` | `[Reference]` | `[Insert]` | `[Low / Moderate / High]` | `[Insert]` |
| Model A | RUL | Elevated temperature | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` |
| Model B | Safety | High-rate charging | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` |
| Model B | Safety | Late-life windows | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` |
| Model C | Multitask | Unseen battery group | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` | `[Insert]` |

## Interpretation Notes

- `Test Condition / Subgroup` should refer to a clearly defined operating regime, degradation stage, or held-out battery subset.
- `Primary Metric` and `Secondary Metric` should match the task:
  - for RUL, typically `MAE` and `RMSE`;
  - for safety, typically `F1-score` and high-risk recall or AUPRC.
- `Performance Change vs Reference` should show whether the model deteriorates materially under the tested condition.
- `Explanation Shift` should summarize whether dominant explanatory patterns remain stable or change under the subgroup.
- `Safety-Relevant Concern` should reflect whether the robustness loss has practical implications, especially when false negatives or high-confidence errors increase under the tested condition.
- This table is most useful when paired with a short narrative explaining why the condition is important for battery monitoring.
