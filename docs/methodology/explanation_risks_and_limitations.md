# Explanation Risks and Limitations

## Purpose

This document identifies risks and limitations associated with explainability methods in the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The emphasis is on risks that are especially important in safety-critical battery monitoring, where explanation outputs may appear persuasive even when they are incomplete, unstable, or misleading.

## Why a Limitations Framework Is Necessary

Explainability methods do not reveal ground-truth battery mechanisms directly. They reveal how a specific model associates input variables with outputs under the assumptions of the model, the data, and the explanation method used.

In this project, this means that an explanation may be:

- useful without being causal;
- plausible without being fully reliable;
- stable for one model but not another;
- visually intuitive while still being methodologically weak.

## Major Risks

## 1. Mistaking Association for Causation

Risk:
An explanation may identify a variable as influential even though the variable is only correlated with the true mechanism.

Battery-relevant example:

- temperature may appear highly important because it co-varies with another unmeasured process, not because it is the sole causal driver.

Implication:

- explanation outputs should not be interpreted as proof of physical causality.

## 2. Model-Specific Explanation Dependence

Risk:
An explanation describes the behavior of one fitted model, not the full underlying system.

Implication:

- two different models may assign different importance to the same variables;
- explanation conclusions may change across model families.

Recommended response:

- compare explanations across more than one credible model where feasible.

## 3. Instability Across Samples or Runs

Risk:
Local explanations, especially for complex neural models, may change materially across nearby observations or repeated training runs.

Implication:

- a seemingly important variable may not be a stable explanation component.

Recommended response:

- assess explanation stability across folds, seeds, and representative samples.

## 4. Correlated Feature Distortion

Risk:
When features are highly correlated, attribution may be split or shifted across related variables in ways that do not reflect their practical importance.

Battery-relevant example:

- multiple temperature summaries or multiple degradation features may compete in attribution results.

Recommended response:

- review correlated feature groups explicitly;
- use grouped interpretation in addition to individual feature attribution.

## 5. Proxy Label Contamination

Risk:
If `target_safety_risk` is based on a proxy rule, explanations may simply restate the proxy definition rather than reveal broader predictive structure.

Battery-relevant example:

- if high risk is defined mainly by temperature threshold exceedance, the model may simply learn temperature threshold reproduction.

Implication:

- explanation may appear convincing but add limited scientific value.

Recommended response:

- document proxy-label logic explicitly;
- avoid overstating explanation results derived from proxy labels.

## 6. Misleading Attention Interpretation

Risk:
For transformer-based or attention-based models, attention weights may be mistaken for explanations.

Implication:

- visually salient time steps may not correspond directly to predictive contribution.

Recommended response:

- treat attention as descriptive evidence only unless supported by additional attribution analysis.

## 7. Oversimplified Local Narratives

Risk:
A local explanation may support a compelling case narrative that is not representative of general model behavior.

Implication:

- case studies may be overgeneralized.

Recommended response:

- pair local explanations with global explanation context.

## 8. Overconfidence in Safety-Critical Contexts

Risk:
Because explanations appear interpretable, users may over-trust the model in situations where both the model and the explanation remain uncertain.

Implication:

- explanation may create unwarranted confidence in safety judgments.

Recommended response:

- interpret explanations as decision support rather than autonomous safety certification.

## Practical Limitations by Method Type

## Tree-Based Explanations

### Strength

- often strong for tabular engineered features;
- compatible with SHAP and permutation analysis.

### Limitation

- still affected by correlation and proxy-label issues;
- feature importance may differ across tree-based methods.

## Neural-Network Explanations

### Strength

- can attribute influence in complex non-linear models.

### Limitation

- sensitive to baselines, architecture, scaling, and training noise;
- often harder to validate for stability.

## Time-Series Explanations

### Strength

- can reveal temporally relevant regions or channels.

### Limitation

- temporal attribution is often harder to summarize clearly;
- local saliency can be noisy;
- channel and time-step importance may be confounded.

## Interpretation Risks Specific to Battery Monitoring

## 1. Confusing Degradation Interpretation with Safety Interpretation

Low-RUL explanations may emphasize degradation indicators, but this should not automatically be interpreted as immediate safety danger.

## 2. Confusing Thermal Stress with Confirmed Hazard

A thermal explanation may support elevated concern, but not all heating patterns correspond to imminent unsafe events.

## 3. Confusing Proxy-Based Safety Models with Real Event Prediction

If the safety target is inferred, then explanation results describe the inferred labeling framework as much as the battery behavior itself.

## Recommended Safeguards

The project should adopt the following safeguards:

1. Use more than one explanation method where feasible.
2. Compare global and local explanations rather than relying on one level alone.
3. Check explanation stability across folds, seeds, or models.
4. Interpret correlated features at both individual and grouped levels.
5. State clearly when the target label is proxy-based.
6. Use cautious language in safety interpretation.

## Recommended Reporting Language

Suitable academic phrasing includes:

- "The model associated elevated risk primarily with..."
- "The explanation suggests that the prediction was influenced by..."
- "The attribution pattern is consistent with..."

Language to avoid includes:

- "The explanation proves that..."
- "The model identified the true cause..."
- "This confirms that failure will occur..."

## Recommended Conclusion

Explainability in this project should be treated as a structured aid to interpretation, not as a guarantee of truth. In safety-critical battery monitoring, the greatest risks arise when explanations are over-trusted, interpreted causally, or detached from dataset limitations and label quality. A rigorous methodology therefore requires explanation methods to be accompanied by stability checks, proxy-label awareness, cross-method comparison, and cautious safety interpretation.
