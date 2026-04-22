# Literature Gap Synthesis

## Purpose

This document synthesizes the evidence currently recorded in [literature_matrix.md](/Users/tongjaiyampaka/Desktop/EV_Battery_XAI_RUL_Safety/docs/literature_review/literature_matrix.md). The synthesis is limited to the populated matrix entries and does not introduce claims that cannot be traced to those papers.

The discussion distinguishes between:

- `well-supported trends`: patterns visible across multiple papers or across more than one theme; and
- `emerging but limited evidence`: patterns visible in only a small number of papers or in narrowly scoped studies.

## 1. Dominant Research Themes

### Well-Supported Trends

The literature in the matrix is organized around five dominant themes, and the strongest concentration of studies appears in:

- `XAI / interpretable ML`
- `Battery prognostics`
- `RUL prediction`
- `Safety / anomaly / fault diagnosis`
- `Multi-task / hybrid modeling`

Across the matrix, two broader thematic directions are especially clear.

First, there is a strong stream of work on battery prognostics and health management. This includes review papers that focus on degradation mechanisms, prognostic workflows, uncertainty-aware diagnosis and prognosis, and machine-learning-based PHM pipelines. These studies provide methodological framing for battery health analytics, including data acquisition, feature engineering, and prognostic design.

Second, there is a growing stream of data-driven prediction work that splits into two application branches:

- long-horizon degradation or RUL prediction; and
- safety-oriented anomaly, fault, or early-warning detection.

These branches are both active, but they are usually treated separately.

### Emerging but Limited Evidence

A smaller but increasingly visible theme is the use of explainability and interpretability in battery analytics. The matrix includes several papers that use SHAP or interpretable pattern-recognition logic, but most of these are concentrated in:

- RUL interpretation;
- SOH interpretation; or
- operational degradation monitoring.

The matrix also shows emerging interest in multi-task and hybrid frameworks, especially for combining multiple outputs or transferring knowledge across conditions. However, this remains less mature than the prognostics and single-task modeling literature.

## 2. Common Datasets

### Well-Supported Trends

The most recurrent public or named datasets in the matrix are:

- Stanford-MIT fast-charging aging dataset
- Cambridge Cavendish Laboratory battery aging / EIS dataset
- NDANEV real-world vehicle-operation data

The Stanford-MIT dataset appears in the RUL and XAI-related RUL literature, especially for cell-level degradation prediction and early-life battery forecasting. The Cambridge Cavendish dataset appears in EIS-based SOH or prognosis studies, particularly where impedance-derived health indicators are central. NDANEV appears in the multi-fault diagnosis and prognostics paper and represents a real-world EV operational dataset.

The matrix also includes:

- proprietary heavy-duty electric bus data;
- real-world electric mining truck data;
- actual pre-fault EV operating data from three situations; and
- several review papers that are not tied to a single dataset.

### Emerging but Limited Evidence

There is no single dominant benchmark dataset shared across all five themes. Instead, the matrix suggests that dataset choice is fragmented by task:

- RUL papers often rely on cell-level degradation datasets;
- safety papers more often use proprietary or application-specific operational data;
- XAI papers often use whichever dataset is convenient for the prediction task rather than a common interpretability benchmark.

This means dataset commonality is present, but only within substreams rather than across the full problem space.

## 3. Common Input Features

### Well-Supported Trends

The most common input features across the matrix are:

- voltage
- current
- temperature
- SOC or related operating-state variables
- capacity or degradation-trajectory information

These variables appear repeatedly across RUL, fault diagnosis, prognostics, and multi-fault early warning. In operational studies, voltage and temperature are especially prominent in anomaly detection and warning logic. In prognostics and RUL studies, degradation trajectories, discharge fragments, or time-indexed health indicators are commonly used.

Another visible feature class is impedance-derived information. The Cambridge-based studies use:

- EIS spectra;
- real and imaginary impedance components; and
- engineered impedance-health indicators.

These are common in the XAI-plus-SOH and transfer-learning prognosis papers, but they are not common across the whole matrix.

### Emerging but Limited Evidence

More specialized feature constructions include:

- entropy-related and phase-space features for mining-truck fault detection;
- dimensionless indicators extracted from voltage signals;
- multi-feature extraction for transformer-based RUL models;
- online pre-failure patterns derived from SoH-linked sensor behavior.

These appear in individual studies, but the matrix does not show them as broadly recurring across themes.

## 4. Common Model Families

### Well-Supported Trends

The dominant model families in the matrix are deep learning and hybrid deep-learning architectures. Common examples include:

