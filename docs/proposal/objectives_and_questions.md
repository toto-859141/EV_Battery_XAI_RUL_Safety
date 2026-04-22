# Objectives and Research Questions

> Revision summary: This version makes the objectives operational and measurable by linking them to concrete outputs, comparison criteria, and evaluation targets for both prediction tasks.

## Overview

This study seeks to develop an explainable machine learning framework for electric vehicle batteries using battery monitoring data as predictors and two dependent variables as outcomes: `target_rul` and `target_safety_risk`. The objectives are defined so that each can be assessed through identifiable outputs, model comparisons, or explanation results.

## General Objective

To develop and evaluate an explainable machine learning framework that predicts `target_rul` and `target_safety_risk` from battery monitoring data and engineered features, and that identifies the variables contributing to each prediction task.

## Specific Objectives

### Objective 1: Data and Target Definition

To construct a documented analytical dataset that includes:

- cleaned battery monitoring inputs;
- engineered predictors derived from those inputs;
- an explicit definition of `target_rul`; and
- an explicit definition of `target_safety_risk`.

Measurable output:
A reproducible dataset specification and processed feature set suitable for supervised learning.

### Objective 2: RUL Modeling

To train and evaluate at least one baseline model and at least one non-linear machine learning model for `target_rul` prediction.

Measurable output:
Comparative RUL performance results using predefined regression metrics such as MAE, RMSE, or related task-appropriate measures.

### Objective 3: Safety Risk Modeling

To train and evaluate at least one baseline model and at least one non-linear machine learning model for `target_safety_risk` prediction.

Measurable output:
Comparative safety risk performance results using predefined classification or scoring metrics such as F1-score, AUROC, precision-recall measures, or task-appropriate alternatives.

### Objective 4: Feature Contribution Analysis

To apply XAI methods to quantify and compare the contribution of input variables and engineered features to `target_rul` and `target_safety_risk` predictions.

Measurable output:
Ranked feature-importance or local explanation results for each task, together with a comparison of overlapping and task-specific predictors.

### Objective 5: Model Selection Under Multiple Criteria

To compare candidate models using three criteria:

- predictive performance;
- interpretability of variable contributions; and
- relevance of the identified predictors to battery degradation and safety monitoring.

Measurable output:
A justified model selection statement indicating which approach provides the strongest overall trade-off for the project aims.

## Research Questions

### Main Research Question

How can explainable artificial intelligence be used to predict and interpret `target_rul` and `target_safety_risk` in electric vehicle batteries from battery monitoring data?

### Sub-Questions

#### RQ1

Which monitored battery variables and engineered features provide the strongest predictive value for `target_rul`?

#### RQ2

Which monitored battery variables and engineered features provide the strongest predictive value for `target_safety_risk`?

#### RQ3

How do baseline and non-linear machine learning models differ in predictive performance for `target_rul` and `target_safety_risk`?

#### RQ4

Which variables are identified by XAI methods as the dominant contributors to `target_rul` prediction and to `target_safety_risk` prediction?

#### RQ5

To what extent are the dominant predictors for `target_rul` shared with, or distinct from, the dominant predictors for `target_safety_risk`?

## Assumptions

These objectives and questions assume that:

- the selected dataset supports supervised learning for both dependent variables, either directly or through a documented proxy for safety risk; and
- the final methodology will specify the exact metrics, baseline models, and XAI methods used for comparison.
