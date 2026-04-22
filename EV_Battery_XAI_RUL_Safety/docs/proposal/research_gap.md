# Research Gap

> Revision summary: This version narrows the gap statement to the specific missing link in the topic: the lack of studies that jointly model RUL and safety risk from battery monitoring data with explicit target definitions and explainable variable attribution.

## Overview

The proposed study is positioned at the intersection of three established research areas:

- battery prognostics and RUL prediction;
- battery fault, anomaly, or safety-related prediction; and
- explainable artificial intelligence for machine learning models.

The research gap does not lie in the existence of these fields individually. The gap lies in their limited integration for electric vehicle battery analysis under a single, explicit, and reproducible framework.

## Methodological Gap

### Gap 1: RUL and Safety Risk Are Commonly Modeled as Separate Tasks

The literature contains substantial work on battery RUL prediction and substantial work on abnormality detection or safety-related classification. However, these tasks are often developed independently, with different target definitions, different feature sets, and different evaluation goals. This leaves an unresolved methodological question: whether the same battery monitoring variables can support both `target_rul` and `target_safety_risk`, and whether the influential predictors are shared or task-specific.

### Gap 2: Safety Risk Is Often Poorly Operationalized

RUL is commonly tied to an end-of-life threshold, whereas safety risk is frequently defined less explicitly. In many battery datasets, safety is represented through indirect indicators, experimental conditions, or proxy events. When the operational definition of safety risk is left implicit, model outputs become difficult to interpret, compare, and validate. A clear gap therefore exists in the explicit formulation of `target_safety_risk` as a dependent variable with documented measurement logic.

### Gap 3: Explainability Is Rarely Used to Compare the Two Prediction Tasks

Explainability methods are sometimes applied to battery models, but often only to explain a single model after training. Fewer studies use explainability to examine whether the predictors of RUL differ from the predictors of safety risk. This leaves a gap in comparative interpretation: the field lacks a clear account of which monitored variables are important for long-term degradation forecasting and which are important for safety-oriented prediction.

### Gap 4: Data Processing Choices Are Not Always Connected to Interpretability

Battery modeling studies often report predictive performance without showing how preprocessing, feature engineering, target construction, and data partitioning influence the meaning of the model explanations. This weakens the interpretive value of XAI outputs because the explanatory layer may reflect preprocessing artifacts rather than task-relevant battery behavior.

## Practical Gap

### Gap 5: High-Accuracy Models Do Not Automatically Support Safety-Relevant Decision Making

In safety-relevant applications, a model output is more useful when the prediction can be traced to measurable battery behavior. A black-box model may yield strong predictive metrics but still provide limited support for technical review, maintenance reasoning, or safety interpretation. The practical gap is therefore not only in prediction performance, but in prediction performance that remains interpretable enough for engineering use.

### Gap 6: Battery Health, Safety Risk, and RUL Are Not Always Distinguished Clearly

Some studies use these concepts in overlapping ways, which can obscure what a model actually predicts. This is a practical and methodological problem because it can lead to imprecise claims, ambiguous target construction, and weak alignment between variables, tasks, and evaluation metrics.

## Precise Gap Addressed by This Study

This study addresses the absence of a research framework for electric vehicle batteries in which:

1. battery monitoring variables are processed into explicitly defined predictors;
2. `target_rul` and `target_safety_risk` are modeled as separate dependent variables;
3. the contribution of input variables to each target is interpreted using XAI; and
4. predictive performance and interpretability are evaluated together.

## Contribution Implied by the Gap

If the proposed framework is implemented successfully, it will contribute:

- a clearer separation of battery health, safety risk, and RUL in model design;
- an explicit target-definition strategy for safety risk and RUL;
- measurable comparison of task-specific model performance; and
- interpretable evidence about which monitored variables influence each task.

## Assumption Boundary

Because the final dataset has not yet been fixed, this gap statement is framed at the level of research design. It should later be sharpened further through a systematic literature review tied to the chosen dataset, target encoding, and evaluation protocol.
