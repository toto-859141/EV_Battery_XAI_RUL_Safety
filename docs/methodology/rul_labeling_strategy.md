# RUL Labeling Strategy

## Purpose

This document defines a methodological strategy for constructing Remaining Useful Life (`target_rul`) labels for the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The objective is to specify how RUL should be defined, how end-of-life should be determined, how labels should be aligned with data granularity, and what practical issues arise when battery-use records are incomplete, irregular, or only partially observed.

## Conceptual Definition of RUL

Remaining Useful Life (RUL) is defined as the amount of service remaining between the end of the current observation window and the point at which the battery reaches a predefined end-of-life criterion.

In this study, RUL is treated as:

- a prognostic target;
- a forward-looking quantity;
- a quantity distinct from battery health and safety risk.

This distinction is important because:

- battery health refers to the present degradation condition of the battery;
- safety risk refers to the likelihood or severity of unsafe behavior;
- RUL refers to the remaining service duration before the battery becomes unsuitable according to a defined operational threshold.

## Recommended Form of the RUL Label

The preferred default is a **continuous regression label**.

Depending on the dataset structure, this may be expressed in:

- cycles remaining;
- operating time remaining;
- cumulative usage units remaining, if such units are better aligned with the data source.

For most battery aging datasets with cycle-based experiments, cycles remaining are the most interpretable and methodologically straightforward representation.

## End-of-Life Thresholds

## Role of the End-of-Life Criterion

RUL cannot be labeled without first defining end-of-life. The end-of-life threshold specifies the point at which a battery is considered no longer suitable for its intended use according to the adopted study definition.

The threshold must be:

- explicit;
- reproducible;
- aligned with the dataset;
- reported in the methodology chapter.

## Common End-of-Life Thresholds

### 1. Capacity Retention Threshold

The most widely used threshold in battery prognostics is based on retained capacity.

Common example:

- end-of-life occurs when usable capacity falls below 80 percent of nominal capacity.

Advantages:

- widely used in battery prognostics literature;
- directly interpretable;
- suitable for many controlled aging datasets.

Limitations:

- not universally appropriate across all chemistries and applications;
- may not reflect safety-critical failure modes;
- may be difficult to apply when capacity is measured infrequently.

### 2. Internal Resistance Threshold

End-of-life may also be defined when internal resistance exceeds a specified limit.

Advantages:

- relevant to power fade and degraded performance;
- useful when resistance is more reliably measured than capacity.

Limitations:

- threshold selection may be less standardized;
- resistance measurements may be noisy or protocol-dependent.

### 3. Performance-Based Threshold

End-of-life may be defined using an application-driven performance limit, such as failure to sustain required power, energy, or vehicle operating range.

Advantages:

- closely aligned with real operational requirements;
- appropriate for pack-level or vehicle-level contexts.

Limitations:

- may be harder to standardize across studies;
- can depend heavily on operating context and duty cycle.

### 4. Multi-Criterion End-of-Life Definition

In some settings, end-of-life may be defined using more than one criterion, such as:

- low capacity retention;
- elevated internal resistance;
- inability to meet power demand.

Advantages:

- more realistic representation of operational degradation;
- less dependent on a single indicator.

Limitations:

- more difficult to label consistently;
- requires careful documentation of the decision rule.

## Recommended Default Threshold

Unless the dataset provides a clearly preferable alternative, the recommended default threshold is:

- end-of-life at 80 percent of nominal capacity.

This recommendation is methodological rather than universal. If the selected dataset or application context defines end-of-life differently, the dataset-specific criterion should take precedence.

## Cycle-Based and Time-Based RUL Labels

## Cycle-Based RUL

Cycle-based RUL expresses the label as the number of charge-discharge cycles remaining until end-of-life.

### Example

`target_rul = cycle_index_at_end_of_life - cycle_index_at_observation_end`

### Advantages

- naturally aligned with controlled battery aging experiments;
- easy to interpret in datasets with explicit cycle numbering;
- consistent with many published battery prognostics studies.

### Limitations

- may not reflect real-world usage heterogeneity;
- one cycle may vary substantially in depth of discharge, duration, and stress level;
- less suitable when the dataset does not contain reliable cycle boundaries.

## Time-Based RUL

Time-based RUL expresses the label as the remaining operating time until end-of-life.

### Example

`target_rul = time_at_end_of_life - time_at_observation_end`

### Advantages

- more suitable for irregular-use or field-operation datasets;
- directly interpretable when timestamps are more reliable than cycle definitions;
- potentially more relevant for vehicle-level deployment contexts.

### Limitations

- calendar time may be a weak representation of actual electrochemical usage;
- idle periods can distort apparent remaining life;
- time-to-end-of-life may depend heavily on usage regime rather than degradation state alone.

## Comparative Consideration

Cycle-based labels are generally preferable for laboratory aging datasets with structured cycling, whereas time-based labels are often more appropriate for operational datasets with irregular use patterns. The choice should be determined by the data-generating process rather than by modeling convenience alone.

