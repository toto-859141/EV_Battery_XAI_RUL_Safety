# Preprocessing Pipeline

## Purpose

This document proposes a preprocessing pipeline for time-series battery monitoring data used in:

- Remaining Useful Life prediction; and
- Safety Risk prediction.

The pipeline is designed for practical implementation while remaining suitable for description in a methodology chapter.

## Preprocessing Objectives

The preprocessing workflow should:

- preserve temporal order;
- produce reproducible observation windows;
- derive interpretable degradation and safety-related features;
- support both prediction tasks without conflating them; and
- minimize information leakage from future observations.

## Proposed Pipeline

### Step 1: Data Ingestion and Source Validation

Tasks:

- load raw files from `data/raw/`;
- verify file structure and encoding;
- record dataset version, source, and acquisition metadata;
- validate required fields such as battery identifier, timestamp, and core signals.

Output:

- source-validated raw tables.

### Step 2: Timestamp and Ordering Validation

Tasks:

- convert timestamps to a consistent datetime format;
- sort records by `battery_id` and time;
- check for duplicate timestamps within the same battery entity;
- verify monotonic order of cycle indices where provided.

Output:

- temporally ordered raw signal tables.

### Step 3: Data Quality Screening

Tasks:

- identify missing values in core signals;
- detect physically implausible values such as impossible voltage or temperature readings;
- identify sensor dropouts, flat-line signals, or extreme spikes;
- flag corrupted or incomplete cycles.

Output:

- quality-screened raw data with exclusion flags or correction logs.

### Step 4: Signal Cleaning

Tasks:

- apply dataset-appropriate handling of missing values;
- smooth obvious sensor noise only where justified;
- remove or flag severe outliers after documenting the rule;
- standardize sign conventions for current and operating state labels.

Output:

- cleaned monitoring signals.

### Step 5: Cycle or Window Segmentation

Tasks:

- segment the raw signals into the selected unit of analysis;
- assign `window_id` values;
- record window boundaries such as cycle start, cycle end, timestamp start, and timestamp end;
- ensure each window contains only past and current observations at the point of prediction.

Output:

- observation-window table linked to raw signals.

### Step 6: Feature Engineering

Tasks:

- compute descriptive statistics for voltage, current, and temperature;
- derive degradation-oriented features such as capacity fade or resistance proxies;
- derive safety-relevant features such as temperature excursion counts or instability measures;
- derive operating-condition features such as charge rate, discharge rate, or depth of discharge.

Output:

- feature table with one row per observation window.

### Step 7: Label Construction

Tasks:

- construct `target_rul` using the documented end-of-life rule;
- construct `target_eol` as an auxiliary label;
- construct `target_safety_risk` using direct labels, event-based rules, or justified proxy rules;
- validate label alignment with the observation window.

Output:

- target label table.

### Step 8: Feature Filtering and Selection

Tasks:

- remove identifiers and non-predictive fields from the model input set;
- identify redundant or highly collinear features where appropriate;
- retain physically interpretable features when possible;
- perform feature selection only within the training data split.

Output:

- model-ready feature set definition.

### Step 9: Scaling and Transformation

Tasks:

- standardize or normalize numeric features as required by the model family;
- fit transformation parameters using training data only;
- apply the learned transformation to validation and test data without refitting.

Output:

- transformed model-ready dataset.

### Step 10: Documentation and Export

Tasks:

- export processed features and labels to `data/processed/`;
- record preprocessing configuration, exclusions, and assumptions;
- version the output artifacts for reproducibility.

Output:

- documented processed dataset for model development.

## Recommended Feature Categories

The preprocessing pipeline should aim to produce at least the following categories of features:

- raw signal summary features;
- trend and variability features;
- degradation indicators;
- safety-related abnormality indicators;
- operating-condition features.

## Methodological Notes

### Separate Task Logic

The same preprocessing pipeline may serve both tasks, but:

- `target_rul` is a long-horizon prognostic label;
- `target_safety_risk` is a safety-oriented label that may be short-horizon or event-oriented.

Feature definitions and label windows should therefore be documented separately even when derived from the same raw signals.

### Interpretability Consideration

When two features are highly similar in information content, preference should be given to the more interpretable formulation, provided that predictive performance is not substantially degraded.
