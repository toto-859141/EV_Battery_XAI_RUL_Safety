# Thematic Synthesis Template

## Purpose

This document provides a thesis-ready template for synthesizing the literature reviewed for the project titled:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The template is designed to be completed after evidence has been extracted into `literature_matrix.md`. It supports:

- theme-by-theme synthesis;
- comparative discussion across studies;
- explicit gap extraction;
- critical analysis beyond descriptive summary; and
- final positioning of the present study.

Only studies with a verifiable DOI should be used in the formal synthesis.

## Instructions for Use

1. Complete the literature matrix before drafting the synthesis.
2. Use the matrix fields consistently, especially:
   - Dataset
   - Features
   - Model
   - Explainability Method
   - Safety Aspect
   - Key Findings
   - Limitations
   - Research Gap
3. Write each theme section as a synthesis, not a list of isolated paper summaries.
4. Distinguish clearly between:
   - battery health monitoring;
   - remaining useful life prediction; and
   - safety risk prediction.
5. State where evidence is strong, inconsistent, limited, or absent.

## Recommended Writing Pattern for Each Theme

Each theme section may be drafted using the following sequence:

1. Introduce the theme and define its relevance to the project.
2. Summarize the dominant approaches found in the literature.
3. Compare datasets, features, models, and explainability methods where relevant.
4. Identify points of agreement and disagreement across studies.
5. Evaluate methodological limitations and unresolved issues.
6. Extract the theme-specific research gap.
7. Link the theme back to the present study.

## Theme 1: EV Battery Remaining Useful Life Prediction

### 1.1 Theme Overview

Write a short paragraph introducing how the literature defines and studies RUL in electric vehicle or lithium-ion battery systems.

Placeholder:

`[Insert overview of how RUL is conceptualized, measured, and modeled in the reviewed studies.]`

### 1.2 Main Approaches Reported in the Literature

Placeholder:

`[Summarize the dominant model families, such as statistical models, machine learning models, and deep learning models.]`

### 1.3 Comparative Synthesis

Use this subsection to compare studies across:

- dataset type and source;
- end-of-life definition;
- predictor variables and engineered features;
- model family;
- evaluation metrics;
- presence or absence of interpretability.

Comparative discussion prompts:

- Which datasets are used most often for RUL prediction?
- How consistently is end-of-life defined across studies?
- Which features recur most frequently in high-performing models?
- Do more complex models outperform simpler models consistently?
- How often do RUL studies include explainability methods?

Placeholder:

`[Insert comparative synthesis for RUL studies.]`

### 1.4 Critical Analysis

Use this subsection to move beyond description.

Critical analysis prompts:

- Are reported gains in predictive performance practically meaningful?
- Do the reviewed studies justify their feature choices adequately?
- Are models validated across datasets or only within one dataset?
- Is interpretability treated as essential or optional?
- Are claims about generalizability supported by the evidence presented?

Placeholder:

`[Insert critical analysis of RUL literature.]`

### 1.5 Theme-Specific Gap

Gap extraction prompts:

- What is still unresolved in RUL prediction for EV batteries?
- What is missing in relation to interpretability?
- What prevents direct transfer from RUL prediction to safety-oriented decision support?

Placeholder:

`[Insert theme-specific research gap for RUL literature.]`

## Theme 2: Battery Safety Risk Prediction

### 2.1 Theme Overview

Placeholder:

`[Insert overview of how safety risk, faults, thermal runaway precursors, abnormal states, or hazard-related outcomes are defined in the literature.]`

### 2.2 Main Approaches Reported in the Literature

Placeholder:

`[Summarize the main predictive or diagnostic approaches used for safety-related outcomes.]`

### 2.3 Comparative Synthesis

Compare studies across:

- definition of safety outcome;
- direct versus proxy labels;
- time horizon of prediction or warning;
- monitored variables and sensor inputs;
- treatment of class imbalance;
- interpretability or explanation methods.

Comparative discussion prompts:

- Is safety risk modeled directly, or inferred through faults and anomalies?
- Which variables are most commonly used for safety-oriented prediction?
- How early do studies claim to identify unsafe behavior?
- Are safety studies predictive, diagnostic, or descriptive?
- How often do safety studies include interpretable machine learning?