## Alignment Between RUL Labels and Data Granularity

## General Principle

RUL labels must be aligned with the granularity of the observation unit used for modeling. Misalignment between label definition and data granularity can produce ambiguous or noisy supervisory signals.

## Recommended Alignment Rules

### 1. Cycle-Level Data

If one record corresponds to one complete charge-discharge cycle, then RUL should ideally be labeled in:

- cycles remaining.

This alignment is preferred because:

- the unit of observation and the unit of prediction are directly compatible;
- cycle-to-cycle degradation features are interpretable;
- label noise is reduced relative to finer-grained records.

### 2. Windowed Time-Series Data

If one record corresponds to a fixed-length time window or sliding observation window, then RUL may be labeled in:

- cycles remaining, if the cycle position of the window is known; or
- time remaining, if cycle definition is weak or unavailable.

The key requirement is that the label refers to the end of the observation window, not to an earlier internal point within the same window.

### 3. Partial-Cycle Segments

If one record corresponds to part of a cycle, then the labeling rule must specify whether RUL is measured from:

- the end of the segment;
- the end of the current cycle; or
- the nearest standardized cycle boundary.

The preferred choice is to label RUL from the **end of the segment**, provided this choice is applied consistently.

### 4. Vehicle-Level or Pack-Level Operational Logs

If the data are collected at the vehicle or pack level under irregular operating conditions, RUL should be aligned with:

- time remaining; or
- usage-unit remaining, such as energy throughput or cumulative equivalent cycles, if such measures are available and justified.

## Practical Issues in Labeling Partial-Cycle Data

## 1. Ambiguous Cycle Boundaries

Partial-cycle data may not have clear start and end points for a full operational cycle.

Implication:

- cycle-based RUL becomes difficult to define consistently.

Recommended response:

- either reconstruct cycle boundaries explicitly or adopt a time-based or equivalent-usage label.

## 2. Unequal Informational Content Across Segments

Different partial-cycle segments may contain different levels of degradation information.

Example:

- a charging segment may capture different behavior from a discharge segment of the same battery state.

Implication:

- two records with the same RUL may differ substantially in predictive informativeness.

Recommended response:

- document the segment type explicitly and consider including operating-mode metadata in the model inputs.

## 3. Label Instability Within a Single Cycle

If multiple windows are extracted within one cycle, the difference in RUL between adjacent windows may be negligible even though the measured signal behavior differs.

Implication:

- the dataset may contain many near-duplicate labels.

Recommended response:

- use a consistent windowing policy and evaluate whether dense overlap introduces redundancy or leakage.

## Practical Issues in Labeling Irregular-Use Data

## 1. Irregular Time Gaps

In field or operational data, long idle periods may separate active usage periods.

Implication:

- time-based RUL may overstate degradation progression if calendar time is used without considering actual usage.

Recommended response:

- consider usage-adjusted time or equivalent-cycle measures where justified.

## 2. Non-Uniform Usage Intensity

Some periods may involve mild operating stress, whereas others impose severe thermal or electrical loading.

Implication:

- the same amount of elapsed time may correspond to very different degradation effects.

Recommended response:

- interpret time-based RUL cautiously and include operating-condition variables in the feature set.

## 3. Incomplete Lifetime Observation

Some batteries may not be observed until end-of-life.

Implication:

- exact RUL labels cannot be assigned without extrapolation or censoring assumptions.

Recommended response:

- exclude such trajectories from standard supervised RUL training, or adopt a documented censored-data methodology.

## 4. Changing Operating Regimes

Vehicle usage, ambient conditions, and load patterns may change over time.

Implication:

- historical time-to-failure relationships may not remain stable.

Recommended response:

- record regime changes explicitly where possible and avoid assuming stationary degradation conditions.

## Label Construction Principles

All RUL labels in this project should satisfy the following principles:

1. The end-of-life criterion must be explicit and justified.
2. The label unit must match the data structure and prediction setting.
3. The label must be referenced to the end of the observation window.
4. The label must not require future information to enter the feature set.
5. Any approximation used for irregular or partial-cycle data must be documented as a methodological assumption.

## Recommended Reporting Items

The final methodology chapter should report:

1. the selected end-of-life criterion;
2. whether RUL is cycle-based or time-based;
3. the unit of analysis used for prediction;
4. the exact formula used to construct `target_rul`;
5. how partial cycles, irregular intervals, and incomplete trajectories were handled;
6. any limitations introduced by the labeling process.

## Conclusion

For this project, the preferred default is to define `target_rul` as a continuous cycle-based label derived from a documented end-of-life threshold, ideally based on capacity retention, when the dataset supports cycle-level degradation analysis. However, time-based or usage-adjusted labels may be more appropriate for irregular operational data. The central methodological requirement is that the RUL label must be explicitly aligned with the observation granularity, end-of-life definition, and practical limits of the available dataset.
