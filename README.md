# EV Battery XAI RUL Safety

This project studies explainable artificial intelligence for safety risk and remaining useful life (RUL) prediction of electric vehicle batteries.

## Main Tasks

1. Literature review on EV battery RUL, safety risk, and XAI
2. Data preparation from public or experimental datasets
3. Feature engineering for degradation and safety indicators
4. Model development for:
   - RUL prediction
   - Safety risk prediction
5. Explainability analysis
6. Academic writing support

## Expected Outputs

- Trained ML models
- Explainability reports
- Figures and tables
- Proposal / manuscript drafts

## Project Conventions

### Dataset Sources

Raw datasets should come from one of the following:

- Public battery aging or degradation datasets
- Public safety or abuse-testing datasets
- Internal or experimental datasets collected during lab work

Store all original, unmodified source files in `data/raw/`. If a dataset is downloaded from an external repository or shared by collaborators, add a short note in `data/external/` or project documentation describing:

- dataset name
- source or URL
- access date
- license or usage restrictions
- original file format

### File Naming

Use lowercase file names with underscores and descriptive prefixes.

Recommended patterns:

- Raw data: `datasetname_source_yyyy_mm.csv`
- Processed data: `datasetname_split_stage.parquet`
- Feature tables: `datasetname_features_v01.csv`
- Labels: `datasetname_labels_v01.csv`
- Trained models: `task_modelname_v01.pkl`
- Evaluation reports: `task_experimentname_v01.md`
- Figures: `figure_01_dataset_overview.png`
- Tables: `table_01_model_results.csv`

Examples:

- `nasa_battery_raw_2026_04.csv`
- `nasa_battery_train_clean.parquet`
- `rul_xgboost_v01.pkl`
- `safety_shap_summary_v01.png`

### Target Variable Conventions

Until a specific dataset is finalized, use the following project-wide target definitions:

- `target_rul`: remaining useful life, measured as cycles remaining or time remaining until end-of-life
- `target_eol`: binary indicator that end-of-life threshold has been reached
- `target_safety_risk`: safety risk label, either binary, ordinal, or probability-like score depending on dataset annotation

When working with a dataset, document:

- the exact target definition
- threshold used for end-of-life
- unit of RUL, such as cycles, hours, or days
- whether safety is modeled as classification, regression, or ranking

### Storage Rules

- Keep original source files in `data/raw/`
- Keep third-party reference files or downloaded metadata in `data/external/`
- Keep cleaned datasets, manifests, and feature-ready tables in `data/processed/`
- Save trained models and serialized pipelines in `models/`
- Save figures in `output/figures/`
- Save tables in `output/tables/`
- Save experiment summaries, metrics, and explainability reports in `output/reports/`

Do not overwrite raw data. Each preprocessing stage should produce a new artifact in `data/processed/`.

### Experiment Tracking

Each experiment should record:

- dataset name and version
- train/validation/test split strategy
- target variable used
- feature set version
- model name and hyperparameters
- evaluation metrics
- explainability method
- output file locations

Recommended experiment ID pattern:

- `exp_YYYYMMDD_task_model_shortnote`

Example:

- `exp_20260422_rul_xgboost_baseline`

Use the experiment ID in report names, exported figures, and saved model metadata when possible.