- CNN-LSTM
- TCN-LSTM
- GRU-Attention
- autoencoder-based anomaly detection
- transformer-family models such as Informer

Hybridization is a recurring pattern. Several papers combine:

- sequence models with decomposition methods;
- neural networks with Gaussian process regression;
- neural models with Bayesian optimization;
- transfer learning with GRU-attention architectures;
- autoencoders with thresholding or anomaly scoring;
- deep learning with interpretable or pruning layers.

Review papers also reinforce that machine-learning PHM and hybrid frameworks are central to recent battery analytics.

### Emerging but Limited Evidence

Multi-task learning appears as an emerging model family rather than a dominant one. The multi-task review provides strong conceptual support, and one joint diagnosis-prognostics paper shows hybrid multi-output modeling behavior, but the matrix does not yet show a large empirical literature on battery-specific multi-task frameworks that jointly model RUL and safety-oriented outcomes with explanation.

Classical machine-learning families do appear in the explainable EIS-based SOH protocol, especially:

- random forest
- boosting families
- CatBoost
- LightGBM
- XGBoost

However, in the current matrix these are more visible in XAI/SOH work than in the broader combined literature.

## 5. Common Explainability Methods

### Well-Supported Trends

The most common explainability method in the matrix is `SHAP`. It appears in:

- interpretable deep-learning RUL prediction;
- PSO-enhanced deep learning for SOH;
- explainable ensemble SOH prediction.

This makes SHAP the clearest recurring post hoc explanation method in the matrix.

The matrix also includes other interpretability forms, such as:

- multimodal decoupling and latent-space visualization;
- interpretable pattern recognition and logical reasoning;
- global interpretability analysis tied to feature-space decomposition.

### Emerging but Limited Evidence

Although explainability is clearly present, it is still limited in scope. Most studies with explicit explainability focus on:

- SOH;
- RUL; or
- pre-failure monitoring.

The matrix does not show a broad body of work using explainability to compare RUL and safety-oriented predictions side by side in one framework.

## 6. How Safety Is Treated in Prior Work

### Well-Supported Trends

Safety is treated in prior work mainly through:

- fault detection
- anomaly detection
- early warning
- pre-failure inspection
- thermal-risk motivation

In the safety-focused studies, the main operational goals are:

- earlier detection of abnormal voltage or temperature behavior;
- reduction of false alarms;
- warning of overvoltage, undervoltage, or abnormal temperature conditions;
- support for inspection or intervention before failure escalation.

In the prognostics and RUL papers, safety is usually treated indirectly. Typical forms of indirect treatment include statements that:

- battery degradation affects safe operation;
- better health estimation supports reliability and safety;
- prognostics can help avoid severe failures.

### Emerging but Limited Evidence

The matrix contains limited evidence of papers that define `safety risk` as a standalone predictive target comparable to RUL. Instead, safety is usually represented by:

- fault states;
- anomaly patterns;
- temperature abnormalities;
- pre-failure zones; or
- early-warning conditions.

This means that safety is commonly operationalized as abnormality or fault detection rather than as an explicitly modeled safety-risk variable.

## 7. Recurrent Methodological Limitations

### Well-Supported Trends

Several methodological limitations recur across the matrix:

- many studies are single-task rather than comparative across outcomes;
- explainability is often absent or secondary;
- direct safety labels are uncommon;
- real-world deployment and generalization remain constrained;
- many studies are not designed to compare long-horizon prediction with safety-oriented detection in one framework.

The RUL papers often deliver strong predictive architectures but do not provide:

- formal explainability; or
- direct safety-oriented interpretation.

The safety papers often deliver early-warning or anomaly-detection capability, but they usually do not extend to:

- remaining-life estimation; or
- comparative interpretation against a prognostic target.

The reviews repeatedly emphasize PHM pipelines, data engineering, uncertainty, and deployment constraints, which suggests that the field recognizes the importance of methodological rigor, but the empirical studies in the matrix do not yet consistently integrate these dimensions.

### Emerging but Limited Evidence

Interpretability-enhanced safety detection exists, especially in the mining-truck and heavy-duty EV studies, but this is still limited to a small number of domain-specific papers. Similarly, multi-task integration is discussed conceptually and reviewed systematically, but the matrix contains limited empirical examples in battery applications that integrate multiple outputs in a well-explained way.

## 8. Recurrent Data Limitations

### Well-Supported Trends

The matrix shows several recurrent data limitations:

- reliance on cell-level laboratory datasets in RUL and XAI studies;
- use of proprietary or inaccessible operational datasets in safety and deployment-oriented work;
- incomplete dataset reporting in some empirical papers;
- fragmentation between datasets used for prognostics and datasets used for safety analysis.

