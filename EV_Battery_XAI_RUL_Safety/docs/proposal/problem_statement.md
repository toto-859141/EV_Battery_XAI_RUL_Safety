# Problem Statement

> Revision summary: This version removes general claims, states the research problem in operational terms, clarifies the distinction between battery health, safety risk, and remaining useful life, and makes the study assumptions explicit.

## Overview

Electric vehicle batteries are safety-critical components whose degradation affects operational reliability, maintenance planning, and risk management. In this study, three constructs are treated as related but non-equivalent:

- `battery health`: the condition of the battery relative to its nominal performance, reflected by degradation indicators such as capacity retention and internal resistance growth;
- `safety risk`: the likelihood or severity of unsafe or abnormal battery states, such as overheating, instability, or other hazard-relevant conditions; and
- `remaining useful life (RUL)`: the amount of service life remaining before a defined end-of-life threshold is reached.

This distinction is necessary because a battery with degraded health is not automatically in an unsafe state, and a battery with elevated safety risk is not necessarily near end-of-life under a conventional RUL definition.

## Problem Context

Battery monitoring systems generate data such as voltage, current, temperature, cycle count, and charge-discharge profiles. These signals are widely used for degradation analysis and prognostics. However, published data-driven work often treats:

- RUL prediction as a degradation forecasting task;
- safety analysis as a separate fault, anomaly, or event detection task; and
- explainability as an optional post-processing step rather than a core analytic requirement.

As a result, the literature provides limited guidance on how to build a single research framework that uses monitored battery data to predict both RUL and safety risk while also producing interpretable explanations of model behavior.

## Research Problem

The research problem addressed in this study is the lack of an explainable predictive framework for electric vehicle batteries that can:

1. use monitored battery variables and engineered features as model inputs;
2. estimate `target_rul` as a prognostic outcome;
3. estimate `target_safety_risk` as a safety-oriented outcome; and
4. explain which input variables drive each prediction.

This is a methodological problem because the two prediction targets require related but not identical representations of battery behavior. It is also a practical problem because predictions that cannot be interpreted are difficult to justify in safety-relevant engineering contexts.

## Why the Problem Matters

An RUL model without interpretability provides limited support for deciding whether predicted degradation is associated with normal aging or with abnormal operating conditions. Similarly, a safety risk model without interpretable variable attribution provides limited support for diagnosing whether risk is associated with thermal behavior, electrical instability, or usage conditions. For research and practice, the relevant need is therefore not prediction alone, but prediction plus defensible explanation.

## Scope of the Problem

This study focuses on supervised machine learning applied to battery monitoring data. The research framing does not assume that:

- battery physics are modeled explicitly;
- direct safety-event labels are always available; or
- a single model will necessarily perform best for both RUL and safety risk tasks.

Instead, the study evaluates whether an explainable artificial intelligence workflow can produce task-specific predictions and interpretable variable contributions for both outcomes.

## Assumptions

The problem framing is based on the following explicit assumptions:

- the selected dataset contains sufficient battery monitoring variables to construct predictive features;
- `target_rul` can be defined with reference to a documented end-of-life criterion;
- `target_safety_risk` can be defined either from direct labels or from a justified proxy, which must be documented as part of the methodology; and
- explainability methods can be applied to the selected models in a way that permits variable-level interpretation.

## Statement of the Problem

This study addresses the absence of a clearly defined and interpretable machine learning framework for electric vehicle battery analysis in which monitored battery variables are used to predict both remaining useful life and safety risk as separate dependent variables, and in which explainable artificial intelligence is used to identify the predictors that contribute to each outcome. This absence limits both methodological rigor and the practical usefulness of battery prognostic models in safety-relevant settings.
