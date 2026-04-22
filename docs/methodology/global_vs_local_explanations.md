# Global and Local Explanations

## Purpose

This document distinguishes between global and local explanations in the context of:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The distinction is important because the two types of explanation serve different scientific and operational purposes.

## Conceptual Distinction

### Global Explanation

A global explanation describes how a model behaves across a broad set of observations. It aims to identify which variables are influential in general and how the model tends to use them.

### Local Explanation

A local explanation describes why the model made a specific prediction for a specific observation window. It aims to identify the variables that were influential for one prediction instance rather than for the entire dataset.

## Why the Distinction Matters in This Project

The project requires both forms of explanation because:

- global explanation is needed to compare predictors of `target_rul` and `target_safety_risk` across the dataset;
- local explanation is needed to interpret specific high-risk or low-RUL cases that may be safety-relevant.

Without this distinction, explanations may be overgeneralized or misapplied.

## Global Explanations

## Purpose

Global explanations are useful for:

- identifying dominant feature groups;
- comparing model behavior across tasks;
- informing feature selection and ablation;
- supporting literature-grounded discussion of predictive structure.

## Typical Questions Answered

- Which variables matter most overall for RUL prediction?
- Which variables matter most overall for safety risk prediction?
- Are thermal variables globally more important for safety than for RUL?
- Do degradation indicators dominate the prognostic task?

## Suitable Methods

- global SHAP summaries;
- permutation importance;
- partial dependence plots;
- accumulated local effects;
- feature-group importance analysis.

## Strengths

- useful for model comparison;
- useful for cross-task synthesis;
- suitable for chapter-level interpretation in a thesis or article.

## Limitations

- can hide variation across individual cases;
- may obscure minority or rare but safety-relevant behavior;
- may understate context-dependent interactions.

## Local Explanations

## Purpose

Local explanations are useful for:

- interpreting a specific observation window;
- understanding why a given battery state was predicted as high risk;
- inspecting whether a low-RUL prediction is linked to plausible degradation indicators;
- examining unusual or borderline cases.

## Typical Questions Answered

- Why was this battery window assigned a high safety risk?
- Why was this observation assigned low remaining useful life?
- Which variables most influenced this specific prediction?
- Is the local explanation plausible relative to the observed thermal and electrical behavior?

## Suitable Methods

- local SHAP values;
- integrated gradients;
- local perturbation analysis;
- time-step masking or occlusion for sequence models.

## Strengths

- useful for case-based interpretation;
- important for safety-relevant inspection;
- useful for debugging model behavior.

## Limitations

- may not generalize across the dataset;
- may be unstable for complex models;
- may produce convincing narratives for isolated predictions without confirming broader validity.

## Recommended Use in Battery Monitoring

## For `target_rul`

### Global Explanation Should Be Used To

- identify the main degradation indicators;
- compare the importance of electrical, thermal, and usage variables;
- assess whether the model relies primarily on interpretable degradation signals.

### Local Explanation Should Be Used To

- explain unusually low-RUL predictions;
- inspect cases where the model contradicts expected degradation patterns;
- compare individual low-RUL and high-RUL windows.

## For `target_safety_risk`

### Global Explanation Should Be Used To

- identify whether safety predictions are driven by thermal, electrical, or interaction features;
- assess whether the model reflects plausible risk structure across the dataset.

### Local Explanation Should Be Used To

- inspect specific high-risk predictions;
- identify whether the model relied on interpretable warning indicators such as temperature rise, current spikes, or instability;
- examine false positives and false negatives in safety-oriented classification.

## Recommended Combined Use

The project should not treat global and local explanation as substitutes. Instead, they should be combined in a complementary workflow:

1. use global explanation to understand the broad predictive structure;
2. use local explanation to interpret representative or critical cases;
3. compare whether local explanations are consistent with the global pattern;
4. investigate meaningful deviations rather than dismissing them automatically.

## Safety-Critical Interpretation

In safety-critical battery monitoring, local explanations are especially important because a single high-risk case may be operationally significant even if it represents a minority pattern. However, local explanation alone is not sufficient. A single convincing case study does not prove that the model is generally reliable or generally aligned with physically meaningful behavior.

For this reason:

- global explanation supports model-level trust assessment;
- local explanation supports case-level safety inspection.

## Common Misinterpretations to Avoid

The following interpretation errors should be avoided:

- treating a global ranking as proof of causality;
- treating one local explanation as representative of the whole model;
- assuming that a visually plausible explanation is necessarily correct;
- ignoring disagreement between local and global patterns.

## Recommended Conclusion

Global explanations are most appropriate for understanding general predictive structure, feature importance, and cross-task comparison. Local explanations are most appropriate for interpreting individual battery windows, especially high-risk or low-RUL cases. In this project, both forms are required to support technically grounded and safety-relevant explainability.
