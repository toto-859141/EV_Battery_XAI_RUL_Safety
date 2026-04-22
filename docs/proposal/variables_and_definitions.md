# Variables and Definitions

> Revision summary: This version sharpens the operational definitions, separates conceptual constructs from measurable variables, and aligns variable categories directly with the objectives and hypotheses.

## Overview

This document defines the constructs and variables used in the proposed study. Because the final dataset has not yet been selected, the operational forms below are preliminary and must be finalized once the data source and label structure are confirmed.

## Conceptual Constructs

### Battery Health

Battery health is a latent condition construct representing the extent to which a battery retains expected performance relative to its nominal state. In this study, battery health is not treated as the primary dependent variable. Instead, it is inferred through measurable predictors such as capacity-related, resistance-related, and efficiency-related degradation indicators.

### Safety Risk

Safety risk is a task-specific outcome construct representing the likelihood, severity, or presence of unsafe or abnormal battery conditions. In this study, safety risk is modeled explicitly as a dependent variable rather than treated as interchangeable with battery health.

### Remaining Useful Life

Remaining useful life is a prognostic outcome construct representing the amount of service remaining before the battery reaches a defined end-of-life criterion.

## Dependent Variables

### 1. `target_rul`

Definition:
The supervised learning target representing remaining useful life.

Likely operational form:

- continuous regression target measured in cycles remaining, time remaining, or an equivalent service-life unit.

Role in the study:
Primary dependent variable for the prognostic task.

### 2. `target_safety_risk`

Definition:
The supervised learning target representing safety-related risk.

Likely operational form:

- binary class;
- ordinal risk level; or
- continuous risk score.

Role in the study:
Primary dependent variable for the safety-oriented task.

### 3. `target_eol`

Definition:
A binary indicator of whether the end-of-life threshold has been reached.

Role in the study:
Auxiliary variable for defining or validating `target_rul`, not a substitute for `target_rul`.

## Independent Variables

Independent variables are the predictors used in model training. They are grouped below so they can be mapped directly to feature engineering and hypothesis testing.

### A. Monitored Battery Variables

- terminal voltage;
- current;
- surface or internal temperature, where available;
- cycle index or elapsed time;
- charge duration;
- discharge duration.

### B. Engineered Degradation Features

- capacity retention or capacity fade;
- internal resistance or resistance-growth proxies;
- energy throughput;
- coulombic efficiency, where available;
- cycle-to-cycle change statistics;
- voltage-curve summary statistics.

### C. Engineered Safety-Relevant Features

- temperature excursion indicators;
- temperature variability statistics;
- abnormal voltage deviation indicators;
- current instability indicators;
- combined operating-stress indicators derived from voltage, current, and temperature.

### D. Operating-Condition Variables

- charging rate;
- discharging rate;
- depth of discharge;
- ambient temperature, where available;
- test-condition metadata relevant to load or protocol.

## Control Variables

Control variables are included to reduce confounding and to ensure fair model comparison.

- battery chemistry;
- cell or pack type;
- dataset source;
- experimental or cycling protocol;
- train, validation, and test split strategy;
- sampling frequency or observation-window length;
- normalization, filtering, and preprocessing settings.

## Operational Assumptions

### End-of-Life Criterion

Assumption:
If the chosen dataset does not define end-of-life explicitly, `target_eol` and `target_rul` may be derived using a documented threshold such as capacity falling below 80 percent of nominal value. This threshold must be justified in the final methodology.

### Safety Risk Encoding

Assumption:
If direct safety labels are unavailable, `target_safety_risk` may be constructed from a documented proxy based on abnormal thermal, electrical, or operating behavior. If this approach is used, the proxy definition must be reported as a methodological limitation rather than treated as a direct observation of hazard.

## Variable Alignment Table

| Variable or construct | Type | Function in study | Likely measurement form |
| --- | --- | --- | --- |
| Battery health | Conceptual construct | Interpreted through predictors, not modeled as the main outcome | latent construct inferred from degradation indicators |
| `target_rul` | Dependent variable | Outcome for prognostic modeling | continuous service-life value |
| `target_safety_risk` | Dependent variable | Outcome for safety-oriented modeling | binary, ordinal, or continuous score |
| `target_eol` | Auxiliary dependent variable | End-of-life reference for RUL construction | binary indicator |
| Monitored battery variables | Independent variables | Core input signals for both tasks | time-series values or aggregated summaries |
| Engineered degradation features | Independent variables | Task-relevant predictors for degradation and RUL | derived numeric features |
| Engineered safety-relevant features | Independent variables | Task-relevant predictors for safety risk | derived numeric features |
| Operating-condition variables | Independent variables | Contextual predictors affecting both tasks | numeric or categorical variables |
| Chemistry, protocol, preprocessing, split settings | Control variables | Confound control and reproducibility | categorical metadata or fixed configuration |
