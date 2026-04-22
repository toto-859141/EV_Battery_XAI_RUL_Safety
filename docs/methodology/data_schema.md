# Data Schema

## Purpose

This document defines the proposed data structure for the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The schema is intended to guide dataset integration, preprocessing, feature extraction, target construction, and model development. Because the final dataset has not yet been selected, the schema is specified as a methodological design that can be adapted to public, experimental, or institutional battery-monitoring datasets.

## Proposed Unit of Analysis

The recommended unit of analysis is the **battery observation window**, defined as a fixed analysis segment for a single battery entity over a bounded time or cycle interval.

This design is recommended because it supports:

- time-dependent feature extraction from voltage, current, and temperature signals;
- alignment of monitoring data with both prognostic and safety-oriented targets;
- compatibility with cell-level, module-level, pack-level, or vehicle-level datasets; and
- interpretable mapping between observed behavior and model predictions.

## Operational Form of the Unit of Analysis

The observation window should be defined using one of the following, depending on dataset structure:

- one complete charge-discharge cycle;
- a partial cycle segment with fixed duration;
- a fixed-length sliding time window;
- a fixed-length sliding cycle window.

### Recommended Default

If the dataset supports cycle-based analysis, a **cycle-level or short rolling multi-cycle window** is the preferred default because:

- RUL is often defined relative to cycle progression;
- degradation features are usually easier to interpret at this level; and
- safety-relevant anomalies can still be summarized within the same window.

## Entity Hierarchy

The schema should preserve the distinction between the monitored entity and the observation window.

### Entity Levels

- `battery_id`: unique identifier for the monitored battery unit
- `battery_level`: one of `cell`, `module`, `pack`, or `vehicle`
- `dataset_id`: identifier for the dataset source

### Observation-Level Keys

- `window_id`: unique identifier for the observation window
- `cycle_index_start`
- `cycle_index_end`
- `timestamp_start`
- `timestamp_end`

## Expected Raw Data Structure

The expected raw data structure is a time-series table or collection of files containing repeated measurements from battery monitoring systems.

### Minimum Expected Fields

| Field name | Description | Expected type |
| --- | --- | --- |
| `dataset_id` | Dataset source identifier | categorical |
| `battery_id` | Unique battery identifier | categorical |
| `battery_level` | Cell, module, pack, or vehicle | categorical |
| `timestamp` | Measurement time | datetime |
| `cycle_index` | Charge-discharge cycle number, where available | integer |
| `voltage` | Terminal voltage measurement | numeric |
| `current` | Current measurement | numeric |
| `temperature` | Surface or internal temperature, where available | numeric |
| `capacity` | Capacity measurement, where available | numeric |
| `state_of_charge` | State of charge, where available | numeric |
| `operating_mode` | Charge, discharge, rest, or drive state | categorical |

## Optional Raw Fields

The following fields are desirable but not mandatory:

- `internal_resistance`
- `ambient_temperature`
- `depth_of_discharge`
- `charge_rate`
- `discharge_rate`
- `power`
- `energy_throughput`
- `vehicle_speed` or load-related variables at vehicle level
- fault or warning-event indicators
- test protocol metadata

## Proposed Processed Data Layers

The data schema should be organized into three analytical layers.

### Layer 1: Raw Time-Series Layer

This layer stores original monitoring signals without irreversible transformation.

Example contents:

- timestamped voltage measurements;
- timestamped current measurements;
- timestamped temperature measurements;
- cycle metadata.

### Layer 2: Windowed Feature Layer

This layer stores engineered features for each observation window.

Example contents:

- summary statistics of voltage, current, and temperature;
- degradation indicators such as capacity fade and resistance growth proxies;
- safety-relevant indicators such as temperature excursions and voltage instability;
- operating-condition variables.

### Layer 3: Target Label Layer

This layer stores the dependent variables and auxiliary labels associated with each observation window.

Example contents:

- `target_rul`
- `target_eol`
- `target_safety_risk`
- target-definition metadata

## Relational Structure

The proposed analytical schema can be represented as follows:

1. `raw_measurements`
   - one row per timestamped measurement
2. `window_features`
   - one row per battery observation window
3. `window_targets`
   - one row per battery observation window
4. `battery_metadata`
   - one row per battery entity

### Join Keys

- `dataset_id`
- `battery_id`
- `window_id`

## Example Analytical Record

One processed row in the feature table may represent:

- one battery cell;
- cycles 120 to 124;
- summary and derived features computed only from signals available up to cycle 124; and
- labels such as `target_rul = 80 cycles remaining` and `target_safety_risk = medium`.

## Methodological Note

The schema is designed to prevent conceptual confusion between:

- raw signals, which are measured directly;
- engineered features, which are derived from the signals;
- battery health, which is an inferred construct;
- `target_rul`, which is a prognostic outcome; and
- `target_safety_risk`, which is a safety-oriented outcome.

This separation is important for model transparency and for preventing ambiguity in later explainability analysis.
