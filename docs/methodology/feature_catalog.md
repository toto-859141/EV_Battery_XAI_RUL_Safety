# Feature Catalog

## Purpose

This catalog provides a consolidated candidate feature list for electric vehicle battery monitoring research in the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The table is designed for methodology planning, feature review, and later implementation in both:

- classical machine learning pipelines based on engineered tabular features; and
- hybrid or deep learning workflows that combine raw sequences with structured summary variables.

The candidate features below are organized to support two distinct outcomes:

- `target_rul`
- `target_safety_risk`

## Feature Catalog Table

| Feature Name | Category | Description | Data Source | Supports RUL | Supports Safety Risk | Interpretability Level | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mean voltage | Electrical behavior | Average terminal voltage within the observation window | Raw voltage time series | Yes | Yes | High | Useful baseline electrical-state summary |
| Minimum voltage | Electrical behavior | Lowest voltage observed within the observation window | Raw voltage time series | Yes | Yes | High | May indicate deep discharge or abnormal sag |
| Maximum voltage | Electrical behavior | Highest voltage observed within the observation window | Raw voltage time series | Yes | Yes | High | Relevant to charging behavior and voltage stress |
| Voltage range | Electrical behavior | Difference between maximum and minimum voltage within the window | Raw voltage time series | Yes | Yes | High | Captures electrical fluctuation and instability |
| Voltage standard deviation | Electrical behavior | Dispersion of voltage values within the window | Raw voltage time series | Yes | Yes | High | Useful for detecting unstable electrical behavior |
| Voltage slope | Electrical behavior | Rate of voltage change over time or over charge-discharge progression | Raw voltage time series | Yes | Yes | Moderate | Interpretation depends on segment definition |
| Voltage recovery magnitude | Electrical behavior | Change in voltage during rest or recovery period after load | Raw voltage and rest-period segments | Yes | Yes | Moderate | May reflect internal state and electrochemical relaxation |
| Voltage recovery time | Electrical behavior | Time required for voltage to stabilize after load change | Raw voltage and timestamp data | Yes | Yes | Moderate | Sensitive to protocol and sampling frequency |
| Mean current | Electrical behavior | Average current within the observation window | Raw current time series | Yes | Yes | High | Summarizes loading intensity |
| Maximum absolute current | Electrical behavior | Highest absolute current observed within the window | Raw current time series | Yes | Yes | High | Important for stress characterization |
| Current range | Electrical behavior | Difference between maximum and minimum current values | Raw current time series | Yes | Yes | High | Represents variation in load demand |
| Current standard deviation | Electrical behavior | Dispersion of current within the window | Raw current time series | Yes | Yes | High | Useful for irregular usage characterization |
| Current spike count | Electrical behavior | Number of current samples above a defined spike threshold | Raw current time series | No | Yes | High | Particularly relevant to abnormal high-stress operation |
| Current zero-crossing count | Electrical behavior | Number of sign changes in current within the window | Raw current time series | Yes | Yes | Moderate | May capture switching or mixed operating states |
| Voltage-current consistency indicator | Electrical behavior | Deviation from expected voltage response under observed current conditions | Joint voltage-current series | No | Yes | Moderate | Useful for abnormal-response detection |
| Mean power | Electrical behavior | Average electrical power estimated as voltage multiplied by current | Derived from raw voltage and current | Yes | Yes | High | Useful summary of operational load |
| Peak power | Electrical behavior | Highest absolute power value within the window | Derived from raw voltage and current | Yes | Yes | High | May capture high-demand operating stress |
| Power variability | Electrical behavior | Dispersion of power values within the window | Derived from raw voltage and current | Yes | Yes | Moderate | Useful for dynamic usage characterization |
| Mean temperature | Thermal behavior | Average battery temperature within the observation window | Raw temperature time series | Yes | Yes | High | Persistent thermal elevation can affect both tasks |
| Minimum temperature | Thermal behavior | Lowest temperature observed within the window | Raw temperature time series | Yes | No | High | Useful for contextual thermal state |
| Maximum temperature | Thermal behavior | Highest temperature observed within the window | Raw temperature time series | Yes | Yes | High | Strongly relevant to safety-oriented modeling |
| Temperature range | Thermal behavior | Difference between maximum and minimum temperature within the window | Raw temperature time series | Yes | Yes | High | Captures thermal instability |
| Temperature standard deviation | Thermal behavior | Dispersion of temperature within the window | Raw temperature time series | No | Yes | High | Useful indicator of unstable thermal behavior |
| Temperature rise rate | Thermal behavior | Rate of temperature increase across the observation window | Raw temperature and time series | Yes | Yes | High | Rapid heating is particularly safety-relevant |
| Temperature excursion count | Thermal behavior | Number of observations above a documented thermal threshold | Raw temperature time series | No | Yes | High | Useful for rule-based safety labeling |
| Thermal recovery time | Thermal behavior | Time required for temperature to return toward baseline after heating | Raw temperature and timestamp data | Yes | Yes | Moderate | Protocol-sensitive but potentially informative |
| Thermal gradient | Thermal behavior | Difference between sensor locations or spatial temperature spread | Multi-sensor temperature data | No | Yes | Moderate | Requires multiple thermal sensors |
| Temperature-current coupling index | Thermal behavior | Relation between current intensity and resulting thermal response | Joint temperature-current series | Yes | Yes | Moderate | Can capture stress-response mismatch |
| Capacity retention | Degradation indicators | Current usable capacity relative to nominal or initial capacity | Capacity measurements or derived cycle summaries | Yes | No | High | One of the most interpretable RUL features |
| Capacity fade rate | Degradation indicators | Rate of decline in capacity across recent cycles or windows | Capacity history | Yes | No | High | Captures degradation velocity |
| Incremental capacity change | Degradation indicators | Change in capacity-related measure over adjacent cycles or windows | Capacity history or voltage-capacity curves | Yes | No | Moderate | Useful when curve-based diagnostics are available |
| Internal resistance | Degradation indicators | Direct measurement of internal resistance where available | Sensor or lab measurement | Yes | Yes | High | Relevant to both aging and thermal burden |
| Internal resistance proxy | Degradation indicators | Estimated resistance-related feature derived from voltage-current response | Raw voltage and current series | Yes | Yes | Moderate | Useful when direct resistance is unavailable |
| Resistance growth rate | Degradation indicators | Rate of increase in resistance across recent cycles | Resistance history or proxy history | Yes | Yes | Moderate | Can indicate accelerated aging |
| Coulombic efficiency | Degradation indicators | Ratio of discharge capacity to charge capacity within a cycle | Charge and discharge capacity records | Yes | No | High | Strong degradation-oriented feature in cycle data |
| Energy efficiency | Degradation indicators | Ratio of useful output energy to input energy | Voltage-current-energy calculations | Yes | No | High | Captures internal loss progression |
| Equivalent full cycle count | Degradation indicators | Cumulative normalized cycle usage based on partial use aggregation | Cycle logs and depth-of-discharge data | Yes | No | High | Particularly useful for irregular use patterns |
| Cycle-to-cycle degradation change | Degradation indicators | Change in degradation indicator relative to recent history | Degradation history | Yes | No | Moderate | Highlights acceleration or regime change |
| Voltage curve summary descriptor | Degradation indicators | Compact descriptor of charge-discharge voltage curve shape | Voltage sequence or voltage-capacity curve | Yes | Yes | Moderate | Can be informative but depends on curve extraction method |
| Incremental capacity peak position | Degradation indicators | Position of key peak in incremental capacity analysis | Voltage-capacity-derived diagnostic curve | Yes | No | Moderate | Useful in detailed diagnostic datasets |
| Differential voltage feature | Degradation indicators | Descriptor derived from differential voltage analysis | Voltage-capacity-derived diagnostic curve | Yes | No | Moderate | More specialized but informative in aging studies |
| State-of-charge mean | Operational usage patterns | Average state of charge within the observation window | SOC series or battery management system output | Yes | Yes | High | Useful contextual variable if reliably available |
| State-of-charge range | Operational usage patterns | Difference between maximum and minimum SOC in the window | SOC series or derived usage records | Yes | Yes | High | Indicates cycle depth or usage intensity |
| Depth of discharge | Operational usage patterns | Fraction of usable capacity withdrawn during the cycle or window | SOC or capacity records | Yes | Yes | High | Strong operational stress indicator |
| Charge duration | Operational usage patterns | Duration of charging activity within the window | Timestamped operating-mode records | Yes | Yes | High | Useful contextual feature for both tasks |
| Discharge duration | Operational usage patterns | Duration of discharge activity within the window | Timestamped operating-mode records | Yes | Yes | High | Reflects demand profile and usage burden |
| Rest duration | Operational usage patterns | Duration of idle or rest intervals between active segments | Timestamped operating-mode records | Yes | Yes | High | Relevant to voltage relaxation and recovery behavior |
| Charge rate | Operational usage patterns | Effective charging C-rate or normalized charging intensity | Current, nominal capacity, and charge records | Yes | Yes | High | Aggressive charging can affect both aging and safety |
| Discharge rate | Operational usage patterns | Effective discharging C-rate or normalized discharge intensity | Current, nominal capacity, and discharge records | Yes | Yes | High | Useful indicator of operating stress |
| Energy throughput | Operational usage patterns | Cumulative energy processed within the window or up to current use stage | Derived from voltage-current integration | Yes | No | High | Strong usage-burden variable for RUL |
| Charge throughput | Operational usage patterns | Cumulative charge transferred within the window | Current integration over time | Yes | Yes | High | Useful for usage normalization |
| High-stress operation frequency | Operational usage patterns | Frequency of intervals with high current, high temperature, or deep discharge | Derived from combined operational and sensor signals | Yes | Yes | High | Compact aggregated stress measure |
| High-rate charging fraction | Operational usage patterns | Proportion of charging time above a chosen charge-rate threshold | Charge logs and current records | Yes | Yes | High | Useful for stress profiling |
| High-load discharge fraction | Operational usage patterns | Proportion of discharge time above a chosen discharge-rate threshold | Discharge logs and current records | Yes | Yes | High | Useful for stress profiling |
| Ambient temperature | Operational usage patterns | Environmental temperature associated with battery operation | External sensor or metadata | Yes | Yes | High | Important contextual control variable |
| Operating-mode fraction | Operational usage patterns | Proportion of time spent in charge, discharge, or rest mode | Operating-mode logs | Yes | Yes | High | Summarizes window composition |
| Window cycle index | Operational usage patterns | Position of the observation window in the battery lifecycle | Cycle metadata | Yes | No | High | Useful as a lifecycle-progress feature if not leakage-prone |
| Usage irregularity index | Operational usage patterns | Summary measure of irregularity in timing, load, or cycling behavior | Timestamps, current, and mode logs | Yes | Yes | Moderate | More abstract but useful in field data |
| Abnormal event count | Safety-relevant derived indicators | Count of flagged abnormal events within the observation window | Derived from rule-based screening of raw signals | No | Yes | High | Useful if event rules are documented explicitly |
| Thermal-electrical stress interaction score | Safety-relevant derived indicators | Combined feature summarizing concurrent high thermal and electrical stress | Joint temperature, current, and voltage signals | Yes | Yes | Moderate | Useful for hybrid RUL-safety modeling |
| Safety rule score | Safety-relevant derived indicators | Aggregated score from predefined safety labeling rules | Derived from threshold and anomaly rules | No | Yes | Moderate | Should be handled carefully to avoid proxy-label duplication |
| Anomaly score | Safety-relevant derived indicators | Measure of deviation from nominal battery behavior | Derived from anomaly detection model or residual logic | No | Yes | Low to Moderate | Useful as a safety-oriented feature only if computed without leakage |

## Methodological Note

This catalog is intended as a comprehensive candidate inventory rather than a mandatory final feature list. The final subset should be determined using:

- dataset availability;
- signal quality;
- leakage control requirements;
- task-specific predictive relevance;
- interpretability considerations;
- feature selection procedures documented in `feature_selection_strategy.md`.
