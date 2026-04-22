# Metrics for Safety Risk Prediction

## Purpose

This document recommends evaluation metrics for `target_safety_risk` in the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

Because safety risk is treated as a classification or risk-scoring outcome, the evaluation framework must consider not only overall predictive accuracy but also the safety consequences of different error types.

## Recommended Primary Metrics

## 1. F1-Score

### Definition

The harmonic mean of precision and recall.

### Why It Matters

- useful when classes are imbalanced;
- balances detection quality and false-alarm control.

### Recommended Role

Macro F1 or class-weighted F1 should be reported as a primary metric, depending on the final label structure.

## 2. Recall for High-Risk Class

### Definition

The proportion of true high-risk cases correctly identified.

### Why It Matters

- directly relevant to safety-critical monitoring;
- low recall in the high-risk class means the model misses dangerous or concerning cases.

### Recommended Role

High-risk recall should be treated as a primary safety-relevant metric rather than only a secondary detail.

## 3. Precision for High-Risk Class

### Definition

The proportion of predicted high-risk cases that are truly high-risk.

### Why It Matters

- high false-alarm rates may reduce trust and operational usefulness.

### Recommended Role

Should be reported together with recall to characterize the warning trade-off.

## 4. Area Under the Receiver Operating Characteristic Curve (AUROC)

### Why It Matters

- useful for comparing discriminative ability across thresholds;
- appropriate when probability outputs are available.

### Limitation

- may appear optimistic in highly imbalanced settings.

### Recommended Role

Use as a secondary metric, not as the only selection criterion.

## 5. Area Under the Precision-Recall Curve (AUPRC)

### Why It Matters

- more informative than AUROC when the high-risk class is rare;
- directly reflects precision-recall behavior in imbalanced datasets.

### Recommended Role

Strongly recommended when high-risk observations are sparse.

## Recommended Secondary Metrics

## 6. Accuracy

### Why It Matters

- familiar and simple.

### Limitation

- can be misleading under class imbalance.

### Recommended Role

Report only as a secondary descriptive metric.

## 7. Confusion Matrix

### Why It Matters

- reveals the absolute pattern of correct and incorrect classifications;
- essential for identifying false negatives and false positives.

### Recommended Role

A confusion matrix should always accompany the metric summary.

## Safety-Relevant False Negatives and False Positives

## False Negatives

Definition:

- the model predicts low or moderate risk when the true class is high risk.

Why They Matter:

- these errors may suppress warning signals in cases where elevated concern is warranted;
- they are particularly important in safety-critical monitoring.

## False Positives

Definition:

- the model predicts high risk when the true class is lower risk.

Why They Matter:

- these errors may lead to unnecessary warnings or interventions;
- excessive false alarms may reduce trust in the monitoring system.

## Recommended Evaluation Position

False negatives should generally be treated as the more critical error type in safety-oriented settings, but false positives should still be monitored carefully because they affect operational credibility and response burden.

## Recommended Metric Set for the Project

The recommended reporting set for `target_safety_risk` is:

- macro or weighted F1-score;
- high-risk recall;
- high-risk precision;
- AUPRC where probabilities are available;
- confusion matrix.

## Threshold-Aware Evaluation

If the model outputs probabilities or scores rather than only hard classes, the evaluation should include threshold analysis.

Recommended analyses:

- precision-recall trade-off across thresholds;
- recall-oriented threshold setting for high-risk detection;
- threshold choice aligned with the warning-level design.

## Recommended Conclusion

Safety-risk classification should be evaluated using a metric set that makes false negatives and false positives visible rather than relying on overall accuracy alone. High-risk recall, F1-score, and precision-recall-based analysis are especially important for a safety-critical battery monitoring context.
