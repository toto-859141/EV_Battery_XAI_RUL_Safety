# Conceptual Framework

> Revision summary: This version aligns the framework precisely with the study topic by separating battery health as an inferred condition construct from the two modeled outcomes, `target_rul` and `target_safety_risk`, and by linking XAI directly to variable attribution for both tasks.

## Overview

The conceptual framework for this study explains how monitored battery variables are transformed into model inputs, how those inputs support two separate prediction tasks, and how explainable artificial intelligence is used to interpret variable contributions. The framework is specific to the topic of electric vehicle batteries and does not treat battery health, safety risk, and remaining useful life as interchangeable outcomes.

## Core Conceptual Position

The framework distinguishes three layers of meaning:

- `battery health` is an inferred condition construct reflected by degradation-related indicators;
- `target_rul` is a prognostic outcome representing the remaining service life before end-of-life; and
- `target_safety_risk` is a safety-oriented outcome representing the likelihood or level of unsafe or abnormal battery behavior.

The study therefore models `target_rul` and `target_safety_risk` directly, while battery health functions as an intermediate interpretive construct rather than as the main modeled output.

## Framework Components

### 1. Input Layer: Monitored Battery Variables

The framework begins with directly measured battery variables and operating-condition variables, including:

- voltage;
- current;
- temperature;
- cycle count or elapsed time;
- charge-discharge duration; and
- operating-condition metadata such as C-rate, depth of discharge, or ambient temperature, where available.

These variables provide the empirical basis for all subsequent feature construction.

### 2. Transformation Layer: Preprocessing and Feature Engineering

The input variables are processed through cleaning, normalization, segmentation, and feature engineering. This transformation stage produces:

- degradation-oriented features used to represent battery health trends;
- safety-relevant features used to represent abnormal thermal or electrical behavior; and
- task-ready predictor sets for supervised learning.

This layer is essential because neither `target_rul` nor `target_safety_risk` is assumed to be observable directly from raw signals without transformation.

### 3. Modeling Layer: Two Distinct Dependent Variables

The engineered predictor set is then used in two separate supervised learning tasks.

#### A. Prognostic Task

Predict `target_rul` from monitored variables and engineered degradation features.

Interpretive meaning:
This branch estimates how much service life remains before the battery reaches the chosen end-of-life criterion.

#### B. Safety-Oriented Task

Predict `target_safety_risk` from monitored variables and engineered safety-relevant features.

Interpretive meaning:
This branch estimates the likelihood or degree of safety-related concern associated with the observed battery state or operating window.

### 4. Explainability Layer

Explainable artificial intelligence is applied after or alongside model training to determine:

- which variables contribute most to `target_rul` prediction;
- which variables contribute most to `target_safety_risk` prediction; and
- which predictors are shared across tasks versus task-specific.

In this framework, XAI is not treated as a decorative output. It is part of the analytic logic used to evaluate whether the model is relying on technically meaningful predictors.

### 5. Output Layer

The framework yields four classes of outputs:

- predicted values for `target_rul`;
- predicted values or classes for `target_safety_risk`;
- variable-attribution results for each task; and
- comparative evidence about the relationship between degradation-oriented and safety-oriented predictors.

## Relationship Structure

The intended relationships are as follows:

1. Monitored battery variables and operating conditions influence the observable evidence of degradation and abnormal behavior.
2. Preprocessing and feature engineering convert that evidence into predictors suitable for supervised learning.
3. The resulting predictors are used to model `target_rul` and `target_safety_risk` as separate dependent variables.
4. XAI methods are used to interpret the contribution of predictors to each dependent variable.
5. The comparison of XAI results across tasks clarifies where battery health-related predictors overlap with, or diverge from, safety-related predictors.

## Text-Based Conceptual Diagram

```text
Monitored Battery Variables and Operating Conditions
(voltage, current, temperature, cycle history, C-rate, depth of discharge)
            |
            v
Preprocessing and Feature Engineering
(cleaning, normalization, windowing, degradation features, safety-relevant features)
            |
            v
---------------------------------------------------------------
|                                                             |
v                                                             v
Model for target_rul                                  Model for target_safety_risk
(prognostic task)                                     (safety-oriented task)
|                                                             |
---------------------------------------------------------------
            |
            v
Explainable AI
(variable attribution, local explanations, cross-task comparison)
            |
            v
Interpretation of:
- predictors of remaining useful life
- predictors of safety risk
- overlap and separation between the two tasks
```

## Assumptions

This framework assumes that:

- the selected dataset contains sufficient monitored variables for both prediction tasks;
- the definitions of `target_rul` and `target_safety_risk` are explicitly documented;
- the chosen explainability methods are compatible with the final model classes; and
- cross-task comparison of variable importance is methodologically meaningful under the selected preprocessing and evaluation protocol.
