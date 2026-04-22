# Abstract Template

## Abstract

Electric vehicle batteries are safety-critical energy storage systems whose operational value depends on both long-term durability and safe performance under varying usage conditions. Existing data-driven studies have often treated remaining useful life prediction, battery safety analysis, and model interpretability as partially separate research problems. This separation limits the development of predictive frameworks that are both accurate and technically interpretable in safety-relevant contexts.

This study proposes an explainable artificial intelligence framework for safety risk prediction and remaining useful life prediction in electric vehicle batteries. The framework is designed to use battery monitoring data, including electrical, thermal, degradation-related, and operational variables, to model two distinct but related outcomes: remaining useful life and safety risk. The study further examines how explainability methods can be used to identify the monitored variables and engineered features that contribute most strongly to each prediction task.

Methodologically, the study develops a structured pipeline for data preparation, feature engineering, target definition, model development, evaluation, and explanation analysis. Remaining useful life is treated as a prognostic regression target defined relative to an explicit end-of-life criterion, whereas safety risk is treated as a safety-oriented classification or risk-labeling task defined using direct labels, event-based labels, or carefully documented proxy rules, depending on dataset availability. Baseline and advanced machine learning models are compared in terms of predictive performance, interpretability, and safety relevance.

The expected contribution of the study is threefold. First, it provides a clearer conceptual distinction between battery health, safety risk, and remaining useful life in battery analytics. Second, it develops a modeling framework in which safety risk and remaining useful life are treated as separate predictive tasks while remaining analytically comparable through shared monitoring variables and explainability analysis. Third, it contributes a methodology for interpreting model outputs in a manner that is more useful for safety-critical battery monitoring than accuracy-focused black-box prediction alone.

Keywords:

- electric vehicle batteries
- remaining useful life
- safety risk prediction
- explainable artificial intelligence
- battery prognostics