Placeholder:

`[Insert comparative synthesis for safety risk literature.]`

### 2.4 Critical Analysis

Critical analysis prompts:

- Are safety targets clearly defined and justified?
- Do studies distinguish between failure detection and safety risk prediction?
- Are the reported methods useful for early intervention, or only for event recognition?
- Are explanation methods used to support trust in safety claims?
- Are limitations in labels, events, or proxies acknowledged sufficiently?

Placeholder:

`[Insert critical analysis of safety risk literature.]`

### 2.5 Theme-Specific Gap

Gap extraction prompts:

- What remains unclear about modeling safety risk as a predictive target?
- What methodological weaknesses recur across safety studies?
- What is missing at the intersection of safety prediction and explainability?

Placeholder:

`[Insert theme-specific research gap for safety risk literature.]`

## Theme 3: Battery Health Monitoring

### 3.1 Theme Overview

Placeholder:

`[Insert overview of how battery health is monitored, estimated, or inferred in the literature.]`

### 3.2 Main Approaches Reported in the Literature

Placeholder:

`[Summarize common health indicators, monitoring frameworks, and estimation methods.]`

### 3.3 Comparative Synthesis

Compare studies across:

- health indicators used;
- sensing requirements;
- feature stability under varying operating conditions;
- relationship to downstream RUL or safety tasks;
- level of interpretability provided.

Comparative discussion prompts:

- Which indicators are most commonly used to represent battery health?
- How do health-monitoring studies connect to RUL estimation?
- How often is health linked explicitly to safety?
- Are the variables used in health studies transferable to predictive models?

Placeholder:

`[Insert comparative synthesis for battery health monitoring literature.]`

### 3.4 Critical Analysis

Critical analysis prompts:

- Do health studies treat battery health as a measurable target or as an inferred construct?
- Are the proposed indicators robust across datasets or operating conditions?
- Is the relationship between battery health and safety supported directly or assumed implicitly?
- Are monitoring methods suitable for real-world EV operating conditions?

Placeholder:

`[Insert critical analysis of battery health monitoring literature.]`

### 3.5 Theme-Specific Gap

Gap extraction prompts:

- What is missing in the transition from health monitoring to predictive decision support?
- Which health indicators appear underused in RUL or safety studies?
- Where does the literature fail to separate health from risk and useful life?

Placeholder:

`[Insert theme-specific research gap for battery health monitoring literature.]`

## Theme 4: Explainable AI for Prognostics

### 4.1 Theme Overview

Placeholder:

`[Insert overview of how explainable AI is used in prognostics, predictive maintenance, degradation modeling, or related battery studies.]`

### 4.2 Main Approaches Reported in the Literature

Placeholder:

`[Summarize the main explanation methods reported, such as SHAP, LIME, attention-based interpretation, saliency, or feature attribution.]`

### 4.3 Comparative Synthesis

Compare studies across:

- model-specific versus model-agnostic XAI;
- global versus local explanations;
- static versus time-series explanation strategies;
- validation of explanations;
- contribution of XAI to scientific understanding.

Comparative discussion prompts:

- Which XAI methods are most common in prognostic applications?
- Are explanations used to validate models or only to describe them?
- Do studies connect explanations to physical battery behavior?
- How do explanation methods differ for tabular and sequential models?

Placeholder:

`[Insert comparative synthesis for explainable AI in prognostics.]`

### 4.4 Critical Analysis

Critical analysis prompts:

- Are explanations stable, interpretable, and technically meaningful?
- Do studies evaluate explanation quality explicitly?
- Are explanation results used to revise models, features, or target definitions?
- Is there evidence that XAI improves decision usefulness rather than presentation only?

Placeholder:

`[Insert critical analysis of XAI for prognostics literature.]`

### 4.5 Theme-Specific Gap

Gap extraction prompts:

- What remains weak in the use of XAI for battery prognostics?
- Are explanation methods applied to multiple outcomes or only single-task models?
- What is still missing for XAI to support both safety and RUL prediction?

Placeholder:

`[Insert theme-specific research gap for explainable AI literature.]`

## Theme 5: Interpretable Machine Learning for Safety-Critical Systems

