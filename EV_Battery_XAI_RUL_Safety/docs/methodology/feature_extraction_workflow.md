# Feature Extraction Workflow

## Purpose

This document provides a practical workflow for extracting modeling features from raw time-series battery data for the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The workflow is intended to support implementation and documentation for both:

- classical machine learning based on engineered tabular features; and
- deep learning workflows that may combine raw sequences with engineered summary variables.

The workflow assumes that the unit of analysis is a battery observation window, as defined in the broader methodology package.

## Workflow Objectives

The feature extraction workflow should:

- preserve temporal validity;
- ensure that features use only data available up to the end of the observation window;
- support both `target_rul` and `target_safety_risk`;
- produce interpretable indicators suitable for explainable analysis;
- export feature tables in reproducible formats;
- record feature provenance so that every derived variable can be traced back to source data and transformation logic.

## Recommended Order of Feature Extraction

The recommended order is:

1. ingest and validate raw data;
2. standardize timestamps, identifiers, and operating-mode labels;
3. screen and clean the raw signal streams;
4. segment the data into cycles or observation windows;
5. compute baseline descriptive signal summaries;
6. derive interpretable electrical and thermal indicators;
7. derive degradation indicators;
8. derive operational usage pattern features;
9. assemble the final feature table;
10. validate, save, and document the extracted features.

This order is recommended because later feature groups depend on earlier steps being stable and correctly aligned with the observation window.

## Step 1: Ingest and Validate Raw Time-Series Data

### Inputs

Raw files from `data/raw/`, expected to contain at least:

- `battery_id`
- `timestamp`
- voltage
- current
- temperature, where available
- cycle index, where available

### Tasks

- load the raw files into a structured tabular format;
- verify encoding, schema, and required fields;
- confirm that each row is associated with a valid battery entity;
- record dataset source and version information.

### Output

- raw signal tables with verified identifiers and metadata.

## Step 2: Standardize Time and Signal Conventions

### Tasks

- convert timestamps to a consistent datetime format;
- sort data by `battery_id` and timestamp;
- standardize current sign conventions;
- standardize operating-mode labels such as `charge`, `discharge`, and `rest`;
- verify monotonic cycle progression where cycle indices are available.

### Output

- ordered and convention-consistent time-series data.

## Step 3: Screen and Clean Raw Signals

### Tasks

- identify missing values in voltage, current, temperature, and capacity-related records;
- detect physically implausible values;
- identify flat-line sensor failures, spikes, or repeated duplicate records;
- apply documented cleaning rules such as exclusion, interpolation, or flagging.

### Implementation Note

Cleaning should be conservative. Signal smoothing or interpolation should only be applied when justified and documented, particularly in safety-oriented analyses where abnormal spikes may be meaningful.

### Output

- cleaned raw signals with data-quality flags.

## Step 4: Handle Cycle Segmentation

## General Principle

Feature extraction should be performed only after the raw data have been aligned to a consistent unit of analysis. In battery studies, this usually requires cycle segmentation or fixed-window construction.

## Preferred Segmentation Strategy

### Option A: Full-Cycle Segmentation

Use one full charge-discharge cycle as the observation unit when:

- cycle boundaries are available or reconstructable;
- the dataset is a controlled aging dataset;
- degradation-oriented modeling is the main priority.

### Option B: Fixed-Length Time Window Segmentation

Use fixed time windows when:

- cycle boundaries are weak or unavailable;
- the dataset is operational or irregular-use data;
- short-horizon safety monitoring is a major objective.

### Option C: Rolling Multi-Cycle Windows

Use rolling windows across multiple recent cycles when:

- short-term signal instability and long-term degradation both need to be represented;
- richer context is needed for feature construction.

## Cycle Segmentation Tasks

- define the segmentation rule explicitly;
- assign a unique `window_id` to each segment;
- record `timestamp_start`, `timestamp_end`, `cycle_index_start`, and `cycle_index_end`;
- ensure that overlapping windows are documented and controlled to avoid downstream leakage.

## Practical Guidance

- if cycles are incomplete, either mark the segment as partial or exclude it according to the study rule;
- if the same raw interval contributes to multiple overlapping windows, record the overlap policy explicitly;
- if the data are irregular-use logs, document why a time-window strategy was chosen instead of full-cycle segmentation.

### Output

- a segmented window table that defines the exact extraction boundary for each observation.

## Step 5: Compute Baseline Descriptive Features

These features should be extracted first because they serve as the foundation for both interpretability and more advanced engineered indicators.

### Electrical Summaries

Examples:

- mean voltage;
- minimum voltage;
- maximum voltage;
- voltage range;
- mean current;
- maximum absolute current;
- current standard deviation;
- mean power.

### Thermal Summaries

Examples:

- mean temperature;
- maximum temperature;
- temperature range;
- temperature standard deviation.

### Output

- baseline signal summary features for each observation window.

## Step 6: Derive Interpretable Electrical and Thermal Indicators

After baseline summaries are available, derive indicators that capture dynamic behavior and potential abnormality.

### Electrical Indicators

Examples:

- voltage slope;
- voltage recovery magnitude;
- current spike count;
- voltage-current consistency indicator;
- power variability.

### Thermal Indicators

Examples:

- temperature rise rate;
- temperature excursion count;
- thermal recovery time;
- temperature-current coupling index;
- thermal gradient, where multiple sensors exist.

