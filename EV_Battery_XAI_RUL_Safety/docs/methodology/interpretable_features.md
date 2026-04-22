# Interpretable Feature Catalogue

## Purpose

This document defines a catalogue of interpretable engineered features for the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The features below are proposed as candidate inputs for classical machine learning and hybrid deep learning workflows. Each feature is described in terms of:

- definition;
- why it matters;
- task relevance;
- interpretability.

## Reading Guide

Task support is recorded using the following shorthand:

- `RUL`: primarily supports remaining useful life prediction
- `Safety`: primarily supports safety risk prediction
- `Both`: relevant to both prediction tasks

Interpretability is recorded qualitatively as:

- `High`: directly understandable in physical or engineering terms
- `Moderate`: interpretable but dependent on derivation details
- `Low`: more abstract or model-specific

## Electrical Behavior Features

### 1. Mean Voltage

- Definition: average terminal voltage within the observation window.
- Why it matters: summarizes the electrical operating state and may reflect loading conditions or altered electrochemical response.
- Task support: Both
- Interpretability: High

### 2. Voltage Range

- Definition: difference between maximum and minimum voltage within the observation window.
- Why it matters: captures electrical fluctuation and may indicate unstable operation, load variation, or altered charge-discharge response.
- Task support: Both
- Interpretability: High

### 3. Voltage Slope

- Definition: rate of voltage change over time or over the charge-discharge segment.
- Why it matters: may reflect response dynamics linked to degradation or abnormal electrical behavior.
- Task support: Both
- Interpretability: Moderate

### 4. Mean Current

- Definition: average current within the observation window.
- Why it matters: provides a measure of loading intensity and helps contextualize both degradation and abnormal conditions.
- Task support: Both
- Interpretability: High

### 5. Peak Current

- Definition: maximum absolute current recorded within the observation window.
- Why it matters: high-current events can accelerate stress and may contribute to safety-relevant abnormality.
- Task support: Both
- Interpretability: High

### 6. Current Variability

- Definition: standard deviation or similar dispersion measure of current within the observation window.
- Why it matters: unstable current demand may be associated with irregular operation, control instability, or varying stress.
- Task support: Both
- Interpretability: High

### 7. Current Spike Count

- Definition: number of current observations exceeding a predefined spike threshold within the window.
- Why it matters: repeated spikes may reflect abnormal operating stress and can be safety-relevant.
- Task support: Safety
- Interpretability: High

### 8. Voltage-Current Consistency Indicator

- Definition: feature describing whether voltage response is consistent with expected current behavior under the operating mode.
- Why it matters: inconsistency may indicate abnormal electrochemical or control behavior.
- Task support: Safety
- Interpretability: Moderate

## Thermal Behavior Features

### 9. Mean Temperature

- Definition: average battery temperature within the observation window.
- Why it matters: persistent thermal elevation may indicate increased stress and accelerated degradation.
- Task support: Both
- Interpretability: High

### 10. Maximum Temperature

- Definition: highest temperature observed within the window.
- Why it matters: strongly relevant to safety because extreme temperature is a direct indicator of potential thermal hazard.
- Task support: Safety
- Interpretability: High

### 11. Temperature Range

- Definition: difference between maximum and minimum temperature within the observation window.
- Why it matters: captures thermal variability and possible instability.
- Task support: Both
- Interpretability: High

### 12. Temperature Rise Rate

- Definition: rate of increase in temperature over time during the window.
- Why it matters: rapid heating may be more safety-relevant than high temperature alone.
- Task support: Safety
- Interpretability: High

### 13. Temperature Variance

- Definition: dispersion of temperature values within the observation window.
- Why it matters: unstable temperature behavior may signal abnormal operation or poor thermal control.
- Task support: Safety
- Interpretability: High

### 14. Temperature Excursion Count

- Definition: number of observations above a documented temperature threshold.
- Why it matters: repeated thermal excursions are a direct and interpretable warning indicator.
- Task support: Safety
- Interpretability: High