### 5.1 Theme Overview

Placeholder:

`[Insert overview of why interpretability is treated as necessary in safety-critical systems, including battery and adjacent engineering domains.]`

### 5.2 Main Approaches Reported in the Literature

Placeholder:

`[Summarize major approaches to interpretable or trustworthy machine learning in safety-critical settings.]`

### 5.3 Comparative Synthesis

Compare studies across:

- domain of application;
- level of risk sensitivity;
- interpretability requirement;
- auditability and traceability mechanisms;
- trade-off between model complexity and interpretability.

Comparative discussion prompts:

- What types of interpretability are considered sufficient in safety-critical systems?
- How is trust justified in these studies?
- Are interpretable models preferred over black-box models in high-risk settings?
- Which principles can be transferred to EV battery analytics?

Placeholder:

`[Insert comparative synthesis for interpretable machine learning in safety-critical systems.]`

### 5.4 Critical Analysis

Critical analysis prompts:

- Are interpretability claims grounded in actual user or engineering needs?
- Do studies distinguish transparency from post hoc explanation?
- Is the performance-interpretability trade-off discussed rigorously?
- Which lessons are directly relevant to battery prognostics, and which are not?

Placeholder:

`[Insert critical analysis of safety-critical interpretability literature.]`

### 5.5 Theme-Specific Gap

Gap extraction prompts:

- What interpretability requirements are still insufficiently addressed for battery applications?
- What lessons from adjacent domains have not yet been translated to battery analytics?
- What remains missing for technically defensible safety-oriented battery prediction?

Placeholder:

`[Insert theme-specific research gap for interpretable machine learning in safety-critical systems.]`

## Cross-Theme Comparative Synthesis

### Purpose

This section should integrate findings across all five themes rather than repeating the earlier summaries.

### Comparative Discussion Prompts

- Which monitored battery variables recur across RUL, health, and safety studies?
- Which features appear most relevant to both prognostic and safety-oriented tasks?
- How consistently are `battery health`, `safety risk`, and `RUL` distinguished across the literature?
- Which model families recur across multiple themes?
- How often is XAI used as a core analytical method rather than a post hoc supplement?
- Where do target definitions vary enough to complicate comparison?
- Which methodological weaknesses recur across the literature regardless of theme?

Placeholder:

`[Insert cross-theme synthesis.]`

## Cross-Theme Critical Analysis

This subsection should state the strongest interpretive judgments supported by the reviewed literature.

Critical analysis prompts:

- Is the literature methodologically fragmented or converging?
- Are target definitions sufficiently standardized for cumulative knowledge-building?
- Does existing work support a joint framework for RUL and safety risk prediction?
- Is interpretability treated as technically necessary in battery prediction research?
- Are current studies adequate for safety-relevant engineering use, or mainly proof-of-concept?

Placeholder:

`[Insert cross-theme critical analysis.]`

## Final Research Gap Extraction

This section should identify the strongest unresolved gap after reviewing all themes together.

Gap extraction prompts:

- What exact methodological gap remains at the intersection of EV battery RUL prediction, safety risk prediction, and explainable AI?
- Which variables, target definitions, or model evaluation practices remain insufficiently integrated?
- What has not yet been demonstrated convincingly in the reviewed literature?
- Why is the unresolved gap academically significant and practically relevant?

Placeholder:

`[Insert final integrated research gap.]`

## Positioning of the Present Study

### Purpose

This section should explain precisely how the current study responds to the literature.

### Positioning Prompts

- Which gap does the study address directly?
- How does the study distinguish battery health, safety risk, and RUL?
- What variables or monitored signals will be emphasized?
- Why is XAI included as a core methodological component rather than an optional add-on?
- How does the proposed study improve on limitations identified in prior work?
- What is the expected scholarly contribution?
- What is the expected practical contribution for battery prognostics and safety-oriented decision support?

Placeholder:

`[Insert positioning statement for the present study.]`

## Optional Closing Synthesis Paragraph

Use this short closing paragraph to transition from the literature review chapter to the research gap, objectives, or methodology chapter.

Placeholder:

`[Insert closing synthesis paragraph that leads into the proposal or thesis argument.]`
