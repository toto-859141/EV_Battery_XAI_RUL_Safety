# Safety Interpretation Framework

## Purpose

This document defines a framework for translating model outputs and explanation results into safety-relevant interpretations in the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The framework is intended to ensure that safety interpretation remains technically grounded and does not confuse:

- model prediction;
- statistical association;
- inferred safety concern;
- observed hazard.

## Conceptual Principle

Model outputs in this project are predictive signals, not direct safety verdicts. A safety-relevant interpretation must therefore proceed in stages rather than treating model output as self-explanatory.

In particular:

- `target_safety_risk` is a modeled outcome that may be direct or proxy-based;
- `target_rul` is a prognostic outcome and is not itself a direct safety label;
- battery health is an inferred condition construct and is not identical to either output.

## Translation Chain from Model Output to Safety Interpretation

The recommended interpretation chain is:

1. observe the model output;
2. inspect the explanation of the output;
3. identify the dominant contributing variables;
4. map those variables to plausible thermal, electrical, degradation, or usage mechanisms;
5. interpret the result as a safety-relevant inference, not as proof of hazard.

## Step 1: Interpret the Output Type Correctly

### For `target_safety_risk`

The output should be interpreted as:

- a predicted risk class;
- a predicted risk score; or
- a predicted probability of a risk label.

This output should not automatically be interpreted as:

- confirmation that a dangerous event will occur;
- proof that the battery is unsafe in an operational sense.

### For `target_rul`

The output should be interpreted as a prediction of service life remaining before end-of-life according to the selected criterion.

Low predicted RUL may be safety-relevant when it reflects severe degradation or stress accumulation, but it does not automatically imply immediate hazard.

## Step 2: Inspect Explanation Results

Explanation results should identify which features contributed most strongly to the prediction.

Relevant feature domains include:

- thermal indicators;
- electrical behavior indicators;
- degradation indicators;
- operational usage patterns.

The central interpretive question is:

Which observed battery behaviors caused the model to assign elevated risk or reduced useful life?

## Step 3: Map Features to Safety-Relevant Mechanisms

The explanation should then be interpreted in relation to plausible battery mechanisms.

### Thermal Interpretation

If the explanation is dominated by:

- maximum temperature;
- temperature rise rate;
- temperature excursion count;

then the safety interpretation may emphasize thermal stress, abnormal heating, or heat accumulation.

### Electrical Interpretation

If the explanation is dominated by:

- voltage instability;
- current spikes;
- voltage-current inconsistency;

then the safety interpretation may emphasize electrical abnormality, unstable loading, or non-standard operating response.

### Degradation Interpretation

If the explanation is dominated by:

- capacity retention;
- resistance growth;
- degradation acceleration indicators;

then the interpretation may emphasize degraded condition that could indirectly elevate safety concern or reduce robust operation.

### Operational Interpretation

If the explanation is dominated by:

- high charge rate;
- deep discharge;
- repeated high-stress operation;

then the interpretation may emphasize usage-induced stress rather than a direct fault signal.

## Step 4: Distinguish Safety-Relevant Interpretation from Safety Claim

The interpretation framework should distinguish among three statements:

### Statement Type A: Model Output Statement

Example:

The model predicts `high risk` for this observation window.

### Statement Type B: Explanation Statement

Example:

The prediction is primarily associated with high temperature rise, repeated current spikes, and elevated maximum temperature.

### Statement Type C: Safety-Relevant Interpretation

Example:

This battery window shows a pattern consistent with elevated thermal and electrical stress, which may justify heightened monitoring or caution.

The study should avoid moving directly from Statement Type A to a stronger claim such as:

- the battery is unsafe;
- failure is imminent;
- the model has diagnosed a specific fault mechanism.

Such claims require additional evidence beyond model output and attribution.

## Recommended Interpretation Categories

For thesis or report writing, safety-relevant interpretations may be grouped into the following categories:

### 1. Thermal Stress Interpretation

Use when explanations emphasize thermal variables and heating dynamics.

### 2. Electrical Instability Interpretation

Use when explanations emphasize abnormal voltage-current behavior.

### 3. Degradation-Linked Risk Interpretation

Use when explanations emphasize severe aging indicators that may weaken stable operation.

### 4. Usage-Driven Risk Interpretation

Use when explanations emphasize aggressive or repeated stress-inducing operating patterns.

### 5. Mixed-Mechanism Interpretation

Use when no single feature domain dominates and the model appears to rely on interacting thermal, electrical, and degradation signals.

## Role of Human Review

In safety-critical battery monitoring, model interpretation should be treated as decision support rather than autonomous judgment.

Accordingly, explanation results should support:

- technical review;
- comparison with engineering expectations;
- prioritization of further inspection;
- identification of suspicious cases for domain-expert analysis.

## Recommended Interpretation Workflow

1. identify predictions of interest, such as high-risk or unexpectedly low-RUL cases;
2. generate local explanations for those cases;
3. compare the local explanation against global explanation patterns;
4. map the influential features to thermal, electrical, degradation, or usage domains;
5. write a safety-relevant interpretation using cautious, non-causal language;
6. record unresolved uncertainty where the explanation is ambiguous.

## Practical Example

If a battery window is predicted as high safety risk and the explanation highlights:

- high maximum temperature;
- rapid temperature rise;
- high-rate charging;

then a suitable interpretation would be:

The model associates this battery window with elevated thermal and operational stress. This pattern is consistent with increased safety concern and may justify additional inspection or monitoring.

A less appropriate interpretation would be:

The battery will enter thermal runaway.

The latter statement exceeds what the model output and explanation alone can justify.

## Recommended Conclusion

Safety-relevant interpretation in this project should be structured, cautious, and mechanism-aware. Model outputs become useful for safety-critical battery monitoring only when they are translated through explanation results into technically plausible interpretations of thermal, electrical, degradation, and usage behavior. Even then, the interpretation should remain an informed inference rather than a direct claim of hazard certainty.
