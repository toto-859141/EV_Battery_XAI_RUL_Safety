# Safety Warning Logic

## Purpose

This document defines a methodological framework for translating predictive outputs into warning-oriented interpretation in the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The purpose of this framework is not to define an operational deployment policy at the current stage of the research. Rather, it is to explain how model outputs may be interpreted cautiously as warning-relevant signals in a safety-critical battery monitoring context.

## Conceptual Principle

Safety warning logic should be treated as an interpretation layer built on top of predictive outputs, not as a direct automatic consequence of model inference.

In particular:

- a predicted safety-risk class is not equivalent to a confirmed hazard;
- a low predicted RUL is not equivalent to an immediate unsafe state;
- explainability output is not a substitute for engineering judgment;
- warning generation should be regarded as decision support rather than autonomous certification.

## Translating Safety Risk Predictions into Warning Levels

## General Principle

Predicted safety-risk outputs may be mapped into warning levels when the model and labeling strategy are sufficiently documented. The warning logic should preserve a distinction between:

- model-level prediction;
- operational concern level;
- required human or system response.

## Recommended Warning Levels

The following staged warning structure is recommended for methodology design:

### Level 0: No Warning

Interpretation:

- the current observation window does not indicate elevated concern under the model and selected thresholds.

Recommended meaning:

- no warning is issued;
- continued routine monitoring is appropriate.

### Level 1: Advisory Warning

Interpretation:

- the model indicates low to moderate concern, or there is emerging abnormality that does not yet justify a strong alert.

Recommended meaning:

- increase observation frequency;
- review recent operating conditions;
- check whether the pattern persists over subsequent windows.

### Level 2: Caution Warning

Interpretation:

- the model indicates elevated safety concern based on one or more strong contributing indicators, such as thermal excursions, electrical instability, or repeated stress patterns.

Recommended meaning:

- conduct targeted diagnostic review;
- inspect recent electrical and thermal behavior;
- evaluate whether operating limits should be tightened.

### Level 3: High-Priority Warning

Interpretation:

- the model indicates strongly elevated risk, especially when supported by consistent explanation patterns and repeated abnormal observations.

Recommended meaning:

- immediate engineering review is warranted;
- operational mitigation or further system checks may be justified;
- the case should be escalated rather than treated as a routine event.

## Recommended Mapping Logic

The exact mapping should depend on the form of `target_safety_risk`.

### If the Model Outputs Risk Classes

Possible mapping:

- `low risk` -> Level 0 or Level 1
- `medium risk` -> Level 1 or Level 2
- `high risk` -> Level 2 or Level 3

### If the Model Outputs Risk Probabilities or Scores

Possible mapping:

- lower score region -> no warning or advisory warning
- intermediate score region -> caution warning
- upper score region -> high-priority warning

### Methodological Caution

Thresholds for warning levels should not be selected solely for convenience. They should be calibrated using:

- validation performance;
- class distribution;
- risk tolerance of the intended use context;
- stability of explanation patterns.

## Interpreting RUL and Safety Risk Together

## Why Joint Interpretation Matters

The project models `target_rul` and `target_safety_risk` as separate but related outputs. Their joint interpretation may provide richer decision support than either output alone.

## Recommended Joint Interpretation Cases

### Case 1: Low Safety Risk and High RUL

Interpretation:

- the battery appears relatively stable in both short-horizon safety and longer-horizon service-life terms.

Methodological implication:

- routine monitoring is likely sufficient.

### Case 2: Low Safety Risk and Low RUL

Interpretation:

- the battery may be substantially degraded and near end-of-life, but not necessarily in an immediate high-risk state.

Methodological implication:

- maintenance or replacement planning may be more relevant than urgent safety escalation.

### Case 3: High Safety Risk and High or Moderate RUL

Interpretation:

- the battery may exhibit abnormal or hazardous patterns that are not explained solely by end-of-life proximity.

Methodological implication:

