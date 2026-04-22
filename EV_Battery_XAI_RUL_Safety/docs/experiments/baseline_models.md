# Baseline Models

## Purpose

This document recommends baseline models for the two primary supervised learning tasks in the project:

- `target_rul` as a regression problem;
- `target_safety_risk` as a classification problem.

Baseline models are essential because they provide:

- minimum performance references;
- interpretable comparisons for more advanced models;
- a check on whether the engineered feature set contains meaningful signal.

## Baseline Model Principles

Baseline models should be:

- simple to train and reproduce;
- interpretable or at least easy to audit;
- appropriate for the scale and structure of the processed feature table;
- strong enough to serve as meaningful benchmarks rather than trivial placeholders.

## Baseline Models for RUL Regression

## 1. Mean or Median Predictor

### Description

Predict the mean or median `target_rul` value from the training data for all test observations.

### Purpose

- provides a minimal statistical reference;
- confirms whether learned models outperform a naive baseline.

### Advantages

- extremely simple;
- useful for sanity checking evaluation metrics.

### Limitations

- no interpretability regarding battery variables;
- not useful as a substantive modeling approach.

## 2. Linear Regression

### Description

Fit a linear relationship between engineered features and `target_rul`.

### Purpose

- provides a transparent benchmark for structured tabular features;
- allows direct inspection of coefficients.

### Advantages

- highly interpretable;
- easy to diagnose;
- suitable for coefficient-based explanation.

### Limitations

- may underfit non-linear degradation behavior;
- sensitive to collinearity.

## 3. Regularized Linear Regression

Recommended variants:

- Ridge regression;
- Lasso regression;
- Elastic net.

### Purpose

- provide more stable linear baselines when features are numerous or correlated;
- support implicit feature selection.

### Advantages

- interpretable;
- robust in high-dimensional feature spaces;
- useful for reduced-feature benchmarking.

### Limitations

- still limited in capturing strongly non-linear behavior.

## 4. Random Forest Regressor

### Description

A tree-based ensemble regression model using engineered features.

### Purpose

- provides a stronger non-linear baseline without requiring sequence modeling.

### Advantages

- handles non-linear interactions;
- relatively robust to scaling;
- compatible with feature importance analysis.

### Limitations

- less transparent than linear models;
- feature importance may be biased if used uncritically.

## 5. Gradient Boosting Regressor

Recommended variants:

- XGBoost;
- LightGBM;
- CatBoost, where appropriate.

### Purpose

- serve as strong structured-feature baselines for RUL prediction.

### Advantages

- often high-performing on tabular data;
- compatible with SHAP analysis;
- captures non-linear structure effectively.

### Limitations

- more complex than linear baselines;
- explainability depends on post hoc methods.

## Baseline Models for Safety Risk Classification

## 1. Majority-Class Classifier

### Description

Predict the most frequent safety-risk class in the training data.

### Purpose

- provides a minimal classification benchmark;
- particularly important in imbalanced safety datasets.

### Limitations

- no task insight;
- inadequate for real use beyond benchmarking.

## 2. Logistic Regression

### Description

A linear probabilistic classifier for binary or one-vs-rest multi-class safety labels.

### Purpose

- provides an interpretable classification baseline;
- supports coefficient-based feature interpretation.

### Advantages

- simple;
- transparent;
- suitable for calibrated probability outputs in many settings.

### Limitations

- may underfit non-linear safety patterns;
- sensitive to feature scaling and collinearity.

## 3. Regularized Logistic Regression

Recommended variants:

- L1-regularized logistic regression;
- L2-regularized logistic regression;
- Elastic net logistic regression.

### Purpose

- improve stability in the presence of many engineered features;
- support sparse and interpretable classification baselines.

## 4. Decision Tree Classifier

### Description

A simple rule-based tree classifier.

### Purpose

- provide a transparent non-linear baseline;
- useful for understanding coarse decision boundaries in safety labeling.

### Advantages

- easily visualized;
- interpretable as a rule hierarchy.

### Limitations

- unstable if not constrained;
- often weaker than ensemble methods.

## 5. Random Forest Classifier

### Purpose

- provide a stronger non-linear tabular baseline for safety classification.

### Advantages

- can capture non-linear relationships and interactions;
- useful for feature-importance screening.

### Limitations

- less interpretable than logistic regression or small trees.

## 6. Gradient Boosting Classifier

Recommended variants:

- XGBoost classifier;
- LightGBM classifier;
- CatBoost classifier, where applicable.

### Purpose

- serve as strong structured-feature baselines for safety prediction.

### Advantages

- strong performance on engineered tabular features;
- compatible with SHAP-based explanation.

### Limitations

- interpretation is post hoc rather than intrinsic.

## Recommended Baseline Set

The minimum recommended baseline set is:

### For `target_rul`

- mean or median predictor;
- Ridge or Elastic Net regression;
- random forest regressor;
- gradient boosting regressor.

### For `target_safety_risk`

- majority-class classifier;
- regularized logistic regression;
- decision tree classifier;
- gradient boosting classifier.

## Role of Baselines in the Study

Baseline models should be used to answer three questions:

1. Do engineered battery features contain predictive signal for each task?
2. How much improvement is achieved by more advanced non-linear or sequence-based models?
3. Does the performance gain justify a reduction in interpretability?

## Performance-Explainability Note

Linear and tree-based baselines are especially important in this project because they provide reference explanations against which more complex models can be compared. Even if they are not the best-performing models, they are methodologically valuable for interpreting the predictive structure of the data.
