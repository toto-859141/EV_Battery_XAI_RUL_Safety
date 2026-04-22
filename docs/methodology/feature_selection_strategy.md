# Feature Selection Strategy

## Purpose

This document proposes a feature-selection strategy for the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The strategy is designed for both:

- classical machine learning using explicit engineered features; and
- deep learning workflows in which engineered features may be used as companion or hybrid inputs.

The selection process must support predictive performance while preserving interpretability and minimizing redundancy and leakage.

## Objectives of Feature Selection

Feature selection should aim to:

- reduce irrelevant or redundant variables;
- improve model stability;
- support explainable analysis;
- avoid selection bias and data leakage;
- preserve variables with clear physical meaning where possible.

## General Principles

All feature selection in this project should follow five principles:

1. Selection must be performed using training data only.
2. Feature choice should consider both predictive value and interpretability.
3. RUL and safety risk tasks should be reviewed separately because the most informative features may differ.
4. Domain knowledge should be used to retain physically meaningful variables, especially in safety-relevant analysis.
5. Deep learning workflows should not assume that explicit feature selection is unnecessary; structured companion features may still require pruning or grouping.

## Recommended Multi-Stage Selection Process

## Stage 1: Conceptual Filtering

Purpose:
Remove variables that should never be used as predictive inputs.

Examples:

- identifiers such as `battery_id`;
- direct leakage variables;
- post-event fields unavailable at prediction time;
- duplicate administrative metadata with no predictive meaning.

Recommended action:

- perform a manual review against the data dictionary and label definitions.

## Stage 2: Data Quality Filtering

Purpose:
Remove features with weak practical value because of poor measurement quality.

Examples:

- features with excessive missingness;
- near-constant variables;
- variables dominated by sensor noise;
- features that cannot be reproduced consistently across batteries or splits.

Recommended action:

- define and document missingness and low-variance thresholds within the training set.

## Stage 3: Redundancy Review

Purpose:
Reduce highly correlated or conceptually overlapping features.

Examples:

- multiple summary features that encode nearly identical information;
- duplicate temperature summaries from the same signal;
- strongly collinear degradation features.

Recommended action:

- apply correlation analysis or variance inflation review within the training data;
- retain the more interpretable feature when predictive evidence is similar.

## Stage 4: Univariate Screening

Purpose:
Identify features with weak direct association to the task.

Recommended methods:

- correlation with `target_rul` for regression-oriented screening;
- mutual information for either task;
- univariate tests suited to classification for `target_safety_risk`.

Recommended caution:

- do not rely on univariate screening alone, because battery behavior is often multivariate and interaction-driven.

## Stage 5: Model-Based Selection

Purpose:
Identify features that remain important in multivariate prediction.

Recommended methods for classical ML:

- L1-regularized linear models;
- tree-based feature importance;
- permutation importance on the validation set;
- recursive feature elimination where computationally feasible.

Recommended action:

- compare selected features across multiple model families rather than relying on one estimator only.

## Stage 6: Stability and Interpretability Review

Purpose:
Ensure that the selected feature set is not only predictive but also stable and meaningful.

Recommended checks:

- does the feature remain important across folds or blocked validation splits?
- does the feature remain important across similar model families?
- can the feature be interpreted physically or operationally?
- is the feature likely to generalize beyond one dataset split?

## Task-Specific Selection Strategy

## A. Selection for `target_rul`

Priority should be given to features that represent:

- long-term degradation;
- gradual change over cycles or time;
- usage burden and operating stress;
- stable trajectory information.

Examples:

- capacity retention;
- capacity fade rate;
- resistance proxies;
- energy throughput;
- charge-discharge duration;
- depth of discharge.

Recommended caution:

- very short-horizon anomaly features may be less useful for long-horizon RUL unless they are linked to persistent degradation.

## B. Selection for `target_safety_risk`

Priority should be given to features that represent:

- thermal abnormality;
- electrical instability;
- abrupt or repeated stress patterns;
- context-dependent hazard indicators.

Examples:

- maximum temperature;
- temperature rise rate;
- temperature excursion count;
- current spike count;
- voltage-current inconsistency;
- high-stress operation frequency.

Recommended caution:

- if proxy safety labels are used, selection must avoid trivial duplication of the proxy rule.

## Recommended Selection Methods by Workflow

## Classical Machine Learning

Recommended sequence:

1. conceptual filtering;
2. missingness and low-variance filtering;
3. collinearity review;
4. univariate screening;
5. model-based importance review;
6. final interpretability review.

Suitable methods:

- correlation filtering;
- mutual information;
- Lasso or elastic net;
- random forest importance;
- gradient boosting importance;
- permutation importance.

## Deep Learning

Deep learning may reduce the need for aggressive manual selection of raw sequence channels, but engineered companion features still require structured review.

Recommended sequence:

1. retain core raw channels such as voltage, current, and temperature;
2. apply conceptual filtering to engineered scalar features;
3. remove highly redundant scalar features;
4. use ablation studies to test the value of feature groups;
5. compare raw-sequence-only models against hybrid models.

Suitable methods:

- channel ablation;
- feature-group ablation;
- attention or attribution analysis;
- permutation tests on companion scalar features.

## Feature Group Selection

In addition to individual-feature selection, this project should evaluate feature groups as coherent units:

- electrical behavior group;
- thermal behavior group;
- degradation indicator group;
- operational usage pattern group.

This is recommended because:

- it aligns with the conceptual framework;
- it simplifies ablation analysis;
- it supports interpretation of which domains of battery behavior drive each task.

## Interpretability-Preserving Recommendation

When two feature sets produce similar predictive performance, preference should be given to the set that:

- uses fewer variables;
- has clearer physical meaning;
- provides more stable explanations across validation splits.

This recommendation is especially important because explainable AI is a central component of the project rather than an optional add-on.

## Practices to Avoid

The following practices should be avoided:

- feature selection on the full dataset before splitting;
- retaining features that encode future information;
- keeping large numbers of highly redundant variables without justification;
- removing physically meaningful features solely because they appear weaker in one split;
- using post hoc importance from the final test set to decide the final feature set.

## Recommended Outputs

The feature-selection process should produce:

1. a baseline full engineered feature set;
2. a reduced interpretable feature set;
3. task-specific subsets for RUL and safety risk;
4. ablation results at feature-group level;
5. documented reasons for retaining or removing major features.
