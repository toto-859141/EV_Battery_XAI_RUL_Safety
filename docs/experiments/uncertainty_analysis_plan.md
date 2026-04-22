# Uncertainty Analysis Plan

## Purpose

This document proposes an uncertainty analysis plan for the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The purpose of uncertainty analysis is to evaluate whether model predictions are accompanied by useful indications of confidence or instability, especially in settings where decisions may be safety-relevant.

## Why Uncertainty Matters

In this project, uncertainty analysis is important because:

- RUL predictions may be more difficult in late-life or under changing usage regimes;
- safety-risk predictions may be unreliable when labels are sparse or proxy-based;
- high-confidence errors may be especially problematic in safety-critical monitoring.

## Recommended Uncertainty Types

## 1. Predictive Uncertainty

Represents uncertainty in the predicted output itself.

Examples:

- uncertainty interval around predicted RUL;
- confidence score or calibrated probability for safety-risk classification.

## 2. Model Uncertainty

Represents uncertainty arising from model instability or parameter uncertainty.

Examples:

- variation across ensembles;
- variation across repeated runs with different seeds.

## 3. Data Uncertainty

Represents ambiguity or noise arising from the data-generating process.

Examples:

- noisy thermal measurements;
- incomplete end-of-life observation;
- uncertain safety proxy labels.

## Recommended Methods

## For RUL Regression

Recommended methods include:

- ensemble-based prediction intervals;
- quantile regression;
- bootstrap resampling;
- repeated-seed model variation.

### Recommended Use

Report:

- central prediction;
- interval width or uncertainty band;
- whether uncertainty grows near end-of-life or under difficult regimes.

## For Safety Risk Classification

Recommended methods include:

- probability calibration analysis;
- predictive entropy for probabilistic models;
- ensemble disagreement;
- bootstrap confidence intervals on classification metrics.

### Recommended Use

Report:

- predicted class;
- associated confidence or probability;
- calibration quality;
- disagreement or instability across repeated runs where feasible.

## Calibration Analysis

Calibration should be examined especially for safety-risk models that output class probabilities.

Recommended analyses:

- reliability diagrams;
- calibration error measures;
- threshold sensitivity review.

Why this matters:

- a model that is accurate but poorly calibrated may still be unsafe as a decision-support tool.

## Uncertainty in Safety-Critical Interpretation

Predictions with:

- high uncertainty;
- low confidence;
- strong model disagreement;

should be treated differently from high-confidence predictions.

Recommended interpretation:

- uncertainty should increase caution, not automatically suppress warning consideration;
- highly uncertain high-risk predictions may still warrant review, especially if explanation patterns are plausible;
- highly confident but incorrect predictions should be analyzed carefully as failure cases.

## Recommended Outputs

The uncertainty analysis should produce:

- uncertainty summary tables;
- interval or confidence plots;
- calibration plots for classification outputs;
- narrative interpretation of where uncertainty is highest.

## Recommended Conclusion

Uncertainty analysis should complement, not replace, standard evaluation metrics. In this project, uncertainty is especially important for identifying where model predictions are weakly supported and where additional caution is needed in safety-oriented interpretation.