- safety-oriented investigation is required;
- the case should not be dismissed simply because predicted RUL remains moderate.

### Case 4: High Safety Risk and Low RUL

Interpretation:

- the battery may exhibit both severe degradation and elevated abnormality, making the case particularly important for engineering review.

Methodological implication:

- this is a high-priority interpretive category for the study;
- cross-task explanation comparison is especially valuable here.

## Recommended Joint Interpretation Rule

RUL and safety-risk outputs should be interpreted jointly as complementary evidence, not collapsed into a single undifferentiated health score. This is necessary to preserve the conceptual distinction between:

- long-term usability;
- immediate or near-term abnormality;
- inferred battery condition.

## Role of Explainability in Decision Support

## Why Explanations Matter

A warning signal is more useful in safety-critical battery monitoring when the model can indicate why the warning was produced.

Explainability can support decision support by:

- identifying whether the warning is driven by thermal, electrical, degradation, or usage features;
- distinguishing persistent degradation from abrupt abnormality;
- helping reviewers understand why RUL and safety-risk predictions agree or diverge;
- supporting prioritization of cases for deeper inspection.

## Recommended Explanation Use by Warning Level

### For Advisory or Caution Warnings

Use explanation outputs to determine:

- whether the signal is driven by a single feature or multiple features;
- whether the pattern is primarily thermal, electrical, or usage-related;
- whether the warning is consistent with recent operating context.

### For High-Priority Warnings

Use explanation outputs to determine:

- which variables most strongly contributed to the alert;
- whether the explanation is stable across similar nearby windows;
- whether the warning aligns with known engineering expectations.

## Limits of Explanation-Supported Decision Support

Explanation should support, but not replace:

- engineering review;
- direct diagnostic analysis;
- sensor validation;
- operational safety checks.

## Safeguards Before Operational Deployment

## General Principle

Before any model-derived warning logic is considered for operational deployment, additional safeguards are required beyond predictive performance.

## Recommended Safeguards

### 1. Label Validity Review

The safety target must be evaluated to determine whether it is:

- directly observed;
- event-based;
- proxy-based.

Proxy-based targets should not be deployed as if they were validated hazard labels without further evidence.

### 2. External Validation

The warning logic should be tested on data not used in model development, ideally including:

- unseen batteries;
- different operating conditions;
- different temporal segments.

### 3. Stability Review

Predictions and explanation patterns should be assessed for stability across:

- random seeds;
- validation splits;
- nearby observations;
- comparable operating regimes.

### 4. False-Alarm Review

Operational deployment requires understanding the consequences of:

- false positives, which may cause unnecessary intervention;
- false negatives, which may miss important abnormality.

### 5. Human-in-the-Loop Oversight

Model-derived warnings should initially function within a supervised review framework rather than as autonomous control decisions.

### 6. Monitoring of Data Drift

Deployment should include procedures for detecting:

- shift in operating patterns;
- shift in sensor behavior;
- change in label relevance or calibration.

### 7. Explanation Auditability

The deployed warning system should retain explanation artifacts or explanation summaries so that warning decisions can be reviewed after the fact.

## Recommended Reporting Language

Appropriate language for the thesis or methodology chapter includes:

- "Predicted safety-risk outputs may be mapped to warning levels for decision-support purposes."
- "Warning interpretation should remain conditional on model validity, label quality, and engineering review."
- "Low predicted RUL may increase concern when accompanied by elevated risk indicators, but it should not be interpreted as a direct warning in isolation."

Language to avoid includes:

- "The model determines whether the battery is safe."
- "The warning output confirms hazardous failure."
- "The warning logic is operationally deployable without further validation."

## Recommended Conclusion

In this project, safety warning logic should be treated as a cautious interpretive framework built on predicted safety risk, predicted RUL, and explanation results. Safety-risk predictions may be translated into staged warning levels, and joint interpretation with RUL may improve decision support. However, such warning logic should remain conditional, explanation-supported, and subject to explicit safeguards before any operational deployment is considered.
