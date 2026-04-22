# Method Comparison Template

## Purpose

This template is designed to compare prior studies relevant to the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The emphasis here is methodological comparison rather than narrative summary. The table should be used to compare how prior studies define their prediction task, what battery context they examine, what data and features they use, what models they implement, whether explainability is included, how safety is treated, how performance is evaluated, and what limitations remain.

Only studies with a verifiable DOI should be included in this template.

## Method Comparison Table

| Study | Year | DOI | Prediction Target | Battery Type | Data Level (Cell/Module/Pack/Vehicle) | Dataset or Source | Features Used | Model Type | Explainability Approach | Safety-Related Outputs | Evaluation Metrics | Main Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Example Author et al. | 2022 | 10.xxxx/xxxxx | RUL prediction | Lithium-ion NMC cell | Cell | Public aging dataset | Voltage, current, temperature, cycle index, capacity fade | XGBoost | SHAP | No explicit safety output | MAE, RMSE | Single dataset, no external validation, no safety target |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |

## Guidance Notes

### General Use

- Record one study per row.
- Use concise but specific wording so that comparisons across studies remain readable.
- If a study evaluates multiple models, record the primary model or the best-performing model, and note additional models briefly in the same cell if necessary.
- If the same study addresses more than one prediction target, state this clearly in the `Prediction Target` column.

### Column Guidance

#### Study

Record the first author followed by `et al.` where appropriate.

Example:

- `Zhang et al.`

#### Year

Record the publication year of the study.

#### DOI

Record the verified DOI exactly. If a DOI cannot be verified, the study should not be included in this table.

#### Prediction Target

State the primary modeling target as precisely as possible.

Examples:

- `Remaining useful life`
- `State of health`
- `Thermal runaway prediction`
- `Fault diagnosis`
- `Safety risk classification`
- `Multi-task prediction: RUL and SOH`

#### Battery Type

Record the chemistry or battery description reported in the paper.

Examples:

- `Lithium-ion`
- `NMC lithium-ion`
- `LFP battery`
- `EV battery pack`

If the battery type is not clearly stated, write:

- `Not clearly specified`

#### Data Level (Cell/Module/Pack/Vehicle)

State the level at which the data were collected or modeled.

Examples:

- `Cell`
- `Module`
- `Pack`
- `Vehicle`

If multiple levels are used, write:

- `Cell and pack`

#### Dataset or Source

Record whether the study uses:

- a public dataset;
- an experimental dataset;
- a proprietary dataset;
- simulation data; or
- mixed data sources.

Examples:

- `NASA battery dataset`
- `Oxford battery degradation dataset`
- `Laboratory cycling experiment`
- `Proprietary EV fleet data`

#### Features Used

Summarize the main inputs used for modeling. Focus on informative variables rather than exhaustive lists.

Examples:

- `Voltage, current, temperature, capacity`
- `Incremental capacity features, resistance proxies, cycle statistics`
- `Thermal and electrical features from pack-level monitoring`

#### Model Type

Record the main modeling approach.

Examples:

- `Linear regression`
- `Random forest`
- `Support vector machine`
- `LSTM`
- `Transformer`
- `Physics-informed neural network`

If the study compares several methods, use a compact notation such as:

- `RF, XGBoost, LSTM`

#### Explainability Approach

Record the explainability or interpretability method used.

Examples:

- `SHAP`
- `LIME`
- `Attention visualization`
- `Feature importance`
- `Inherently interpretable model`
- `None`

If interpretability is discussed conceptually but not implemented methodologically, record:

- `Conceptual only`

#### Safety-Related Outputs

This column should capture whether the study addresses safety explicitly, indirectly, or not at all.

Examples:

- `No explicit safety output`
- `Fault class prediction`
- `Thermal runaway early warning`
- `Abnormal operating state detection`
- `Indirect safety relevance through SOH or RUL`

#### Evaluation Metrics

Record the principal reported metrics.

Examples:

- `MAE, RMSE`
- `Accuracy, F1-score, AUROC`
- `Precision, recall, F1-score`
- `MAPE, R^2`

If uncertainty metrics are reported, include them briefly.

#### Main Limitations

Summarize the key limitation or limitations relevant to the present project.

Examples:

- `No explainability analysis`
- `Small sample size`
- `Unclear target definition`
- `Single operating condition`
- `No external validation`
- `No explicit safety target`

## Recommended Coding Conventions

- Use `RUL` only if the paper clearly uses remaining useful life as the target.
- Do not treat `battery health`, `state of health`, and `safety risk` as interchangeable labels.
- Distinguish between direct safety outputs and indirect safety relevance.
- When the paper uses a proxy for safety, make that explicit in the `Safety-Related Outputs` or `Main Limitations` column.
- Where the data level is unclear, state the ambiguity rather than inferring it.

## Suggested Analytical Uses

This table can later be used to support:

- comparison of RUL versus safety-oriented prediction studies;
- identification of which battery levels are underrepresented in the literature;
- mapping of feature types to prediction targets;
- comparison of explainability adoption across model families;
- identification of common evaluation metrics and reporting practices; and
- extraction of methodological limitations that justify the present study.
