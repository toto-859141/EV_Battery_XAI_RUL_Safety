# Feature Engineering Plan

## Purpose

This document defines the proposed feature-engineering plan for the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The plan is designed to support both:

- classical machine learning workflows based on engineered tabular features; and
- deep learning workflows that may combine raw sequences with structured summary features.

The guiding principle is that features should be technically meaningful, aligned with the observation window, and interpretable wherever possible.

## Feature Engineering Objectives

The feature-engineering process should:

- capture battery behavior visible in voltage, current, and temperature signals;
- represent both long-term degradation and short-term abnormality;
- support `target_rul` and `target_safety_risk` as distinct prediction tasks;
- preserve compatibility with explainable AI analysis;
- remain adaptable to cell-, module-, pack-, or vehicle-level data.

## Proposed Feature Groups

The proposed feature set is organized into four core groups:

1. electrical behavior features;
2. thermal behavior features;
3. degradation indicator features;
4. operational usage pattern features.

These four groups are recommended because they map naturally onto the main research constructs:

- degradation-related features are expected to be particularly relevant for RUL;
- thermal and abnormal electrical features are expected to be particularly relevant for safety risk;
- operational patterns provide contextual information that may influence both tasks.

## Group 1: Electrical Behavior Features

### Purpose

Electrical behavior features summarize the observable electrical response of the battery within an observation window.

### Candidate Features

- mean voltage;
- minimum voltage;
- maximum voltage;
- voltage range;
- voltage slope during charge or discharge;
- mean current;
- peak current;
- current variability;
- current spike count;
- voltage-current consistency indicators.

### Expected Relevance

- strong relevance for safety risk when abnormal electrical behavior occurs;
- moderate to strong relevance for RUL when electrical behavior reflects degradation progression.

## Group 2: Thermal Behavior Features

### Purpose

Thermal behavior features summarize battery heating patterns, temperature stability, and thermal excursions.

### Candidate Features

- mean temperature;
- maximum temperature;
- temperature range;
- temperature rise rate;
- temperature variance;
- temperature excursion count;
- temperature recovery time;
- thermal gradient, where multiple sensors are available.

### Expected Relevance

- strong relevance for safety risk because abnormal heating is closely associated with hazardous conditions;
- moderate relevance for RUL because persistent thermal stress may accelerate degradation.

## Group 3: Degradation Indicator Features

### Purpose

Degradation indicator features summarize long-term loss of battery capability or changes in electrochemical response.

### Candidate Features

- capacity retention;
- capacity fade rate;
- internal resistance or resistance proxy;
- coulombic efficiency;
- energy efficiency;
- incremental cycle-to-cycle degradation rate;
- voltage curve summary descriptors;
- equivalent full cycle count, where available.

### Expected Relevance

- very strong relevance for RUL prediction;
- indirect but meaningful relevance for safety risk when degradation interacts with thermal or electrical stress.

## Group 4: Operational Usage Pattern Features

### Purpose

Operational usage pattern features represent how the battery is being used, rather than only how it responds internally.

### Candidate Features

- charge duration;
- discharge duration;
- depth of discharge;
- charge rate;
- discharge rate;
- cumulative energy throughput;
- rest duration between cycles;
- frequency of high-load or high-rate operation.

### Expected Relevance

- relevant to both tasks because usage stress affects degradation progression and may elevate safety-related abnormality risk.

## Feature Levels for Different Modeling Workflows

## A. Classical Machine Learning Workflow

For classical machine learning, the preferred approach is to use an explicit feature table with one row per observation window and one column per engineered feature.

Recommended models:

- linear models;
- random forest;
- gradient boosting;
- support vector machines;
- explainable tree-based models.

Advantages:

- strong compatibility with feature attribution and post hoc XAI;
- easier physical interpretation;
- more transparent feature auditing.

## B. Deep Learning Workflow

For deep learning, two feature-design strategies are recommended.

### Strategy 1: Raw Sequence Modeling

Use the raw or lightly processed signal sequence directly as input.

Examples:

- voltage sequence;
- current sequence;
- temperature sequence.

Recommended models:

- LSTM;
- temporal convolutional networks;
- transformer-based time-series models.

### Strategy 2: Hybrid Modeling

Combine raw sequences with engineered summary features.

Rationale:

- raw sequences preserve fine-grained temporal information;
- engineered features preserve interpretability and physical meaning.

This hybrid strategy is recommended when both predictive performance and explainability are important.

## Recommended Design Principle

The project should maintain two parallel feature views where feasible:

1. an interpretable engineered feature set for transparent analysis and classical ML;
2. a sequence-oriented representation for deep learning experiments.

This approach enables methodological comparison without forcing a single representation on all models.

## Feature Engineering Principles

All engineered features should satisfy the following principles:

1. The feature must be computed using only data available up to the end of the observation window.
2. The feature definition must be explicit and reproducible.
3. The feature should have a clear physical, operational, or statistical interpretation.
4. The feature should be assigned a plausible task role:
   - RUL
   - safety risk
   - both
5. Highly redundant features should be documented and reviewed before model fitting.

## Recommended Workflow

The feature-engineering workflow should proceed as follows:

1. define the observation window;
2. compute baseline descriptive features;
3. add degradation indicator features;
4. add safety-relevant abnormality features;
5. add operational usage context features;
6. review interpretability and redundancy;
7. create task-ready feature subsets for RUL and safety experiments.

## Link to Companion Documents

The detailed feature descriptions are provided in:

- `interpretable_features.md`
- `feature_grouping_table.md`
- `feature_selection_strategy.md`
