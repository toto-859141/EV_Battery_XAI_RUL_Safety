# Safety Risk Labeling Strategy

## Purpose

This document specifies a proposed labeling strategy for `target_safety_risk` in the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The purpose of this strategy is to define a methodologically defensible approach for translating battery-monitoring data into safety-related labels suitable for supervised machine learning. Because many battery datasets do not contain direct and standardized safety annotations, the labeling strategy must distinguish clearly between:

- observed hazardous events;
- event-proximal risk states; and
- inferred proxy-based safety risk.

## Conceptual Position

In this study, safety risk is defined as the level of concern that a battery observation window may be associated with unsafe, abnormal, or hazard-relevant battery behavior. This concept is related to, but distinct from:

- battery health, which reflects degradation condition;
- fault status, which may refer to a specific diagnosed failure mode;
- remaining useful life, which represents the service life remaining before end-of-life.

Accordingly, `target_safety_risk` should not be treated as a direct substitute for state of health, fault class, or RUL.

## Labeling Priority Order

The recommended priority order for safety labeling is:

1. direct safety labels supplied by the dataset;
2. event-based labels derived from known safety-related events;
3. rule-based proxy labels derived from monitored signals and domain knowledge.

This ordering is recommended because it prioritizes observed information over inferred logic, while still allowing supervised modeling when direct labels are unavailable.

## Possible Safety Risk Levels

## Recommended Risk Scale

For methodological clarity and practical interpretability, the recommended default scale is an **ordinal three-level label**:

- `low risk`
- `medium risk`
- `high risk`

This scale is preferred because it:

- preserves more nuance than a binary label;
- remains easier to justify than a continuous risk score in datasets with uncertain safety annotations; and
- aligns with safety-oriented decision support in which escalation levels are often more useful than exact probabilities.

## Alternative Encodings

Depending on dataset quality and modeling scope, the following encodings may also be used:

### Binary Encoding

- `low risk`
- `high risk`

Recommended when:

- event frequency is low;
- the dataset is small;
- label quality is limited; or
- the initial objective is robust baseline classification.

### Continuous Risk Score

A continuous score may be used only if the dataset or label-generation process supports defensible ranking across safety severity levels.

Recommended caution:

- continuous risk scoring should not be adopted merely for numerical convenience;
- it requires stronger justification than ordinal labeling.

## Proposed Meaning of Risk Levels

### Low Risk

The observation window shows no substantial evidence of abnormal thermal, electrical, or operational behavior according to the adopted rule set. The battery may still be degraded, but no immediate or elevated safety concern is indicated by the available variables.

### Medium Risk

The observation window shows early or moderate evidence of abnormality, stress, or deviation from expected behavior, but not at a level that clearly indicates imminent hazard. This level is intended to capture cautionary states that merit monitoring.

### High Risk

The observation window shows strong evidence of safety-relevant abnormality, proximity to a known event, or multiple concurrent rule violations consistent with elevated hazard concern.

## Rule-Based Labeling Logic

## General Principle

When direct labels are unavailable, `target_safety_risk` should be assigned using explicit and reproducible rules derived from monitored battery variables. The logic should be transparent enough to be audited and sufficiently structured to support later discussion of label validity.

## Recommended Rule Structure

Each observation window should be evaluated across three categories of evidence:

1. thermal abnormality;
2. electrical abnormality;
3. operating stress and instability.

Each category can contribute a partial risk signal, which is then combined into the final label.

## Illustrative Rule Framework

The following framework is recommended as a methodological template rather than a fixed universal rule set.

### Rule Group A: Thermal Indicators

Potential indicators:

- maximum temperature within the window;
- rate of temperature increase;
- temperature variability;
- temperature excursion above a reference range.

Illustrative logic:

- assign one thermal risk point if temperature exceeds a moderate threshold once;
- assign two thermal risk points if temperature exceeds a severe threshold or rises rapidly within a short interval.

### Rule Group B: Electrical Indicators

Potential indicators:

- abnormal voltage deviation;
- voltage instability during charge or discharge;
- unusual current spikes;
- inconsistent current response relative to operating mode.

Illustrative logic:

- assign one electrical risk point for repeated moderate deviation from expected operating behavior;
- assign two electrical risk points for severe deviation or abrupt instability.

### Rule Group C: Stress and Degradation Interaction Indicators

Potential indicators:

- high operating stress under elevated temperature;
- abrupt change in resistance-related proxies;
- combined degradation and thermal-stress signals;
- repeated abnormal windows over a short sequence.

Illustrative logic:

- assign one interaction risk point for a sustained combination of high stress and abnormal degradation features;
- assign two interaction risk points if multiple stress indicators co-occur with strong thermal or electrical abnormality.

## Illustrative Aggregation Logic

After assigning category-level risk points, the final label may be determined as follows:

- `low risk`: total score = 0 or no rule category exceeds the minimum warning condition;
- `medium risk`: total score in an intermediate range or one strong abnormality without event-level evidence;
- `high risk`: total score above a documented threshold, multiple category violations, or known proximity to a safety event.

This scoring approach is recommended because it avoids reducing safety risk to a single-sensor threshold and encourages multi-indicator interpretation.

## Threshold-Based Labeling

## Definition

Threshold-based labeling assigns risk levels by comparing observed variables or derived indicators against predefined cutoffs.

## Appropriate Use

Threshold-based labeling is appropriate when:

- the dataset contains physically meaningful limits or warning thresholds;
- battery operation occurs under controlled conditions;
- the threshold values are documented in test protocols, standards, prior studies, or engineering practice.

## Candidate Threshold Types

Thresholds may be applied to:

