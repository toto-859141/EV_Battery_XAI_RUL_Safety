# Advanced Models

## Purpose

This document recommends advanced model families suitable for time-series battery data in the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

These models are intended to extend the baseline experiments by capturing temporal structure, non-linear interactions, and cross-variable dependencies that may not be fully represented by static engineered features alone.

## Why Advanced Models Are Needed

Battery behavior is often:

- sequential;
- non-linear;
- sensitive to operating context;
- dependent on interactions between electrical, thermal, and degradation processes.

Advanced models may therefore provide improved predictive performance, especially when the available data include sufficiently rich temporal sequences.

## Recommended Advanced Models for Time-Series Battery Data

## 1. Gradient Boosting on Enhanced Feature Sets

Although not a sequence model, gradient boosting remains a strong advanced model for structured battery features.

Recommended variants:

- XGBoost;
- LightGBM;
- CatBoost.

### Appropriate Use

- engineered feature tables with one row per observation window;
- strong benchmark for tabular data;
- useful intermediate step before deep learning.

### Explainability Position

- moderate to strong practical explainability using SHAP;
- not inherently transparent, but often sufficiently interpretable for structured-feature analysis.

## 2. Recurrent Neural Networks

Recommended variants:

- LSTM;
- GRU.

### Appropriate Use

- sequential voltage-current-temperature windows;
- modeling degradation progression or temporal anomaly patterns.

### Strengths

- captures temporal dependencies;
- suitable for variable evolution over time.

### Limitations

- less interpretable than tabular models;
- can be harder to train and tune;
- explanation methods may be less stable.

## 3. Temporal Convolutional Networks

### Appropriate Use

- time-series windows where local temporal patterns are important;
- settings requiring efficient sequence modeling.

### Strengths

- captures temporal structure through convolutional filters;
- can be easier to optimize than recurrent models in some settings.

### Limitations

- interpretation of learned filters may still be limited;
- performance advantage depends on the structure of the signal.

## 4. Transformer-Based Time-Series Models

### Appropriate Use

- longer windows or complex multi-sensor sequences;
- settings where attention-based temporal dependency modeling is beneficial.

### Strengths

- flexible for long-range dependency modeling;
- can integrate multi-channel signals effectively.

### Limitations

- data-hungry;
- computationally heavier;
- attention weights should not automatically be treated as explanation.

## 5. Hybrid Models

### Description

Combine raw sequence encoders with engineered summary features.

Examples:

- LSTM plus engineered tabular feature branch;
- TCN plus degradation feature branch;
- transformer plus structured usage features.

### Appropriate Use

- when both sequence detail and interpretable engineered features are important;
- when the project seeks a balance between predictive performance and post hoc explanation.

### Strengths

- preserves fine-grained temporal information;
- retains access to interpretable engineered variables.

### Limitations

- more complex to train and analyze;
- explanation must account for multiple input pathways.

## 6. Multi-Input Classical-Deep Comparisons

### Description

Compare:

- tabular-feature-only models;
- sequence-only models;
- hybrid tabular-plus-sequence models.

### Purpose

- determine whether raw temporal signals truly add value beyond engineered features;
- avoid assuming that more complex models are necessarily superior.

## Recommended Advanced Model Set

The recommended advanced comparison set is:

### For `target_rul`

- gradient boosting regressor;
- LSTM or GRU sequence regressor;
- temporal convolutional regressor;
- hybrid sequence-plus-feature regressor.

### For `target_safety_risk`

- gradient boosting classifier;
- LSTM or GRU sequence classifier;
- temporal convolutional classifier;
- hybrid sequence-plus-feature classifier.

## Model Selection Guidance

The advanced model family should be selected based on:

- data volume;
- sequence length;
- feature reliability;
- interpretability needs;
- computational feasibility.

### If the dataset is small or moderate

Prefer:

- gradient boosting;
- simpler recurrent models;
- hybrid models with strong engineered features.

### If the dataset is large and richly sampled

Consider:

- temporal convolutional networks;
- transformer-based sequence models;
- multi-task neural architectures.

## Performance and Explainability Trade-Off

More advanced models may improve predictive performance by capturing richer temporal dynamics, but they typically reduce direct interpretability. In this project, such models should not be selected solely on predictive accuracy. They should also be assessed according to:

- whether explanations are stable and meaningful;
- whether the learned predictors align with technically plausible battery behavior;
- whether the performance improvement is substantial enough to justify increased complexity.

## Recommended Position

Advanced models should be treated as candidates for improvement rather than automatic replacements for interpretable baselines. The most credible final model may be a structured-feature model if it achieves competitive accuracy with stronger explainability, especially in a safety-relevant research setting.
