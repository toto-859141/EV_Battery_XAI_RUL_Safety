# Feature Grouping Table

## Purpose

This table organizes the proposed feature space for the project into interpretable groups that can be used consistently across:

- exploratory analysis;
- classical machine learning;
- hybrid deep learning;
- explainability analysis.

## Feature Grouping Table

| Feature Group | Feature Name | Definition | Why It Matters | Supports RUL, Safety, or Both | Interpretable | Notes for Classical ML | Notes for Deep Learning |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Electrical behavior | Mean voltage | Average voltage within the observation window | Summarizes electrical state and response level | Both | Yes | Useful as direct tabular input | Can be combined with raw voltage sequence |
| Electrical behavior | Voltage range | Max minus min voltage within the window | Captures electrical fluctuation and instability | Both | Yes | Useful summary statistic | Complements learned sequence embeddings |
| Electrical behavior | Voltage slope | Rate of voltage change over the window | Reflects dynamic charge-discharge response | Both | Partly | Useful engineered derivative feature | May overlap with learned temporal dynamics |
| Electrical behavior | Mean current | Average current within the window | Represents loading intensity | Both | Yes | Core baseline feature | Useful as contextual scalar input |
| Electrical behavior | Peak current | Maximum absolute current in the window | Captures high-stress current demand | Both | Yes | Strong stress indicator | Useful alongside raw current sequence |
| Electrical behavior | Current variability | Dispersion of current values | Reflects unstable or varying operation | Both | Yes | Good for tree-based models | Can supplement learned temporal variability |
| Electrical behavior | Current spike count | Count of current spikes above threshold | Signals abrupt electrical stress events | Safety | Yes | Interpretable event-count feature | Useful as auxiliary summary input |
| Electrical behavior | Voltage-current consistency indicator | Deviation from expected voltage-current relationship | May identify abnormal electrochemical behavior | Safety | Partly | Useful if explicitly defined | Can complement learned relational patterns |
| Thermal behavior | Mean temperature | Average temperature within the window | Summarizes thermal operating level | Both | Yes | Strong baseline thermal feature | Useful scalar context variable |
| Thermal behavior | Maximum temperature | Highest temperature in the window | Directly relevant to thermal hazard concern | Safety | Yes | Important safety feature | Useful summary even with raw sequence input |
| Thermal behavior | Temperature range | Max minus min temperature | Captures thermal instability | Both | Yes | Good variability indicator | Complements raw thermal series |
| Thermal behavior | Temperature rise rate | Rate of temperature increase | Rapid heating may indicate unsafe progression | Safety | Yes | Strong rule-based feature | Useful supervisory feature for hybrid models |
| Thermal behavior | Temperature variance | Dispersion of temperature values | Reflects unstable thermal behavior | Safety | Yes | Useful for anomaly-sensitive models | Can complement learned variance patterns |
| Thermal behavior | Temperature excursion count | Number of threshold exceedances | Interpretable warning indicator | Safety | Yes | Good for rule-aware models | Useful as auxiliary event-count input |
| Thermal behavior | Thermal recovery time | Time to return toward baseline temperature | Reflects dissipation and stress persistence | Both | Partly | Useful if timestamps are reliable | Less essential if model learns full thermal trajectory |
| Degradation indicators | Capacity retention | Usable capacity relative to nominal capacity | Direct indicator of degradation status | RUL | Yes | Core prognostic feature | Can be included as summary target context |
| Degradation indicators | Capacity fade rate | Recent rate of capacity loss | Captures degradation velocity | RUL | Yes | Strong engineered feature | Useful alongside sequential capacity history |
| Degradation indicators | Internal resistance proxy | Estimated or measured resistance growth | Associated with aging and thermal burden | Both | Partly | Important if robustly measured | Useful scalar feature in hybrid setting |
| Degradation indicators | Coulombic efficiency | Ratio of discharge to charge capacity | Reflects electrochemical efficiency loss | RUL | Yes | Useful in structured cycle data | Can be embedded as per-cycle scalar input |
| Degradation indicators | Energy efficiency | Ratio of output to input energy | Summarizes performance loss and internal losses | RUL | Yes | Useful summary metric | Complements raw power-related sequences |
| Degradation indicators | Cycle-to-cycle degradation change | Change in degradation metric across recent windows | Captures acceleration in aging | RUL | Partly | Useful trend feature | Deep models may learn similar progression implicitly |
| Degradation indicators | Voltage curve summary descriptor | Compact descriptor of charge-discharge curve shape | Encodes degradation-relevant response structure | Both | Partly | Useful when carefully defined | May be optional if using full voltage sequences |
| Operational usage patterns | Charge duration | Duration of charging in the window | Represents charging behavior and stress context | Both | Yes | Useful contextual feature | Useful scalar context input |
| Operational usage patterns | Discharge duration | Duration of discharge in the window | Represents use intensity and demand profile | Both | Yes | Useful contextual feature | Useful scalar context input |
| Operational usage patterns | Depth of discharge | Fraction of usable capacity withdrawn | Known driver of degradation and stress | Both | Yes | Core physically meaningful feature | Strong contextual feature for hybrid models |
| Operational usage patterns | Charge rate | Effective charging C-rate | Aggressive charging affects degradation and safety | Both | Yes | Strong contextual stress feature | Useful scalar context input |
| Operational usage patterns | Discharge rate | Effective discharge C-rate | High-rate discharge increases stress | Both | Yes | Strong contextual stress feature | Useful scalar context input |
| Operational usage patterns | Energy throughput | Cumulative energy processed | Summarizes usage burden and wear | RUL | Yes | Useful long-term wear feature | Useful global history feature |
| Operational usage patterns | Rest duration | Idle time between active periods | Affects relaxation behavior and signal interpretation | Both | Yes | Useful contextual control feature | May help sequence interpretation |
| Operational usage patterns | High-stress operation frequency | Frequency of high-load, high-heat, or deep-discharge intervals | Aggregates repeated stress exposure | Both | Yes | Good compact risk-and-wear feature | Useful summary input with raw sequences |

## Interpretation Notes

### Supports RUL, Safety, or Both

This column indicates the expected primary task relevance of the feature:

- `RUL` for long-horizon degradation and end-of-life prediction;
- `Safety` for abnormality or hazard-relevant prediction;
- `Both` when the feature is plausibly informative for both tasks.

### Interpretable

Interpretability is marked as:

- `Yes` when the feature has a direct physical or operational meaning;
- `Partly` when the feature remains meaningful but depends on derivation details.

## Use Recommendation

For classical machine learning, the table should be treated as a candidate engineered feature inventory. For deep learning, the table should be treated as a companion summary-feature set that may be used:

- as standalone inputs in hybrid models;
- as auxiliary context variables;
- as post hoc interpretable reference variables when the main model uses raw sequences.
