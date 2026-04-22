# Hypotheses

> Revision summary: This version aligns each hypothesis with named variables, explicit model comparisons, and measurable outcomes rather than broad expectations about model usefulness.

## Overview

The hypotheses below are written to match the variables and objectives defined for the study. They are framed so that each hypothesis can be tested through model comparison, feature analysis, or explainability outputs. Because the final dataset has not yet been selected, the precise thresholds for statistical testing are not specified in this framing document.

## Assumptions

The hypotheses assume that:

- `target_rul` is encoded as a documented prognostic outcome;
- `target_safety_risk` is encoded as a documented safety-related outcome, either directly or through a justified proxy;
- the independent variables include monitored battery variables and engineered degradation or safety-related features; and
- the same train, validation, and test protocol is used when comparing candidate models within each task.

## Variable Alignment

- Dependent variables: `target_rul`, `target_safety_risk`
- Independent variables: monitored battery variables, engineered degradation features, operating-condition variables
- Control variables: dataset source, protocol, chemistry, split strategy, preprocessing settings

## Testable Hypotheses

### H1: Predictive Validity for RUL

Models trained on the independent variables will predict `target_rul` more accurately than a baseline model that does not use the full engineered feature set.

Indicative test basis:
Comparison of regression performance metrics across baseline and candidate RUL models.

### H2: Predictive Validity for Safety Risk

Models trained on the independent variables will predict `target_safety_risk` more accurately than a baseline model that does not use the full engineered feature set.

Indicative test basis:
Comparison of classification or risk-scoring metrics across baseline and candidate safety models.

### H3: Value of Engineered Features

For both `target_rul` and `target_safety_risk`, models trained with engineered degradation and operating-condition features will outperform models trained only on minimally processed monitoring summaries.

Indicative test basis:
Within-task comparison between a reduced-input model and a feature-engineered model.

### H4: Task-Specific Predictor Structure

The most influential predictors identified for `target_rul` will not be identical to the most influential predictors identified for `target_safety_risk`.

Indicative test basis:
Comparison of ranked variable importance or local explanation patterns across the two tasks.

### H5: Partial Predictor Overlap

At least one subset of monitored battery variables will contribute materially to both `target_rul` and `target_safety_risk`, but the relative importance of those shared variables will differ between tasks.

Indicative test basis:
Cross-task comparison of XAI outputs for shared predictors such as voltage, current, temperature, or degradation-derived features.

## Null Hypotheses

- H01: There is no improvement in `target_rul` prediction when using the full independent-variable set compared with the selected baseline model.
- H02: There is no improvement in `target_safety_risk` prediction when using the full independent-variable set compared with the selected baseline model.
- H03: Engineered features do not improve predictive performance for either dependent variable relative to minimally processed inputs.
- H04: The influential predictors for `target_rul` and `target_safety_risk` do not differ in a meaningful way.
- H05: There is no meaningful overlap in influential predictors across the two tasks.

## Boundary Note

These hypotheses do not assume that the same model family will be optimal for both dependent variables. They test whether the proposed variable sets support each task and whether explainability reveals a coherent relationship between degradation-oriented prediction and safety-oriented prediction.
