# Data Dictionary Template

## Purpose

This template provides a structured format for documenting variables used in the project dataset. It should be completed after the final dataset and preprocessing design are confirmed.

The data dictionary should include variables from:

- raw monitoring data;
- engineered feature tables;
- metadata tables; and
- target label tables.

## Instructions for Use

1. Record one variable per row.
2. Use the same variable names as those used in code and processed datasets.
3. Clearly distinguish measured variables from derived variables.
4. State units explicitly.
5. Record whether the variable is used as:
   - input feature;
   - control variable;
   - auxiliary variable; or
   - target label.

## Data Dictionary Table

| Variable Name | Layer | Description | Data Type | Unit | Allowed Values or Range | Source | Derived or Raw | Role in Analysis | Missing Data Handling | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `battery_id` | metadata | Unique battery identifier | categorical | not applicable | dataset-specific | source metadata | raw | grouping key | not allowed to be missing | one identifier per monitored entity |
| `timestamp` | raw | Measurement timestamp | datetime | not applicable | valid datetime | sensor log | raw | ordering variable | rows with invalid timestamps removed or corrected | used for temporal ordering |
| `voltage` | raw | Terminal voltage measurement | numeric | V | dataset-specific | sensor log | raw | input feature | impute or exclude according to preprocessing protocol | verify sensor calibration |
| `current` | raw | Current measurement | numeric | A | dataset-specific | sensor log | raw | input feature | impute or exclude according to preprocessing protocol | sign convention must be documented |
| `temperature` | raw | Battery temperature measurement | numeric | degrees C | dataset-specific | sensor log | raw | input feature | impute or exclude according to preprocessing protocol | specify sensor location where known |
| `target_rul` | target | Remaining useful life label | numeric | cycles or time unit | non-negative | derived from label protocol | derived | dependent variable | not imputed; rows excluded if unavailable | must match end-of-life definition |
| `target_safety_risk` | target | Safety risk label | categorical or numeric | not applicable or score unit | study-specific | direct label or proxy rule | derived | dependent variable | not imputed; rows excluded if unavailable | must document label logic |

## Column Guidance

### Variable Name

Use the final canonical variable name used in the processed dataset.

### Layer

Recommended values:

- `metadata`
- `raw`
- `feature`
- `target`

### Description

Provide a concise but precise description of what the variable represents.

### Data Type

Examples:

- `numeric`
- `integer`
- `categorical`
- `datetime`
- `boolean`

### Unit

Examples:

- `V`
- `A`
- `degrees C`
- `Ah`
- `cycles`
- `seconds`

If no physical unit applies, use:

- `not applicable`

### Allowed Values or Range

Record accepted categories or plausible numeric bounds where known.

### Source

Examples:

- `sensor log`
- `battery management system`
- `laboratory metadata`
- `derived from preprocessing`

### Derived or Raw

Use one of:

- `raw`
- `derived`

### Role in Analysis

Examples:

- `input feature`
- `control variable`
- `grouping key`
- `dependent variable`
- `auxiliary label`

### Missing Data Handling

Document the rule applied if values are missing.

Examples:

- `forward fill within window`
- `interpolate within cycle`
- `exclude row`
- `not imputed`

### Notes

Use this column for critical contextual detail, such as:

- sign conventions;
- sensor location;
- normalization assumptions;
- whether the variable is dataset-specific.

## Recommended Variable Groups

The completed data dictionary should usually include the following groups:

- identifiers and metadata;
- raw battery monitoring signals;
- operating-condition variables;
- engineered degradation features;
- engineered safety-relevant features;
- target labels and auxiliary labels.