This creates a structural limitation in cross-theme synthesis. Public benchmark datasets are more visible in RUL and SOH-oriented studies, while real-world operational safety studies often rely on:

- proprietary fleet data;
- specialized commercial-vehicle settings; or
- case-specific pre-fault datasets.

### Emerging but Limited Evidence

There is some evidence of real-world data use through NDANEV, electric mining trucks, and heavy-duty electric bus monitoring. However, these examples remain limited in number and are tied to specific operational settings. The matrix does not yet show a widely adopted open dataset that supports:

- RUL prediction,
- safety-oriented labeling, and
- explainability benchmarking

within one shared battery-monitoring framework.

## 9. What Is Missing at the Intersection of RUL Prediction, Safety / Anomaly Detection, and Explainable AI

### Well-Supported Trends

The strongest missing element supported by the matrix is the absence of a clearly integrated research stream that does all three of the following together:

1. predicts battery remaining useful life;
2. models safety-relevant abnormality or fault behavior in a directly comparable framework; and
3. uses explainability to compare which inputs matter for each task.

The matrix supports this conclusion in a layered way:

- RUL studies are present, but most lack explicit safety modeling and often lack strong explainability.
- Safety and anomaly papers are present, but most focus on early warning or fault detection rather than on RUL.
- XAI papers are present, but they mostly explain SOH or RUL rather than jointly comparing RUL with safety-oriented outcomes.
- Multi-task and hybrid papers indicate integration potential, but the empirical evidence base for battery-specific explainable joint modeling remains limited.

### Emerging but Limited Evidence

There are partial movements toward this intersection:

- hybrid joint diagnosis and prognostics with real-world EV data;
- interpretable operational degradation monitoring;
- interpretable fault detection in heavy-duty EV applications;
- multi-task review work that explicitly argues for cross-task integration.

However, these examples do not yet amount to a strong body of literature showing a mature, explainable, battery-specific framework that jointly analyzes RUL and safety-relevant prediction as separate but related outcomes.

## 10. The Strongest Novelty Position for This Study

### Well-Supported Trends

Based on the matrix, the strongest novelty position is not simply "using AI for batteries," because that is already well represented. It is also not merely "using XAI for battery prediction," because that too is already emerging in several papers.

The strongest supported novelty is the integration of three elements that the matrix shows are usually studied separately:

- `RUL prediction`
- `safety-oriented prediction or anomaly/fault relevance`
- `explainable comparison of predictor contributions`

This novelty is strongest when framed carefully as a methodological integration contribution rather than as a claim that no related work exists at all.

### Emerging but Limited Evidence

The matrix also suggests a secondary novelty direction:

- positioning the study around a shared battery-monitoring input space, while preserving separate outcome definitions for RUL and safety-related prediction;
- then using explainability to identify shared versus task-specific predictors.

This would align with the multi-task and hybrid literature without depending on a claim that full multi-task learning is already established as best practice.

## Proposed Research Positioning for This Study

This study can be positioned most strongly as an explainable battery-monitoring framework that bridges three research streams that are active but only partially integrated in the current matrix: long-horizon RUL prediction, safety-oriented anomaly or fault analysis, and interpretable machine learning.

The literature in the matrix supports the following positioning:

1. Prior work provides substantial evidence for data-driven RUL prediction, but most of it does not directly model safety-oriented outcomes in the same analytic framework.
2. Prior work also provides substantial evidence for battery fault detection and anomaly warning, but these studies typically prioritize early abnormality identification rather than remaining-life estimation.
3. Explainability methods, especially SHAP, are increasingly used in battery-health studies, but mainly to explain SOH or RUL models rather than to compare RUL-related and safety-related predictor structures side by side.
4. Reviews and hybrid studies indicate growing interest in integrated PHM and multi-task strategies, yet the matrix still shows limited empirical evidence for a battery-specific framework that jointly studies RUL, safety-oriented prediction, and explainability as coequal design goals.

Accordingly, the clearest novelty position for this study is:

To develop and evaluate an explainable machine-learning framework for electric vehicle battery monitoring in which RUL prediction and safety-oriented prediction are treated as distinct but related tasks derived from shared monitoring data, and in which explainability is used not only to interpret individual models but also to compare shared and task-specific predictors across the two outcomes.

This position is stronger than a generic accuracy claim because it is directly supported by the main gap visible in the matrix: the lack of integrated, interpretable comparison between degradation-oriented prediction and safety-oriented prediction within one battery analytics framework.