- absolute temperature;
- temperature rise rate;
- voltage deviation;
- current excursions;
- resistance-related indicators;
- capacity-related abnormal change;
- combined stress metrics.

## Advantages

- simple to implement and audit;
- easy to communicate in a methodology chapter;
- compatible with engineering rule systems and expert review.

## Limitations

- fixed thresholds may be dataset-specific rather than general;
- thresholds may ignore context such as operating mode, chemistry, or ambient temperature;
- single-threshold logic may overstate risk in noisy measurements or understate risk in complex failure progression.

## Anomaly-Based Labeling

## Definition

Anomaly-based labeling assigns risk based on deviation from expected battery behavior rather than on a fixed threshold alone.

## Appropriate Use

Anomaly-based labeling is appropriate when:

- explicit safety thresholds are unavailable;
- the dataset contains normal operating trajectories but few direct safety events;
- abnormal behavior is more informative than absolute signal magnitude.

## Candidate Anomaly Signals

Anomaly-based labeling may be based on:

- deviation from normal voltage-current-temperature relationships;
- departure from expected cycle-to-cycle degradation trajectories;
- reconstruction error from an unsupervised baseline model;
- residual error from a predictive baseline fitted on nominal behavior;
- abrupt local departures from rolling historical patterns.

## Advantages

- more flexible than fixed-threshold rules;
- can capture context-dependent abnormality;
- may identify subtle precursors to hazardous behavior.

## Limitations

- anomaly does not necessarily imply safety hazard;
- anomaly scores can be sensitive to the choice of reference distribution;
- interpretation may be less direct than threshold-based labeling;
- anomaly labels may reflect rarity rather than true danger.

## Combined Threshold and Anomaly Strategy

For this project, a combined strategy is recommended whenever direct safety labels are absent.

### Recommended Logic

- use threshold-based rules for clear, high-severity abnormality;
- use anomaly-based logic for moderate or emerging abnormality;
- combine both sources of evidence into the final ordinal safety-risk label.

### Rationale

This hybrid approach is methodologically preferable because:

- threshold rules preserve interpretability and engineering traceability;
- anomaly logic captures deviations that fixed thresholds may miss;
- the combined label better reflects the uncertainty inherent in battery safety datasets.

## Incorporation of Domain Knowledge

## Role of Domain Knowledge

Domain knowledge should be incorporated to ensure that labeling rules reflect plausible battery behavior rather than arbitrary statistical separation.

## Sources of Domain Knowledge

Relevant domain knowledge may be drawn from:

- battery engineering literature;
- test standards and protocol documents;
- battery management system design principles;
- expert consultation with battery researchers or engineers;
- experimentally observed signs of thermal or electrical instability.

## Recommended Uses of Domain Knowledge

Domain knowledge should inform:

- selection of relevant monitored variables;
- definition of moderate versus severe abnormality;
- interpretation of combined thermal and electrical stress patterns;
- lead-time definition for event-based labeling;
- exclusion of variables that are not safety-relevant despite statistical variation.

## Practical Example

If temperature, current, and voltage all deviate moderately during high-rate charging, domain knowledge may justify assigning a higher risk level than would be assigned by any one variable in isolation. Conversely, a brief benign temperature fluctuation may not warrant elevated risk if it is consistent with the operating regime.

## Methodological Safeguards

When domain knowledge is used:

- all rules should be written explicitly;
- expert assumptions should be documented rather than treated as self-evident;
- the difference between empirical observation and expert-informed inference should remain visible.

## Limitations of Safety Labels in Battery Datasets

## 1. Scarcity of Direct Safety Labels

Many battery datasets were collected for degradation or performance analysis rather than for safety-risk labeling. As a result, direct annotations of hazardous states may be absent, sparse, or inconsistent.

## 2. Event Rarity and Class Imbalance

Safety-relevant events are often rare relative to normal operation. This creates severe class imbalance and may encourage unstable models or overly simplistic labeling rules.

## 3. Proxy Labels Are Not Equivalent to Observed Hazard

When proxy rules are used, the resulting label represents inferred risk rather than verified danger. This limits the strength of causal or operational claims that can be made from the model outputs.

## 4. Threshold Transferability Is Limited

Thresholds that are reasonable for one chemistry, dataset, or operating protocol may not transfer directly to another. A rule that functions well in laboratory cycling data may perform poorly in vehicle-level field data.

## 5. Measurement Context Affects Label Validity

Sensor location, sampling frequency, noise, and test protocol can all influence whether an observed abnormality reflects a true safety concern or a measurement artifact.

## 6. Safety Risk Is Multi-Dimensional

Battery safety risk may involve thermal, electrical, mechanical, and operational dimensions. A label derived from only one dimension may therefore underrepresent the broader safety state.

## Implications for the Study

Given these limitations, the methodology chapter should state explicitly that:

- the safety label may be direct, event-based, or proxy-based depending on dataset availability;
- proxy labels should be interpreted as operational approximations of safety risk;
- model explanations should be used to examine whether learned patterns are technically plausible;
- conclusions about real-world hazard must be stated cautiously when labels are inferred rather than observed.

## Recommended Reporting Statement

The final methodology chapter should report:

1. the chosen risk scale;
2. the exact rule logic or event logic used for labeling;
3. all thresholds and their justification;
4. whether anomaly scores were used and how they were computed;
5. what domain knowledge informed the rules;
6. the principal limitations of the safety-label construction process.

## Conclusion

For this project, the most defensible default strategy is to define `target_safety_risk` as an ordinal label derived from either direct safety annotations or a transparent hybrid rule set combining threshold-based and anomaly-based evidence. This approach provides a workable balance between interpretability, methodological rigor, and practical feasibility, while making explicit the limitations that arise when battery datasets do not contain direct and standardized safety labels.
