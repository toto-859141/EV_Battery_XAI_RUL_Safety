# Explainability Strategy

## Purpose

This document defines the explainability strategy for the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The strategy is intended to ensure that model explanation is:

- methodologically aligned with the prediction task;
- appropriate to the model family used;
- relevant to safety-critical battery monitoring;
- useful for both scientific interpretation and comparative analysis.

## Role of Explainability in the Project

Explainability is a core analytic component of this project rather than a supplementary visualization layer. Its functions are to:

- identify the monitored variables and engineered features associated with `target_rul`;
- identify the monitored variables and engineered features associated with `target_safety_risk`;
- compare shared versus task-specific predictors across the two tasks;
- assess whether the model relies on technically plausible battery behavior;
- support defensible safety interpretation of prediction outputs.

## Explainability Objectives

The explainability workflow should answer the following questions:

1. Which variables contribute most strongly to each task?
2. Are the dominant predictors stable across validation splits and model families?
3. Do the explanation patterns align with known electrical, thermal, degradation, and usage mechanisms?
4. Are explanations sufficiently clear to support safety-relevant interpretation rather than only statistical description?

## Model-Specific Explainability Recommendations

## 1. Tree-Based Models

Relevant model families:

- random forest;
- gradient boosting;
- XGBoost;
- LightGBM;
- CatBoost.

### Recommended Methods

- SHAP values, especially TreeSHAP where supported;
- permutation importance;
- partial dependence plots or accumulated local effects;
- feature importance from the fitted model, used cautiously.

### Recommended Use

Tree-based models should be explained using SHAP as the primary method because:

- it provides both global and local explanations;
- it supports additive attribution at the feature level;
- it is well suited to structured engineered features.

Permutation importance should be used as a secondary robustness check, because it is model-agnostic and can reveal whether a feature materially affects predictive performance.

### Caution

Built-in importance from tree ensembles should not be treated as sufficient evidence on its own, particularly when features are correlated.

## 2. Neural Networks

Relevant model families:

- multilayer perceptrons;
- hybrid tabular-plus-sequence models;
- multi-task neural networks.

### Recommended Methods

- SHAP approximations for neural models where computationally feasible;
- integrated gradients;
- gradient-based feature attribution;
- input perturbation or occlusion analysis;
- permutation-based importance on engineered companion features.

### Recommended Use

For neural networks trained on tabular or hybrid inputs, integrated gradients or SHAP-based approximations are recommended because they can attribute prediction influence to specific inputs. However, these explanations should be checked for stability across samples and repeated runs.

### Caution

Gradient-based explanations may be sensitive to scaling, baseline choice, and network architecture. They should therefore be interpreted as model-specific attribution methods rather than direct evidence of causality.

## 3. Time-Series Models

Relevant model families:

- LSTM;
- GRU;
- temporal convolutional networks;
- transformer-based time-series models.

### Recommended Methods

- time-step or channel attribution methods;
- integrated gradients over sequences;
- temporal occlusion or masking;
- perturbation-based sensitivity analysis;
- attention analysis only as a descriptive aid, not as a standalone explanation.

### Recommended Use

For time-series models, the explanation strategy should distinguish:

- feature-channel importance, such as voltage versus current versus temperature;
- temporal importance, such as which part of the window influences the prediction most;
- interaction patterns, such as thermal response under high current.

### Caution

Attention weights should not be treated as full explanations unless additional evidence demonstrates that they correspond meaningfully to predictive contribution. In safety-critical settings, they may be useful for inspection but are insufficient as the sole interpretive basis.

## Recommended Explanation Layers

The project should use at least three complementary explanation layers.

### Layer 1: Global Feature Attribution

Purpose:

- identify the dominant predictors across the dataset;
- compare predictor structure between `target_rul` and `target_safety_risk`.

Recommended methods:

- global SHAP summaries;
- permutation importance;
- partial dependence or accumulated local effects where appropriate.

### Layer 2: Local Prediction Explanation

Purpose:

- explain individual high-risk or low-RUL predictions;
- inspect whether specific outputs are consistent with observed battery behavior.

Recommended methods:

- local SHAP values;
- local integrated gradients;
- local perturbation analysis.

### Layer 3: Cross-Task Comparative Explanation

Purpose:

- compare which features matter for RUL versus safety;
- assess whether degradation-oriented and safety-oriented predictors overlap or diverge.

Recommended methods:

- comparison of ranked global importance across tasks;
- comparison of explanation distributions for shared features;
- targeted case-study analysis for windows with both low RUL and elevated safety risk.

## Recommended Workflow

The explainability workflow should proceed as follows:

1. train and validate baseline and advanced models;
2. select candidate models for explanation based on predictive credibility;
3. apply model-appropriate global explanation methods;
4. apply local explanation methods to selected observations;
5. compare explanations across tasks and model families;
6. assess whether explanations are stable, plausible, and safety-relevant.

## Criteria for Useful Explainability in Safety-Critical Battery Monitoring

An explanation should be considered useful only if it satisfies most of the following:

- it identifies variables that can be linked to measurable battery behavior;
- it is stable across repeated runs or validation splits;
- it does not depend entirely on one fragile attribution method;
- it helps distinguish degradation-related from hazard-related influence;
- it supports technical interpretation of high-risk or low-RUL outputs.

## Performance-Explainability Trade-Off

The best-performing model should not automatically be selected as the final preferred model. In this project, the final modeling recommendation should depend on whether the predictive gain of a more complex model is large enough to justify:

- reduced transparency;
- greater explanation uncertainty;
- more difficult safety interpretation.

In some cases, a slightly less accurate but more interpretable tree-based model may be preferable to a more opaque sequence model, especially for safety-relevant reporting.

## Recommended Conclusion

The explainability strategy for this project should be model-aware, task-aware, and safety-aware. Tree-based models should be interpreted primarily with SHAP and permutation-based methods; neural and time-series models should be interpreted using gradient-based and perturbation-based approaches with careful validation. Explanations must be evaluated not only for visual plausibility, but for their usefulness in understanding battery degradation, abnormal behavior, and safety-relevant decision logic.