### Implementation Principle

Each derived indicator should have:

- a precise formula;
- a clearly stated observation boundary;
- a stated rationale for inclusion.

### Output

- interpretable electrical and thermal indicator set.

## Step 7: Derive Degradation Indicators

These features are especially important for RUL prediction but may also inform safety-related analysis when degradation and instability interact.

### Candidate Degradation Indicators

- capacity retention;
- capacity fade rate;
- internal resistance or resistance proxy;
- resistance growth rate;
- coulombic efficiency;
- energy efficiency;
- equivalent full cycle count;
- cycle-to-cycle degradation change;
- voltage curve summary descriptors.

### Practical Guidance

- degradation indicators should be computed using historical information available up to the current window only;
- if a feature depends on recent history, define the look-back span explicitly;
- avoid features that directly encode end-of-life timing or future failure information.

### Output

- degradation-oriented feature set aligned to each observation window.

## Step 8: Derive Operational Usage Pattern Features

These features capture how the battery is being used, which is important for contextualizing both degradation and safety risk.

### Candidate Usage Features

- charge duration;
- discharge duration;
- rest duration;
- depth of discharge;
- charge rate;
- discharge rate;
- energy throughput;
- charge throughput;
- high-stress operation frequency;
- high-rate charging fraction;
- high-load discharge fraction;
- usage irregularity index.

### Output

- operational context feature set for each observation window.

## Step 9: Assemble the Final Feature Table

### Tasks

- merge feature groups using `dataset_id`, `battery_id`, and `window_id`;
- verify one row per observation window;
- confirm that feature names are unique and documented;
- separate engineered features from identifiers and metadata.

### Recommended Table Structure

Each row should correspond to one observation window and include:

- identifiers;
- segmentation metadata;
- engineered features;
- optional quality flags.

### Output

- unified feature table ready for target merge and downstream modeling.

## Step 10: Validate the Feature Table

### Validation Checks

- confirm no duplicate `window_id` rows;
- check missingness by feature;
- check plausible value ranges;
- confirm no feature uses future observations;
- inspect correlations to identify unexpected redundancy or data issues;
- verify that safety proxy features do not trivially duplicate the safety label rule.

### Output

- validated feature table with extraction-quality checks completed.

## Saving Features for Modeling

## Recommended Storage Outputs

The workflow should save at least three outputs:

### 1. Feature Table

Suggested location:

- `data/processed/<datasetname>_features_v01.parquet`

Purpose:

- model-ready engineered features.

### 2. Feature Metadata Table

Suggested location:

- `data/processed/<datasetname>_feature_metadata_v01.csv`

Purpose:

- variable names, categories, formulas, units, and interpretability notes.

### 3. Extraction Run Configuration

Suggested location:

- `data/processed/<datasetname>_feature_config_v01.yaml`

Purpose:

- extraction parameters, segmentation settings, thresholds, smoothing rules, and version information.

## Recommended File Format

- use `parquet` for main feature tables when possible;
- use `csv` for human-readable metadata or small supporting tables;
- use `yaml` or `json` for extraction configuration and provenance records.

## Documenting Feature Provenance for Reproducibility

## Purpose of Provenance Tracking

Feature provenance documentation ensures that each engineered variable can be traced to:

- the raw data source;
- the segmentation rule used;
- the transformation logic applied;
- the extraction configuration version.

This is essential for reproducibility, error checking, and later explainability analysis.

## Minimum Provenance Elements

For each extracted feature, record:

- `feature_name`
- `feature_group`
- source raw variables
- formula or transformation description
- observation window definition
- any threshold or parameter values
- software or script version
- date of extraction
- dataset version

## Recommended Provenance Table Fields

| Field | Description |
| --- | --- |
| `feature_name` | Final variable name used in modeling |
| `feature_group` | Electrical, thermal, degradation, operational, or safety-derived |
| `raw_inputs` | Raw variables used to compute the feature |
| `window_rule` | Cycle, time window, or rolling window definition |
| `formula_summary` | Human-readable description of the computation |
| `parameters` | Thresholds, smoothing settings, or look-back values |
| `script_name` | Script or module used for extraction |
| `script_version` | Version tag, commit reference, or run identifier |
| `dataset_version` | Version of the raw or cleaned dataset used |
| `generated_at` | Extraction date and time |

## Recommended Documentation Practices

1. Maintain a feature metadata file alongside the saved feature table.
2. Version feature tables whenever formulas or thresholds change.
3. Record any dropped windows or excluded cycles during extraction.
4. Keep extraction logs separate from model-training logs.
5. Ensure that feature provenance is updated before experiments are run.

## Implementation Summary

The recommended implementation sequence is:

1. load and validate raw battery signals;
2. standardize timestamps and operating conventions;
3. clean and quality-screen the signals;
4. segment the data into cycles or observation windows;
5. compute baseline summaries;
6. derive interpretable electrical and thermal indicators;
7. derive degradation indicators;
8. derive operational usage features;
9. assemble and validate the final feature table;
10. save the outputs and record feature provenance.

## Final Note

This workflow should be implemented in a way that preserves traceability from raw battery signals to final model inputs. In this project, feature extraction is not only a technical preprocessing step; it is also part of the methodological foundation for interpretable prediction of remaining useful life and safety risk.
