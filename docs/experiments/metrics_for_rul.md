# Metrics for RUL Prediction

## Purpose

This document recommends evaluation metrics for `target_rul` in the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

Because RUL is treated as a regression target, the evaluation framework should measure both overall prediction accuracy and the practical significance of large errors, especially near end-of-life.

## Recommended Primary Metrics

## 1. Mean Absolute Error (MAE)

### Definition

The average absolute difference between predicted RUL and true RUL.

### Why It Matters

- easy to interpret in the native unit of the target, such as cycles or time;
- less sensitive to extreme outliers than squared-error measures;
- suitable for summary comparison across models.

### Recommended Role

MAE should be treated as a primary metric for RUL reporting.

## 2. Root Mean Squared Error (RMSE)

### Definition

The square root of the average squared prediction error.

### Why It Matters

- penalizes large errors more strongly than MAE;
- useful when large late-stage forecasting mistakes are particularly undesirable.

### Recommended Role

RMSE should be reported alongside MAE to capture the severity of occasional large errors.

## 3. Mean Absolute Percentage Error (MAPE)

### Definition

The average absolute percentage deviation between prediction and target.

### Why It Matters

- useful for scale-relative comparison in some settings.

### Limitation

- problematic when true RUL values approach zero, which is common near end-of-life.

### Recommended Role

MAPE may be used as a secondary metric only when target values are sufficiently bounded away from zero or when a stable variant is used.

## Recommended Secondary Metrics

## 4. Coefficient of Determination (R-squared)

### Why It Matters

- provides a familiar summary of variance explained;
- useful for general regression benchmarking.

### Limitation

- less informative than MAE or RMSE for safety-relevant operational interpretation.

### Recommended Role

Use as a secondary descriptive metric rather than a primary selection criterion.

## 5. Median Absolute Error

### Why It Matters

- robust to extreme outliers;
- useful for understanding typical error under skewed error distributions.

### Recommended Role

Use as an optional robustness-oriented summary statistic.

## End-of-Life-Relevant Considerations

RUL prediction should not be evaluated only in aggregate. Additional attention should be given to:

- errors near end-of-life;
- errors in early-life versus late-life regimes;
- systematic overestimation or underestimation.

### Why This Matters

Overestimating RUL near end-of-life may be operationally more problematic than modest errors in early-life stages.

## Recommended Supplemental Analyses

### 1. Error by Life Stage

Evaluate MAE or RMSE separately for:

- early life;
- mid life;
- late life.

### 2. Bias Analysis

Evaluate whether the model tends to:

- systematically overestimate RUL;
- systematically underestimate RUL.

### 3. Error Distribution Analysis

Inspect:

- residual histograms;
- residuals versus true RUL;
- residuals versus cycle index or degradation stage.

## Recommended Metric Set for the Project

The recommended reporting set for `target_rul` is:

- MAE;
- RMSE;
- R-squared;
- one stage-aware or late-life-focused supplementary error analysis.

## Model Selection Guidance

For this project, the preferred RUL model should not be selected solely on the lowest aggregate RMSE. Preference should be given to models that:

- achieve competitive MAE and RMSE;
- avoid large late-stage errors;
- remain stable across batteries or operating regimes;
- support interpretable analysis of dominant predictors.

## Recommended Conclusion

MAE and RMSE should serve as the principal evaluation metrics for RUL regression, with additional life-stage-sensitive analysis to capture operational relevance near end-of-life. This approach is more appropriate than relying on a single aggregate goodness-of-fit measure alone.
