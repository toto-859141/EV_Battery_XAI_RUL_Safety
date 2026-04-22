# Data Leakage Risks

## Purpose

This document identifies common forms of data leakage relevant to battery-monitoring studies involving:

- Remaining Useful Life prediction; and
- Safety Risk prediction.

Because battery data are time-dependent and often highly correlated within each battery trajectory, leakage can arise easily during preprocessing, feature engineering, target construction, scaling, and evaluation.

## Why Leakage Matters

Data leakage occurs when information unavailable at the intended prediction time influences model training or evaluation. This leads to inflated performance estimates and weakens the credibility of the results, especially in safety-relevant applications.

## Common Leakage Risks

### 1. Future Information in Features

Risk:
Features are computed using observations that occur after the prediction window.

Example:

- using the full battery lifecycle to compute a trend feature for an early prediction window;
- computing summary statistics that include future cycles.

Mitigation:

- compute features using only data available up to the end of the observation window;
- validate feature code with explicit temporal boundaries.

### 2. Leakage Through End-of-Life-Derived Features

Risk:
Features include values that are mathematically or operationally derived from the same future information used to define `target_rul`.

Example:

- using remaining capacity-to-failure directly as an input while also predicting `target_rul`.

Mitigation:

- separate target-construction logic from feature-construction logic;
- exclude any feature that encodes direct knowledge of future failure timing.

### 3. Random Row-Level Splitting

Risk:
Highly similar windows from the same battery trajectory appear in both training and test sets.

Example:

- windows from cycles 100 to 104 in the training set and cycles 105 to 109 in the test set without grouped separation.

Mitigation:

- split by battery identity or blocked chronology;
- preserve sequential dependence when creating train, validation, and test sets.

### 4. Leakage Across Safety Events

Risk:
Windows adjacent to the same fault or safety event are split across training and testing.

Example:

- pre-event windows for one thermal event appear in training, while later windows from the same event appear in testing.

Mitigation:

- split at the event or battery level rather than the window row level;
- treat each event trajectory as a grouped unit during splitting.

### 5. Global Scaling Before Splitting

Risk:
Normalization or standardization parameters are fitted on the full dataset before train-test separation.

Mitigation:

- fit scalers on training data only;
- apply the learned parameters unchanged to validation and test data.

### 6. Imputation Using Full-Dataset Statistics

Risk:
Missing-value imputation uses mean, median, nearest-neighbor, or model-based parameters estimated from the entire dataset.

Mitigation:

- fit imputation rules on training data only;
- document whether imputation is performed within battery, within split, or globally within training.

### 7. Feature Selection Before Splitting

Risk:
Feature importance, correlation filtering, or dimensionality reduction is performed using all rows before the data split.

Mitigation:

- perform feature selection or dimensionality reduction within the training set only;
- if cross-validation is used, repeat selection inside each fold.

### 8. Target Proxy Leakage in Safety Labels

Risk:
`target_safety_risk` is defined using variables that also appear directly in untransformed feature form, effectively making the task a near-duplicate of the labeling rule.

Example:

- defining high risk solely as temperature greater than a threshold and then using the same uncontextualized temperature threshold as the dominant model input.

Mitigation:

- document the proxy logic explicitly;
- prefer multi-indicator label definitions where justified;
- evaluate whether the model is learning meaningful structure rather than reproducing a single rule.

### 9. Duplicate or Near-Duplicate Windows

Risk:
Repeated or heavily overlapping windows appear across training and evaluation splits.

Mitigation:

- control overlap between adjacent windows;
- prevent near-duplicate windows from crossing split boundaries;
- report the windowing policy clearly.

### 10. Hyperparameter Tuning on the Test Set

Risk:
Test-set performance influences model selection, feature engineering choices, or label definitions.

Mitigation:

- reserve the test set for one final evaluation only;
- use validation data or nested training procedures for tuning.

## Leakage Risk Summary Table

| Leakage source | Example | Main consequence | Prevention strategy |
| --- | --- | --- | --- |
| Future information in features | Using later-cycle data in current-window features | Inflated predictive accuracy | Restrict features to past and present observations |
| End-of-life-derived features | Input encodes failure timing | Artificially easy RUL prediction | Separate feature and target logic |
| Random row splitting | Same battery trajectory in train and test | Over-optimistic generalization | Grouped chronological split |
| Event adjacency leakage | Same safety event appears across splits | Inflated safety performance | Event-level or battery-level grouping |
| Global scaling | Scaler fitted on full dataset | Information transfer across splits | Fit scaler on training data only |
| Full-dataset imputation | Missing values filled using all data | Hidden leakage through preprocessing | Fit imputation on training only |
| Pre-split feature selection | Full-data importance filtering | Test information influences features | Select features within training only |
| Proxy-label duplication | Label mirrors a raw input threshold | Misleading safety model validity | Use documented and justified proxy logic |

## Recommended Audit Checklist

Before model training, verify the following:

1. Are all features computed using only past and current observations?
2. Are train, validation, and test splits separated before fitting preprocessing objects?
3. Are batteries or event trajectories prevented from crossing splits in a way that creates near-duplicate observations?
4. Are label definitions documented separately from feature definitions?
5. Is the test set untouched during model and feature selection?

## Methodological Note

Leakage control is especially important in this project because the same raw signals may be used to derive both degradation-oriented and safety-oriented features. A rigorous separation between observation windows, labels, preprocessing parameters, and evaluation splits is therefore necessary for both predictive credibility and explainability validity.
