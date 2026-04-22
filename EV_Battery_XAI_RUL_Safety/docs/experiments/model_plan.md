# Model Development Plan

## Purpose

This document defines the model development plan for the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The plan is intended to guide the staged development, comparison, and interpretation of predictive models for:

- Remaining Useful Life (`target_rul`); and
- Safety Risk (`target_safety_risk`).

The modeling strategy must support both predictive performance and methodological transparency because explainability is a central objective of the project rather than a secondary visualization step.

## Modeling Objectives

The model development process should:

- establish credible baselines for both tasks;
- evaluate advanced models suitable for time-series battery data;
- compare separate-task and joint-task formulations;
- support explainable analysis of variable contributions;
- produce evidence for the trade-off between predictive performance and interpretability.

## Recommended Development Stages

The model development process should proceed in five stages.

### Stage 1: Baseline Single-Task Models

Train simple and interpretable baseline models separately for:

- `target_rul` regression;
- `target_safety_risk` classification.

Purpose:

- establish minimum performance benchmarks;
- verify dataset usability;
- provide interpretable references for later comparison.

### Stage 2: Strong Classical Machine Learning Models

Train non-linear tabular models using the engineered feature set.

Purpose:

- improve predictive performance while maintaining manageable interpretability;
- provide strong structured baselines before deep learning is introduced.

### Stage 3: Advanced Time-Series Models

Train sequence-oriented models using raw or lightly processed time-series inputs.

Purpose:

- evaluate whether temporal representation learning improves prediction quality;
- test whether sequence models capture patterns not represented by summary features alone.

### Stage 4: Joint and Multi-Task Modeling

Evaluate whether shared representations can support both `target_rul` and `target_safety_risk`.

Purpose:

- assess whether shared battery signals contain useful cross-task information;
- determine whether multi-task learning improves one or both tasks.

### Stage 5: Ablation and Explainability Analysis

Conduct structured ablation studies and explanation analysis across candidate models.

Purpose:

- identify the contribution of feature groups, input representations, and architectural choices;
- assess the performance-interpretability trade-off.

## Recommended Modeling Formulations

Three formulations should be considered:

1. separate-task modeling;
2. joint-task comparison without parameter sharing;
3. multi-task learning with partial or full shared representation.

The recommended default starting point is separate-task modeling, followed by multi-task comparison only after stable single-task benchmarks are established.

## Recommended Experimental Sequence

The recommended sequence is:

1. train baseline models for `target_rul`;
2. train baseline models for `target_safety_risk`;
3. train stronger tabular models for each task;
4. train sequence models for each task;
5. compare separate-task and multi-task approaches;
6. conduct ablation studies;
7. apply XAI to the most credible models.

This sequence is recommended because it ensures that more complex models are interpreted against clear reference points.

## Evaluation Priorities

Models should be compared using three criteria:

### 1. Predictive Performance

- regression quality for `target_rul`;
- classification quality for `target_safety_risk`.

### 2. Interpretability

- extent to which variable contributions can be explained;
- stability of explanations across validation splits;
- plausibility of explanations in relation to battery behavior.

### 3. Safety Relevance

- whether the model supports technically defensible safety interpretation;
- whether the model distinguishes degradation-related and risk-related patterns appropriately.

## Practical Recommendation

For this project, the most defensible modeling strategy is:

- begin with separate, interpretable baselines for each task;
- add stronger classical machine learning models using engineered features;
- introduce advanced sequence models only after the tabular baselines are stable;
- evaluate multi-task learning as an empirical question rather than as an assumed improvement.

## Link to Companion Documents

Detailed guidance is provided in:

- `baseline_models.md`
- `advanced_models.md`
- `multitask_learning_strategy.md`
- `ablation_study_plan.md`
