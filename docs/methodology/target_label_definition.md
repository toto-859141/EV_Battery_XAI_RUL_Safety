# Target Label Definition

## Purpose

This document defines the proposed target-label logic for the two main prediction tasks in the project:

- Remaining Useful Life (`target_rul`)
- Safety Risk (`target_safety_risk`)

An auxiliary target, `target_eol`, is also defined because it supports the derivation and validation of `target_rul`.

## Conceptual Distinction

The labels should be defined so that the following concepts remain separate:

- `battery health`: inferred battery condition reflected by degradation indicators;
- `target_rul`: remaining service life before end-of-life;
- `target_safety_risk`: level of safety-related concern associated with the observed battery state.

The study should not treat these as interchangeable labels.

## 1. Remaining Useful Life (`target_rul`)

### Definition

`target_rul` is the amount of usable service remaining from the end of the observation window until the battery reaches the defined end-of-life threshold.

### Recommended Label Form

The preferred form is a **continuous regression label** expressed as:

- cycles remaining; or
- time remaining, if the dataset is time-indexed rather than cycle-indexed.

### Recommended Default Definition

If the dataset supports cycle-based degradation analysis, define:

`target_rul = cycle_index_at_end_of_life - cycle_index_at_observation_end`

### End-of-Life Criterion

The end-of-life criterion must be documented explicitly. A common default assumption is:

- end-of-life occurs when usable capacity falls below 80 percent of nominal capacity.

This threshold should not be treated as universal. If the dataset defines end-of-life differently, the dataset-specific definition should take precedence.

### Constraints

- `target_rul` must be non-negative.
- `target_rul` must be computed using only information available after the battery’s full lifecycle is known for label construction, but such future information must not leak into features.
- Rows for which end-of-life cannot be determined should be excluded from supervised RUL training or treated using a documented censored-data strategy.

## 2. End-of-Life Indicator (`target_eol`)

### Definition

`target_eol` is a binary auxiliary label indicating whether the battery has reached the chosen end-of-life threshold at or before the observation point.

### Recommended Form

- `1` if end-of-life has been reached
- `0` otherwise

### Role in Analysis

`target_eol` should be used:

- to validate the end-of-life rule;
- to support descriptive analysis;
- to assist in constructing `target_rul`.

It should not replace `target_rul` unless the project explicitly reframes the prognostic task as an end-of-life classification problem.

## 3. Safety Risk (`target_safety_risk`)

### Definition

`target_safety_risk` is the label representing the degree of safety-related concern associated with a battery observation window.

### Recommended Label Strategy

The preferred priority order is:

1. direct safety label from the dataset;
2. documented event-based label;
3. justified proxy label derived from battery behavior.

### Option A: Direct Safety Label

If the dataset includes direct annotations such as:

- fault state;
- abnormal operating state;
- thermal runaway event;
- warning status;

then these annotations should be used directly, subject to validation of label quality.

### Option B: Event-Based Safety Label

If direct labels are unavailable but event timing is known, define safety risk using a prediction window before the event.

Example:

- `high risk` for windows occurring within a predefined lead time before a safety-relevant event;
- `low risk` for windows sufficiently far from such events.

### Option C: Proxy Safety Label

If neither direct labels nor event markers exist, construct a documented proxy using theoretically justified indicators such as:

- abnormal temperature excursions;
- unstable voltage behavior;
- current irregularity;
- combined operating-stress conditions;
- abrupt changes in degradation behavior.

If a proxy label is used, the methodology chapter must state clearly that:

- the label represents inferred safety risk rather than observed hazard;
- the proxy rules are study assumptions;
- conclusions about real-world hazard should be made cautiously.

## Recommended Safety Label Forms

Depending on data quality and project scope, `target_safety_risk` may be encoded as:

- binary classification: `low risk` vs `high risk`;
- ordinal classification: `low`, `medium`, `high`;
- continuous risk score.

### Recommended Default

For early modeling and interpretability, an **ordinal or binary classification label** is recommended because:

- it is easier to audit and explain;
- it aligns with safety-oriented decision support;
- it avoids overstating precision when labels are uncertain.

## Label Table Summary

| Label | Type | Recommended form | Primary use |
| --- | --- | --- | --- |
| `target_rul` | dependent variable | continuous regression | prognostic prediction |
| `target_eol` | auxiliary variable | binary | end-of-life rule support |
| `target_safety_risk` | dependent variable | binary or ordinal classification by default | safety-oriented prediction |

## Labeling Principles

All target labels should satisfy the following principles:

1. The label definition must be explicit and reproducible.
2. The label must align with the observation window.
3. The label must not require features computed from future observations beyond the window.
4. The difference between direct labels and proxy labels must be documented.
5. The final label logic must be recorded in the experiment documentation.
