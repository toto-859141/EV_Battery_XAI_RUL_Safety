# Literature Review Theme Structure

## Purpose

This document defines the thematic structure for the literature review supporting the project titled:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The structure is intended to organize published studies into analytically distinct but related areas. The review should include only peer-reviewed or otherwise scholarly research articles for which a DOI is available and verifiable.

## Review Scope

The literature review is organized around five major themes:

1. EV battery remaining useful life prediction
2. Battery safety risk prediction
3. Battery health monitoring
4. Explainable AI for prognostics
5. Interpretable machine learning for safety-critical systems

These themes should be treated as complementary rather than interchangeable. In particular:

- battery health monitoring concerns the measurement or estimation of battery condition;
- remaining useful life concerns the time or cycles remaining before end-of-life;
- safety risk concerns hazardous, abnormal, or failure-relevant conditions; and
- explainability concerns interpretation of model behavior, not battery state itself.

## Theme 1: EV Battery Remaining Useful Life Prediction

### Focus

This theme covers studies that estimate the remaining service life of lithium-ion or electric vehicle batteries using empirical, statistical, or machine learning approaches.

### Typical Questions

- How is RUL defined and measured?
- What datasets and degradation indicators are used?
- Which models achieve strong predictive performance?
- How are uncertainty and generalization addressed?

### Suggested Subsections

- RUL definitions and end-of-life criteria
- Data sources and benchmark datasets
- Feature engineering for degradation modeling
- Machine learning and deep learning methods
- Evaluation metrics for RUL prediction
- Limitations related to transferability and interpretability

## Theme 2: Battery Safety Risk Prediction

### Focus

This theme covers studies that predict battery faults, abnormal operating states, thermal instability, thermal runaway precursors, or other safety-relevant outcomes.

### Typical Questions

- How is safety risk operationalized?
- Are safety labels direct, proxy-based, or event-based?
- Which variables are associated with hazardous behavior?
- How early can unsafe conditions be detected or predicted?

### Suggested Subsections

- Fault diagnosis versus safety risk prediction
- Thermal runaway and thermal instability studies
- Abnormality detection and early warning methods
- Safety-related features and sensor variables
- Challenges in target definition and class imbalance

## Theme 3: Battery Health Monitoring

### Focus

This theme covers methods for estimating, tracking, or interpreting battery condition, including state of health, degradation progression, and diagnostic indicators relevant to long-term performance.

### Typical Questions

- Which indicators are used to represent battery health?
- How do health indicators relate to RUL and safety?
- What monitoring strategies are feasible using available battery signals?

### Suggested Subsections

- State-of-health estimation methods
- Capacity fade and resistance growth indicators
- Signal-based health monitoring under operational variability
- Relationship between health indicators and downstream prediction tasks

## Theme 4: Explainable AI for Prognostics

### Focus

This theme covers studies that apply explainable artificial intelligence or related interpretation methods to prognostics, predictive maintenance, degradation modeling, or time-series prediction.

### Typical Questions

- Which XAI methods are used for prognostic models?
- Are explanations global, local, model-specific, or model-agnostic?
- How are explanations validated?
- Do explanations improve scientific interpretability or only post hoc description?

### Suggested Subsections

- SHAP, LIME, feature attribution, and surrogate explanations
- Global versus local interpretability in prognostics
- Interpretation of time-series and sequential models
- Limits of post hoc explanation for degradation forecasting

## Theme 5: Interpretable Machine Learning for Safety-Critical Systems

### Focus

This theme covers studies from battery applications and adjacent safety-critical domains in which interpretability is treated as necessary for trust, auditability, or decision support.

### Typical Questions

- Why is interpretability required in safety-critical settings?
- What forms of interpretability are considered adequate?
- How is the trade-off between predictive performance and interpretability handled?
- What lessons can transfer from other safety-critical domains to battery analytics?

### Suggested Subsections

- Interpretability requirements in safety-critical engineering
- Auditable machine learning in risk-sensitive domains
- Human-centered use of explanations in technical decision support
- Limits of black-box models in safety-relevant applications

## Cross-Theme Synthesis Questions

The final literature review should synthesize the five themes using the following questions:

1. Which monitored battery variables recur across RUL, health, and safety studies?
2. How consistently are safety-related targets defined in the literature?
3. Which model families are most common across the five themes?
4. How often are explainability methods used to compare multiple battery outcomes rather than only one outcome?
5. What methodological gap remains at the intersection of RUL prediction, safety risk prediction, and explainable AI?

## DOI Requirement

Only studies with a verifiable DOI should be included in the main review matrix and thematic synthesis. If a relevant source lacks a DOI, it may be recorded separately as background reading, but it should not be treated as core evidence for the formal review.