### 15. Thermal Recovery Time

- Definition: time required for temperature to return toward baseline after a heating period.
- Why it matters: prolonged recovery may indicate thermal stress accumulation or impaired heat dissipation.
- Task support: Both
- Interpretability: Moderate

## Degradation Indicator Features

### 16. Capacity Retention

- Definition: current usable capacity as a fraction of nominal or initial capacity.
- Why it matters: one of the most direct indicators of degradation progression and end-of-life proximity.
- Task support: RUL
- Interpretability: High

### 17. Capacity Fade Rate

- Definition: rate of capacity decline across recent cycles or windows.
- Why it matters: summarizes degradation velocity rather than only current degradation state.
- Task support: RUL
- Interpretability: High

### 18. Internal Resistance Proxy

- Definition: derived estimate of resistance growth from voltage-current response or direct resistance measurement when available.
- Why it matters: increased resistance is associated with aging, power fade, and altered thermal behavior.
- Task support: Both
- Interpretability: Moderate

### 19. Coulombic Efficiency

- Definition: ratio of discharge capacity to charge capacity within a cycle or aligned window.
- Why it matters: reduced efficiency may indicate degradation or unstable electrochemical behavior.
- Task support: RUL
- Interpretability: High

### 20. Energy Efficiency

- Definition: ratio of output energy to input energy over an observation window.
- Why it matters: summarizes operational degradation and may reflect internal losses.
- Task support: RUL
- Interpretability: High

### 21. Cycle-to-Cycle Degradation Change

- Definition: change in a degradation metric, such as capacity or resistance, relative to recent historical windows.
- Why it matters: captures acceleration or deceleration in degradation progression.
- Task support: RUL
- Interpretability: Moderate

### 22. Voltage Curve Summary Descriptor

- Definition: compact descriptor extracted from the shape of the voltage curve during charge or discharge.
- Why it matters: can capture degradation-related change beyond simple scalar summaries.
- Task support: Both
- Interpretability: Moderate

## Operational Usage Pattern Features

### 23. Charge Duration

- Definition: duration of charging activity within a cycle or observation window.
- Why it matters: helps characterize usage intensity and control behavior.
- Task support: Both
- Interpretability: High

### 24. Discharge Duration

- Definition: duration of discharge activity within a cycle or observation window.
- Why it matters: reflects demand patterns and may contextualize degradation progression.
- Task support: Both
- Interpretability: High

### 25. Depth of Discharge

- Definition: fraction of usable capacity withdrawn during the cycle or window.
- Why it matters: deep discharge cycles are known to influence degradation and stress.
- Task support: Both
- Interpretability: High

### 26. Charge Rate

- Definition: effective charging C-rate or normalized charging intensity.
- Why it matters: aggressive charging can accelerate degradation and elevate thermal risk.
- Task support: Both
- Interpretability: High

### 27. Discharge Rate

- Definition: effective discharging C-rate or normalized discharge intensity.
- Why it matters: high-rate discharge can impose electrical and thermal stress.
- Task support: Both
- Interpretability: High

### 28. Energy Throughput

- Definition: cumulative energy processed during the observation window or up to the current cycle.
- Why it matters: summarizes battery usage burden and long-term wear.
- Task support: RUL
- Interpretability: High

### 29. Rest Duration

- Definition: duration of rest or idle time between active operating periods.
- Why it matters: recovery time may affect voltage relaxation and the interpretation of subsequent signals.
- Task support: Both
- Interpretability: High

### 30. High-Stress Operation Frequency

- Definition: proportion or count of intervals within the window characterized by high current, high temperature, or high depth of discharge.
- Why it matters: aggregates repeated stress exposure into an interpretable usage indicator.
- Task support: Both
- Interpretability: High

## Methodological Note

These features are intended as a starting catalogue rather than a fixed mandatory set. The final subset should depend on:

- dataset availability;
- measurement quality;
- task definition;
- model family;
- leakage control constraints.

In all cases, features should be computed using only information available up to the end of the observation window.
