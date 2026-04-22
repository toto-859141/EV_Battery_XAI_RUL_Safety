# Train, Validation, and Test Strategy

## Purpose

This document recommends a data-splitting strategy for time-dependent battery monitoring data used in prognostic and safety-oriented machine learning tasks.

The objective is to produce evaluation results that are:

- temporally valid;
- resistant to leakage;
- comparable across experiments; and
- appropriate for both RUL and safety risk prediction.

## Principle

Because battery monitoring data are sequential and often contain strong within-battery dependence, the data split must preserve:

- temporal order;
- battery-level grouping where relevant; and
- separation between training information and future evaluation windows.

Random row-wise splitting is not recommended for the main evaluation because it can produce unrealistically optimistic results.

## Recommended Primary Strategy

The recommended primary strategy is a **battery-grouped chronological split**.

This means:

- windows from the same battery should not be distributed across train, validation, and test sets unless there is a clear within-battery forecasting justification;
- within each battery, earlier windows should precede later windows;
- the test set should represent later or held-out battery trajectories not used for model fitting.

## Preferred Split Designs

### Option 1: Hold-Out Batteries for External-Like Generalization

Use this design when multiple battery entities are available.

Recommended logic:

- training set: earlier trajectories from one group of batteries;
- validation set: later or separate trajectories from a second group of batteries;
- test set: fully held-out batteries or battery trajectories.

Advantages:

- strongest protection against battery-level leakage;
- better estimate of generalization to unseen batteries.

Limitations:

- may reduce training data size when the number of batteries is small.

### Option 2: Chronological Split Within Battery Groups

Use this design when the number of batteries is limited but each battery has long trajectories.

Recommended logic:

- training set: earliest 60 to 70 percent of windows;
- validation set: next 10 to 20 percent of windows;
- test set: final 20 percent of windows.

This split should be applied separately within each battery or battery group, then combined only after preserving the temporal partitions.

Advantages:

- respects forecasting order;
- suitable for long degradation sequences.

Limitations:

- if the same battery appears across splits, performance may still be optimistic relative to true unseen-battery deployment.

## Recommended Default

If the dataset contains multiple batteries, the preferred default is:

- `train`: 70 percent of batteries or trajectories
- `validation`: 15 percent
- `test`: 15 percent

with chronological ordering preserved within each battery and complete battery hold-out favored for the test set.

## Validation Strategy for Model Selection

Within the training portion, model selection should use one of the following:

- rolling-origin validation;
- blocked time-series cross-validation;
- grouped cross-validation that respects battery identity.

### Recommended Choice

Rolling-origin or blocked time-series validation is recommended when:

- temporal forecasting behavior is central; and
- sufficient sequential depth exists within the training data.

## Task-Specific Notes

### For `target_rul`

The split must preserve degradation progression. Training windows must always precede evaluation windows in the battery lifecycle.

### For `target_safety_risk`

If safety labels are event-based, the split must ensure that:

- pre-event windows from the same event are not split across training and testing;
- event-adjacent windows do not appear in both train and test sets.

## Reporting Requirements

The methodology chapter should report:

- the splitting unit, such as battery, cycle sequence, or window sequence;
- whether batteries are held out completely;
- temporal boundaries of each split;
- the number of entities and windows in each split;
- any class-imbalance handling applied within the training data only.

## Practices to Avoid

The following practices should be avoided in the main evaluation:

- random row-level splitting across all windows;
- fitting scalers or selectors before the split;
- allowing windows from the same near-identical event sequence into multiple splits;
- tuning hyperparameters on the test set.
