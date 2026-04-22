# Experiment Tracking Plan

## Purpose

This document defines a research workflow for tracking experiments in the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The purpose of experiment tracking is to ensure that every modeling result can be traced to:

- the dataset and preprocessing version used;
- the feature set and target definition applied;
- the model family and hyperparameters selected;
- the outputs and evaluation metrics produced.

In this project, experiment tracking is not treated as a secondary engineering convenience. It is part of the methodological foundation required for reproducibility, comparison, and academically defensible reporting.

## Core Tracking Principles

Each experiment should satisfy the following principles:

1. It must have a unique identifier.
2. Its inputs and parameters must be recorded explicitly.
3. Its outputs must be saved in predictable locations.
4. Its model artifact must be linked to the exact experiment configuration.
5. Its results must be reproducible from saved metadata and code references.

## Experiment Naming Convention

## Recommended Experiment ID Format

The recommended experiment identifier is:

`exp_YYYYMMDD_task_model_shortnote`

## Components of the Identifier

### `YYYYMMDD`

The calendar date on which the experiment is created or first run.

### `task`

The primary prediction task or experiment type.

Examples:

- `rul`
- `safety`
- `multitask`
- `ablation`
- `xai`

### `model`

The principal model family or approach.

Examples:

- `ridge`
- `rf`
- `xgboost`
- `lstm`
- `tcn`
- `transformer`

### `shortnote`

A brief descriptive suffix used to distinguish closely related runs.

Examples:

- `baseline`
- `fullfeatures`
- `thermalonly`
- `sharedbackbone`
- `v02`

## Example Experiment IDs

- `exp_20260422_rul_xgboost_baseline`
- `exp_20260422_safety_rf_thermalonly`
- `exp_20260423_multitask_lstm_sharedbackbone`
- `exp_20260424_ablation_xgboost_nothermal`

## Naming Recommendation

The experiment identifier should be used consistently in:

- result files;
- trained model files;
- report filenames;
- exported figures and tables;
- configuration logs.

## Parameter Logging

## Minimum Parameter Set

Each experiment should record the following parameters:

- experiment ID;
- task definition;
- dataset name;
- dataset version;
- preprocessing version;
- feature set version;
- target label definition version;
- train/validation/test split strategy;
- model family;
- model hyperparameters;
- evaluation metrics used;
- random seed or seeds;
- explainability method, if applied.

## Recommended Logging Format

Each experiment should generate a configuration file in a structured format such as:

- `yaml`
- `json`

Recommended filename:

- `output/reports/<experiment_id>_config.yaml`

## Suggested Parameter Sections

### Dataset Section

- dataset name
- raw source reference
- processed file path
- number of observations
- battery level, such as cell, module, pack, or vehicle

### Feature Section

- feature table path
- feature set name
- included feature groups
- excluded feature groups
- scaling or normalization settings

### Target Section

- target variable name
- target definition
- end-of-life criterion for RUL, where relevant
- safety-risk labeling rule, where relevant

### Model Section

- model class
- hyperparameters
- training procedure
- loss function, where relevant

### Evaluation Section

- split definition
- evaluation metrics
- thresholding logic for classification, where relevant

### Reproducibility Section

- random seed
- software environment notes
- script path or module name
- code version reference, if available

## Model Version Tracking

## Purpose

Model version tracking ensures that saved artifacts correspond to specific experiment definitions rather than to unnamed or overwritten model files.

## Recommended Model File Naming

Model artifacts should use filenames such as:

- `models/<experiment_id>_model.pkl`
- `models/<experiment_id>_pipeline.pkl`
- `models/<experiment_id>_weights.pt`

The exact extension may vary by framework, but the experiment ID should always remain part of the filename.

## What Should Be Versioned

The following should be versioned explicitly:

- trained model artifacts;
- preprocessing pipeline objects;
- feature-scaling objects;
- label-encoding objects;
- model checkpoints, where applicable.

## Versioning Recommendation

Do not overwrite a previous model artifact if:

- the feature set changes;
- the label definition changes;
- the split changes;
- the hyperparameters change;
- the code logic changes materially.

Instead, create a new experiment ID or a new descriptive suffix.

## Results Storage

## Recommended Storage Locations

### Reports

Store experiment summaries in:

- `output/reports/`

Recommended filenames:

- `output/reports/<experiment_id>_report.md`
- `output/reports/<experiment_id>_metrics.json`

### Figures

Store plots in:

- `output/figures/`

Recommended filenames:

- `output/figures/<experiment_id>_feature_importance.png`
- `output/figures/<experiment_id>_prediction_error.png`

### Tables

Store result tables in:

- `output/tables/`

Recommended filenames:

- `output/tables/<experiment_id>_results.csv`
- `output/tables/<experiment_id>_ablation.csv`

### Models

Store trained models in:

- `models/`

## Minimum Result Package Per Experiment

Each completed experiment should ideally produce:

1. one configuration file;
2. one metrics file;
3. one narrative report or summary note;
4. one saved model or explicit note that no model artifact was stored;
5. optional figures and tables.

## Reproducibility Maintenance

## Core Requirement

An experiment should be reproducible without relying on memory or informal notes.

## Required Reproducibility Practices

### 1. Fixed Random Seeds

Record all random seeds used in:

- data splitting;
- model initialization;
- training procedures;
- hyperparameter search.

### 2. Fixed Data References

Record the exact processed dataset file path or dataset version used in the experiment.

### 3. Fixed Feature References

Record:

- the feature table path;
- the feature groups included;
- the feature-selection procedure, if any.

### 4. Fixed Label References

Record the exact target definition used, especially for:

- `target_rul`, including end-of-life rule;
- `target_safety_risk`, including any proxy labeling logic.

### 5. Fixed Code References

Record the script or module used to run the experiment.

Recommended examples:

- `src/modeling/train_rul_baseline.py`
- `src/modeling/train_safety_baseline.py`
- `src/modeling/train_multitask_model.py`

If version control is later introduced formally, record the commit hash or equivalent code version reference.

### 6. Fixed Environment Notes

Where possible, record:

- Python version;
- key package versions;
- hardware notes when relevant for deep learning experiments.

## Suggested Experiment Report Structure

Each experiment report in `output/reports/` should include the following sections:

### 1. Experiment Overview

- experiment ID
- date
- objective

### 2. Inputs

- dataset
- feature set
- target definition
- split strategy

### 3. Model Configuration

- model type
- hyperparameters
- training setup

### 4. Results

- primary metrics
- secondary metrics
- comparison to baseline

### 5. Interpretation

- key observations
- explanation results, if available
- notable failure cases or limitations

### 6. Reproducibility Notes

- random seed
- file paths
- script used

## Recommended Workflow

The recommended tracking workflow is:

1. assign the experiment ID before training begins;
2. save the configuration file before or at run start;
3. save metrics and artifacts immediately after training;
4. write a short narrative report after reviewing the results;
5. avoid renaming files in a way that breaks the experiment ID linkage.

## Practices to Avoid

The following practices should be avoided:

- unnamed experiment runs;
- overwritten model files without version distinction;
- manually edited metrics without corresponding configuration updates;
- storing key results only in notebooks without exported records;
- changing label definitions or feature sets without changing the experiment ID or version suffix.

## Recommended Conclusion

In this project, experiment tracking should function as a formal research control mechanism. A well-tracked experiment is one in which the model artifact, metrics, data references, feature definitions, target definitions, and explanatory outputs all point to the same explicit experiment identifier. This discipline is necessary for reliable comparison of RUL models, safety-risk models, and multi-task models, and it is especially important for a study that aims to balance predictive performance with explainability and methodological rigor.
