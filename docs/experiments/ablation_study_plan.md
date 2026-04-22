# Ablation Study Plan

## Purpose

This document proposes an ablation strategy for evaluating the contribution of:

- feature groups;
- input representations;
- model components;
- task formulations.

The ablation studies are intended to clarify which design choices materially affect predictive performance and interpretability in the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

## Why Ablation Is Necessary

In this project, high predictive performance alone is not sufficient. The study also needs to determine:

- which feature groups drive each task;
- whether raw sequences add value beyond engineered features;
- whether multi-task learning is beneficial;
- whether complexity reduces interpretability without enough performance gain.

## Recommended Ablation Categories

## 1. Feature Group Ablation

### Purpose

Evaluate the contribution of the main feature groups:

- electrical behavior;
- thermal behavior;
- degradation indicators;
- operational usage patterns.

### Recommended Designs

- full feature set;
- remove one feature group at a time;
- train using each feature group alone;
- compare feature-group combinations where relevant.

### Questions Addressed

- Which feature group is most important for `target_rul`?
- Which feature group is most important for `target_safety_risk`?
- Which feature groups are shared across both tasks?

## 2. Representation Ablation

### Purpose

Evaluate whether sequence representations outperform structured engineered features.

### Recommended Designs

- engineered features only;
- raw sequences only;
- hybrid engineered-plus-sequence representation.

### Questions Addressed

- Does temporal sequence modeling add value beyond summary features?
- Is the hybrid representation better than either representation alone?

## 3. Model Family Ablation

### Purpose

Compare simpler and more complex model families using the same input set.

### Recommended Designs

- linear or logistic baseline;
- tree-based model;
- gradient boosting model;
- recurrent or convolutional sequence model.

### Questions Addressed

- How much performance is gained by increasing model complexity?
- Is the gain large enough to justify reduced interpretability?

## 4. Multi-Task Versus Single-Task Ablation

### Purpose

Determine whether shared learning improves one or both tasks.

### Recommended Designs

- single-task RUL model;
- single-task safety model;
- multi-task shared-backbone model.

### Questions Addressed

- Does multi-task learning improve both tasks, one task, or neither?
- Does shared learning alter explanation patterns?

## 5. Interpretable Feature Subset Ablation

### Purpose

Evaluate whether a reduced interpretable feature set performs competitively against the full feature inventory.

### Recommended Designs

- full engineered feature set;
- reduced interpretable subset;
- highly compact core feature subset.

### Questions Addressed

- Can simpler, more interpretable models remain competitive?
- Does the full feature inventory produce only marginal gains?

## Recommended Ablation Sequence

The recommended order is:

1. feature-group ablation;
2. representation ablation;
3. model-family ablation;
4. multi-task ablation;
5. interpretable-subset ablation.

This order is recommended because it moves from data representation to model structure and finally to higher-level design decisions.

## Evaluation Criteria

Each ablation should be evaluated using:

### Predictive Metrics

- regression metrics for `target_rul`;
- classification metrics for `target_safety_risk`.

### Explanation Quality

- stability of feature importance or attribution patterns;
- consistency of dominant predictors across validation splits;
- plausibility of explanation results.

### Practical Interpretation

- whether the ablated model remains technically interpretable;
- whether the lost performance is small or substantial;
- whether the removed component materially affected safety relevance.

## Performance-Explainability Trade-Off

Ablation analysis should be used to evaluate the performance-interpretability trade-off directly.

### Example Interpretation Logic

- if a highly complex model improves performance only marginally over gradient boosting but produces much weaker explanations, the simpler model may be preferable;
- if removing degradation indicators sharply reduces RUL performance but has limited effect on safety prediction, this supports task-specific feature interpretation;
- if thermal features strongly affect safety prediction but only modestly affect RUL, this helps distinguish the predictive structure of the two tasks.

## Recommended Reporting Format

For each ablation experiment, report:

1. model family;
2. input configuration;
3. ablated component;
4. change in primary evaluation metric;
5. change in explanation pattern, if applicable;
6. interpretation of what the ablation reveals.

## Recommended Conclusion

The ablation strategy should not be treated as a minor supplementary analysis. In this project, it is a core methodological tool for determining whether improved performance arises from:

- genuinely informative battery representations;
- feature engineering choices;
- temporal modeling;
- or merely increased model complexity.

This is especially important given the project objective of balancing prediction quality with explainability and safety relevance.
