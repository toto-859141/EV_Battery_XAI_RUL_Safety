# Error Analysis Template

## Purpose

This template is designed to support structured academic reporting of model errors for:

- `target_rul`;
- `target_safety_risk`.

The purpose of the template is to move beyond aggregate metrics and identify where model failures occur, why they may occur, and what they imply for battery monitoring and safety-relevant interpretation.

## Instructions for Use

Use this template after primary evaluation metrics have been computed. The analysis should be completed separately for:

- RUL models;
- safety-risk models;
- multi-task models where applicable.

## Section 1: Experiment Metadata

| Field | Entry |
| --- | --- |
| Experiment ID | `[Insert experiment ID]` |
| Task | `[RUL / Safety / Multi-task]` |
| Model | `[Insert model name]` |
| Dataset version | `[Insert dataset version]` |
| Feature set version | `[Insert feature set version]` |
| Split strategy | `[Insert split description]` |

## Section 2: Aggregate Error Summary

### For RUL

| Metric | Value |
| --- | --- |
| MAE | `[Insert value]` |
| RMSE | `[Insert value]` |
| R-squared | `[Insert value]` |
| Late-life error summary | `[Insert note]` |

### For Safety Risk

| Metric | Value |
| --- | --- |
| F1-score | `[Insert value]` |
| High-risk recall | `[Insert value]` |
| High-risk precision | `[Insert value]` |
| AUPRC or AUROC | `[Insert value]` |

## Section 3: Error Pattern Analysis

### 3.1 Where Do the Largest Errors Occur?

Prompts:

- Are large RUL errors concentrated in early life, mid life, or late life?
- Are safety misclassifications concentrated in specific operating regimes?
- Do errors cluster around temperature excursions, high-rate charging, or other stress patterns?

Entry:

`[Insert structured narrative.]`

### 3.2 Are Errors Systematic or Random?

Prompts:

- Does the model systematically overestimate or underestimate RUL?
- Does the safety model systematically under-detect high-risk cases?
- Are false alarms concentrated in specific subgroups?

Entry:

`[Insert structured narrative.]`

## Section 4: Safety-Relevant Error Review

### 4.1 False Negatives

Definition:

- for safety models, cases where the model predicts low or moderate risk but the reference label is high risk.

Prompts:

- How many false negatives occurred?
- Under what operating conditions did they occur?
- What safety-relevant features were present in those cases?
- Would the explanation outputs have helped identify the miss?

Entry:

`[Insert structured narrative.]`

### 4.2 False Positives

Definition:

- for safety models, cases where the model predicts high risk but the reference label is lower risk.

Prompts:

- How many false positives occurred?
- Are they associated with legitimate abnormality that was not reflected in the label?
- Do they arise from noisy signals, proxy-label limitations, or threshold effects?

Entry:

`[Insert structured narrative.]`

### 4.3 Joint RUL and Safety Interpretation Errors

Prompts:

- Are there cases with low predicted RUL but low safety risk?
- Are there cases with high safety risk but moderate or high RUL?
- What do such disagreements suggest about the model or labels?

Entry:

`[Insert structured narrative.]`

## Section 5: Case Review Table

| Case ID | True Outcome | Predicted Outcome | Error Type | Operating Context | Explanation Summary | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| `[Insert]` | `[Insert]` | `[Insert]` | `[FN / FP / large RUL error / other]` | `[Insert]` | `[Insert key explanation features]` | `[Insert short interpretation]` |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

## Section 6: Possible Error Sources

Prompts:

- Is the error likely driven by label ambiguity?
- Is the error likely driven by feature insufficiency?
- Is the error likely driven by operating-condition shift?
- Is the error likely driven by model underfitting or overfitting?
- Is the error likely driven by proxy-label limitations in safety-risk construction?

Entry:

`[Insert structured narrative.]`

## Section 7: Implications for Model Revision

Prompts:

- Which feature groups may need revision?
- Should thresholds, label rules, or split strategy be reconsidered?
- Does the model family appear inadequate for this error pattern?
- Would a simpler but more stable model be preferable?

Entry:

`[Insert structured narrative.]`

## Section 8: Academic Reporting Summary

Use this section to produce a short, thesis-ready paragraph.

Placeholder:

`[Insert concise error-analysis summary suitable for results or discussion chapter.]`
