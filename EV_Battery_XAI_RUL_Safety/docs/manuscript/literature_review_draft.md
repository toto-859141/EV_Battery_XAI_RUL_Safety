# Literature Review Draft

## Literature Review

### Overview

The literature relevant to this study can be organized into five major themes: electric vehicle battery remaining useful life prediction, battery safety risk prediction, battery health monitoring, explainable artificial intelligence for prognostics, and interpretable machine learning for safety-critical systems. These themes are related, but they do not address identical research questions. A review structured in this way is necessary because the present study seeks to integrate predictive performance, interpretability, and safety relevance within a single framework.

### EV Battery Remaining Useful Life Prediction

Research on battery RUL prediction has focused on estimating the service life remaining before the battery reaches a defined end-of-life criterion. Many studies have used cycle-based degradation data and have modeled capacity fade, resistance growth, or other degradation-related indicators. Classical machine learning models, ensemble models, and deep learning approaches have all been investigated for this purpose. A recurring strength of this literature is its emphasis on quantitative prognostic accuracy. However, a recurring limitation is that RUL is often modeled independently of safety-oriented outcomes, and explainability is not always incorporated as a central part of the analysis.

### Battery Safety Risk Prediction

The battery safety literature has often emphasized fault diagnosis, thermal runaway precursors, anomaly detection, and early warning mechanisms. This body of work is essential because it identifies variables and patterns associated with abnormal electrical and thermal behavior. Nevertheless, safety-related prediction is frequently operationalized in heterogeneous ways. Some studies rely on explicit event labels, whereas others rely on proxy conditions or indirect definitions of abnormality. This makes comparison difficult and highlights the importance of clearly defining safety risk as a target variable in any new study.

### Battery Health Monitoring

Battery health monitoring research has focused on measuring or estimating the condition of the battery using indicators such as capacity retention, internal resistance, efficiency, and signal response characteristics. This literature is especially important because it provides many of the candidate variables used in prognostic modeling. At the same time, battery health should not be treated as interchangeable with either RUL or safety risk. Battery health is better understood as an inferred condition construct that may influence both outcomes while remaining conceptually distinct from them.

### Explainable Artificial Intelligence for Prognostics

Explainable AI has been introduced in prognostics and predictive maintenance to improve the transparency of machine learning models. Techniques such as SHAP, LIME, and other attribution-based approaches have been used to identify influential predictors and to interpret model behavior at both global and local levels. In battery applications, however, explainability has often been applied after model development rather than integrated into the core comparative logic of the study. The present research therefore treats explainability not as an optional visualization tool, but as part of the model evaluation process.

### Interpretable Machine Learning for Safety-Critical Systems

Research in safety-critical machine learning has emphasized that prediction alone is insufficient when outputs may influence high-stakes technical decisions. Interpretability, auditability, and explanation stability are especially important when false negatives may suppress warning signals and false positives may generate unnecessary interventions. Although not all such studies are battery-specific, this literature is directly relevant to the present work because it provides a methodological basis for treating model explanation as a safety-relevant requirement rather than a secondary convenience.

### Synthesis of the Literature

Taken together, the literature suggests that battery prognostics, safety-related prediction, and explainability have each advanced substantially, but their integration remains incomplete. The major unresolved issue is the lack of a research framework in which battery monitoring variables are used to model both RUL and safety risk as separate predictive tasks while also evaluating how explainability clarifies their shared and task-specific drivers. This gap motivates the present study and supports the need for a methodologically explicit design that connects target definition, feature engineering, predictive modeling, and explanation analysis.

### Placeholder for Expansion

This draft section is intended as a structural manuscript foundation. It should later be expanded using:

- `docs/literature_review/thematic_synthesis_template.md`
- `docs/literature_review/literature_matrix.md`
- DOI-verified papers extracted and coded through the literature review workflow.
