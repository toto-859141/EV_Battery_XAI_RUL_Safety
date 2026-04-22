# Repository Revision Audit

## Purpose

This audit reviews repository-wide consistency across the following elements:

- title
- problem statement
- research gap
- objectives
- hypotheses
- variables
- data design
- feature plan
- modeling strategy
- explainability strategy
- evaluation framework

The audit focuses on internal alignment rather than empirical correctness, because the final dataset and final experiments have not yet been fixed.

## Overall Assessment

The repository is broadly consistent in its central research framing. Across the proposal, methodology, experiments, and manuscript drafts, the project repeatedly maintains the important conceptual distinction among battery health, remaining useful life (RUL), and safety risk. The most stable project-wide logic is as follows:

1. monitored battery variables are transformed into engineered predictors;
2. `target_rul` and `target_safety_risk` are modeled as separate outcomes;
3. explainability is used to compare task-specific and shared predictors; and
4. evaluation is expected to balance predictive performance, interpretability, and safety relevance.

The main issues are therefore not major contradictions. They are:

- title inconsistency between the repository root and the formal study title;
- repeated framing language across several documents;
- some hypotheses and evaluation claims that are directionally aligned but still somewhat under-specified;
- a few methodological links that are implied across files rather than explicitly connected in one place.

## 1. Inconsistencies

### 1.1 Title Inconsistency Between Root-Level and Formal Documents

Severity: Moderate

Files affected:

- `README.md`
- `src/__init__.py`
- most documents under `docs/`

Observation:

The formal study title used across the documentation is:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

However, the repository root uses the shortened project label:

- `README.md`: `EV Battery XAI RUL Safety`
- `src/__init__.py`: `Top-level package for the EV Battery XAI RUL Safety project.`

Why this matters:

This is not a conceptual contradiction, but it creates presentation drift between the academic title and the repository identity. For manuscript preparation, proposal defense, and GitHub presentation, it is better to define one official title and one explicit short project label.

Recommended action:

- Keep the full title as the official research title in all thesis and manuscript files.
- Update `README.md` to state the full title directly under the short repository name.
- Update `src/__init__.py` docstring to mention that `EV Battery XAI RUL Safety` is the repository shorthand for the formal study title.

### 1.2 Safety Metric Emphasis Is Slightly Inconsistent

Severity: Low

Files affected:

- `docs/proposal/objectives_and_questions.md`
- `docs/experiments/metrics_for_safety_risk.md`
- `docs/experiments/result_table_safety.md`
- `docs/manuscript/methodology_draft.md`

Observation:

The repository generally emphasizes safety-aware metrics such as recall, F1-score, AUPRC, and false-negative visibility. However, `docs/proposal/objectives_and_questions.md` still lists `AUROC` alongside F1-score and precision-recall measures without the caution that later documents provide. By contrast, the experiments package correctly notes that AUPRC is generally more informative when the high-risk class is rare.

Why this matters:

The issue is not that AUROC is wrong, but that the proposal-level language is less aligned with the safety-oriented evaluation rationale adopted elsewhere.

Recommended action:

- Revise the measurable output under Objective 3 so that recall, F1-score, and AUPRC are clearly prioritized for imbalanced safety-risk prediction.
- Keep AUROC as a secondary metric rather than a co-equal headline metric.

### 1.3 Multi-Task Learning Is Framed Consistently, but Not Always Differentiated From Joint Comparison

Severity: Low

Files affected:

- `docs/experiments/model_plan.md`
- `docs/experiments/multitask_learning_strategy.md`
- `docs/manuscript/methodology_draft.md`

Observation:

The repository correctly treats separate-task modeling as the default and multi-task learning as optional. However, the distinction between:

- joint-task comparison without shared parameters; and
- true multi-task learning with shared representation

is clearer in `docs/experiments/multitask_learning_strategy.md` than in some higher-level summaries.

Why this matters:

Without careful wording, later manuscript sections could collapse these into one idea and weaken methodological precision.

Recommended action:

- Add one explicit sentence in `docs/manuscript/methodology_draft.md` clarifying that matched-pipeline joint comparison is not the same as shared-representation multi-task learning.

## 2. Duplicated Ideas

### 2.1 Repeated Conceptual Distinction Among Battery Health, RUL, and Safety Risk

Severity: Low but widespread

Files affected:

- `docs/proposal/problem_statement.md`
- `docs/proposal/research_gap.md`
- `docs/proposal/variables_and_definitions.md`
- `docs/proposal/conceptual_framework.md`
- `docs/manuscript/introduction_draft.md`
- `docs/manuscript/methodology_draft.md`
- `docs/manuscript/contribution_statement.md`

Observation:

The distinction among battery health, RUL, and safety risk is one of the strongest parts of the repository. However, the same explanation is repeated in near-parallel language across many files.

Why this matters:

This repetition is helpful during scaffold building, but it may later make the manuscript package feel repetitive rather than cumulative.

Recommended action:

- Keep the full conceptual distinction in:
  - `docs/proposal/variables_and_definitions.md`
  - `docs/manuscript/introduction_draft.md`
- Shorten the rest to cross-references or briefer reminders.

### 2.2 Repeated Claim That Explainability Is Not a Post Hoc Visualization Step

Severity: Low

Files affected:

- `docs/proposal/problem_statement.md`
- `docs/proposal/research_gap.md`
- `docs/methodology/explainability_strategy.md`
- `docs/manuscript/introduction_draft.md`
- `docs/manuscript/methodology_draft.md`
- `docs/manuscript/contribution_statement.md`

Observation:

The repository frequently states that explainability is a core analytic requirement rather than an optional post hoc step.

Why this matters:

The message is correct and important, but repeated almost verbatim it starts to read like a slogan rather than a progressively developed argument.

Recommended action:

- Keep the strongest justification in the introduction and explainability strategy.
- In other files, reduce to shorter wording such as "explainability is integrated into model comparison and interpretation."

### 2.3 Repeated Description of the Same Staged Workflow

Severity: Low

Files affected:

- `docs/proposal/conceptual_framework.md`
- `docs/methodology/feature_extraction_workflow.md`
- `docs/experiments/model_plan.md`
- `docs/manuscript/methodology_draft.md`

Observation:

Several documents restate a similar pipeline:

- monitored variables
- preprocessing and features
- modeling
- explainability
- evaluation

Why this matters:

This is not harmful, but the repository would benefit from one canonical end-to-end workflow document and shorter references elsewhere.

Recommended action:

- Treat `docs/manuscript/methodology_draft.md` or a dedicated workflow overview as the canonical synthesis.
- In supporting documents, refer back to that workflow instead of restating it fully.

## 3. Weak Points

### 3.1 Hypotheses Are Aligned, but Statistical Testability Is Still Broad

Severity: Moderate

Files affected:

- `docs/proposal/hypotheses.md`
- `docs/proposal/objectives_and_questions.md`
- `docs/experiments/evaluation_framework.md`

Observation:

The hypotheses are substantially improved compared with generic proposal hypotheses, but they are still mostly framed as directional improvement statements. For example, "more accurately than a baseline model" is testable in principle, but the audit criteria for "improvement" are not yet specified.

Why this matters:

Without a stated comparison rule, later thesis chapters may struggle to show exactly how each hypothesis is accepted, rejected, or only partially supported.

Recommended action:

- Add a short "Hypothesis testing note" to `docs/proposal/hypotheses.md` specifying that support will be judged using predefined primary metrics and fixed split protocols, with optional confidence intervals or repeated-split summaries where feasible.

### 3.2 Safety Risk Remains Methodologically Coherent but Empirically Fragile

Severity: Moderate

Files affected:

- `docs/proposal/research_gap.md`
- `docs/methodology/target_label_definition.md`
- `docs/methodology/safety_risk_labeling_strategy.md`
- `docs/manuscript/introduction_draft.md`
- `docs/manuscript/methodology_draft.md`

Observation:

The repository is careful to note that `target_safety_risk` may be direct, event-based, or proxy-based. That caution is good. However, because the entire safety branch of the project may rely on proxy labels, the eventual empirical strength of safety findings could vary substantially depending on dataset choice.

Why this matters:

This is the most important substantive weak point in the current framing. The study is conceptually sound, but its strength will depend heavily on whether the safety target is observed directly or inferred indirectly.

Recommended action:

- Add one explicit limitation sentence to the manuscript introduction and methodology stating that the evidential strength of safety-risk findings depends on label provenance.
- In the final thesis, separate conclusions about "predicted proxy-based safety concern" from conclusions about real-world hazard.

### 3.3 The Repository Is Strong on Feature Groups but Weaker on Feature-to-Hypothesis Mapping

Severity: Moderate

Files affected:

- `docs/proposal/hypotheses.md`
- `docs/proposal/variables_and_definitions.md`
- `docs/methodology/feature_plan.md`
- `docs/methodology/feature_grouping_table.md`

Observation:

The feature engineering package is detailed and internally consistent. However, the hypotheses refer broadly to engineered features, while the feature plan separates electrical, thermal, degradation, and operational groups without explicitly mapping those groups to each hypothesis.

Why this matters:

The study would be stronger if the feature groups were linked more directly to the empirical claims being tested.

Recommended action:

- Add a compact crosswalk table linking:
  - H1-H5
  - feature groups
  - expected task relevance
  - evaluation evidence

Suggested location:

- `docs/proposal/hypotheses.md` or a new appendix-style methodology note.

### 3.4 The Evaluation Framework States Priorities Clearly but Does Not Yet Define a Final Model Selection Rule

Severity: Moderate

Files affected:

- `docs/experiments/evaluation_framework.md`
- `docs/experiments/model_plan.md`
- `docs/manuscript/methodology_draft.md`

Observation:

The repository repeatedly states that the best model should balance predictive performance, interpretability, robustness, and safety relevance. This is appropriate. However, no document yet defines how those criteria will be integrated into a final model recommendation.

Why this matters:

Without a stated decision rule, final model selection may appear subjective even if the evaluation is thorough.

Recommended action:

- Add a short model selection protocol that specifies:
  - primary task metric
  - minimum acceptable robustness behavior
  - explanation stability requirement
  - safety-error acceptability criteria

Suggested location:

- `docs/experiments/evaluation_framework.md`
- mirrored briefly in `docs/manuscript/methodology_draft.md`

## 4. Missing Methodological Links

### 4.1 Missing Explicit Link Between Hypotheses and Evaluation Metrics

Severity: High

Files affected:

- `docs/proposal/hypotheses.md`
- `docs/experiments/metrics_for_rul.md`
- `docs/experiments/metrics_for_safety_risk.md`
- `docs/experiments/evaluation_framework.md`

Observation:

The hypotheses assert expected improvements and task-specific predictor differences, but there is no single document stating exactly which metrics or evidence patterns correspond to support for each hypothesis.

Why this matters:

This is the clearest repository-wide missing link. The project has good components, but the chain from hypothesis to evidence is still distributed across separate files.

Concrete revision action:

- Add a "Hypothesis-to-evidence map" table with columns such as:
  - Hypothesis
  - Evidence source
  - Primary metric or analysis
  - Comparison basis
  - Interpretation rule

### 4.2 Missing Explicit Link Between Safety Labeling Strategy and Evaluation Thresholds

Severity: High

Files affected:

- `docs/methodology/safety_risk_labeling_strategy.md`
- `docs/methodology/safety_warning_logic.md`
- `docs/experiments/metrics_for_safety_risk.md`
- `docs/experiments/result_table_safety.md`

Observation:

The repository separately defines:

- safety label logic,
- warning interpretation,
- safety metrics,
- safety reporting tables.

However, it does not yet explicitly connect label definitions to evaluation thresholds and reporting conventions. For example, if safety risk is ordinal rather than binary, the appropriate metrics, thresholding logic, and warning table interpretation need to be stated together.

Why this matters:

This gap could create confusion later if the chosen dataset supports only ordinal labels or only proxy scores.

Concrete revision action:

- Add a short section called "Metric selection by safety-label form" to `docs/experiments/metrics_for_safety_risk.md`.
- Cross-reference it from `docs/methodology/safety_risk_labeling_strategy.md`.

### 4.3 Missing Explicit Link Between Feature Provenance and Explainability Validity

Severity: Moderate

Files affected:

- `docs/methodology/feature_extraction_workflow.md`
- `docs/methodology/explainability_strategy.md`
- `docs/methodology/explanation_risks_and_limitations.md`
- `docs/manuscript/methodology_draft.md`

Observation:

The repository states that feature provenance should be documented and that explanations should be interpreted cautiously. However, it does not yet state clearly that explanation validity depends partly on feature provenance, feature aggregation choices, and feature correlation structure.

Why this matters:

Because the study emphasizes explainability, this linkage should be explicit rather than assumed.

Concrete revision action:

- Add a paragraph in `docs/methodology/explainability_strategy.md` explaining that explanation results must be interpreted in light of feature construction, aggregation level, and correlation among engineered features.

### 4.4 Missing Explicit Link Between Data Split Strategy and Cross-Task Comparability

Severity: Moderate

Files affected:

- `docs/methodology/train_validation_test_strategy.md`
- `docs/experiments/multitask_learning_strategy.md`
- `docs/manuscript/methodology_draft.md`

Observation:

The split strategy is strong on leakage prevention and temporal validity. The multi-task document also says comparisons should use the same split. However, the repository does not yet explicitly define whether RUL and safety models will always be compared on:

- the same window population;
- different task-eligible subsets; or
- a common core subset plus task-specific extensions.

Why this matters:

This affects fairness of cross-task comparison and interpretation of shared predictors.

Concrete revision action:

- Add a subsection called "Cross-task comparability set" to either the split strategy or methodology draft, explaining how shared-versus-task-specific data subsets will be handled.

### 4.5 Missing Explicit Link Between Objectives and Expected Contributions

Severity: Low

Files affected:

- `docs/proposal/objectives_and_questions.md`
- `docs/manuscript/contribution_statement.md`
- `docs/manuscript/introduction_draft.md`

Observation:

The expected contributions are well written, but they are not yet explicitly traceable to the numbered objectives.

Why this matters:

A clear objective-to-contribution link would improve proposal defense readiness and help the final discussion chapter show how contributions were actually achieved.

Concrete revision action:

- Add a short objective-to-contribution mapping note in `docs/manuscript/contribution_statement.md` or the proposal chapter summary.

## 5. Concrete Revision Actions

The following actions are recommended in priority order.

### High Priority

1. Create a hypothesis-to-evidence map linking each hypothesis to:
   - metrics
   - comparison logic
   - expected evidence source
2. Add a safety-label-form-to-metric crosswalk so binary, ordinal, and score-based safety targets map to appropriate evaluation and reporting methods.
3. State explicitly how cross-task comparisons will handle shared versus task-specific subsets of observation windows.

### Medium Priority

4. Add a formal model selection protocol describing how predictive performance, robustness, explainability, and safety-error consequences will be combined in final model choice.
5. Add a clearer feature-group-to-hypothesis crosswalk so the feature plan supports direct empirical testing.
6. Add one explicit caution in the introduction and methodology that the strength of safety conclusions depends on label provenance, especially when proxy labels are used.
7. Clarify in the methodology draft that matched-pipeline joint comparison is distinct from shared-representation multi-task learning.
8. Add an explicit note in the explainability strategy linking explanation validity to feature provenance, aggregation choices, and correlated predictors.

### Low Priority

9. Standardize title presentation by keeping one official academic title and one clearly labeled repository shorthand.
10. Reduce repeated conceptual wording across proposal and manuscript files by keeping the full conceptual distinction in only a few anchor documents and shortening the rest.
11. Make the contribution statement more directly traceable to the numbered objectives.

## Suggested Next Revision Sequence

The most efficient revision order is:

1. revise `docs/proposal/hypotheses.md`
2. revise `docs/experiments/metrics_for_safety_risk.md`
3. revise `docs/methodology/train_validation_test_strategy.md`
4. revise `docs/experiments/evaluation_framework.md`
5. revise `docs/manuscript/methodology_draft.md`
6. standardize `README.md` and minor title references

This sequence is recommended because it strengthens the logic chain from research claims to empirical evidence before polishing presentation-level consistency.

## Closing Note

The repository is already strong in conceptual clarity and methodological scaffolding. The next revision phase should focus less on generating additional content and more on tightening traceability across existing content: hypothesis to evidence, label form to metric choice, split strategy to cross-task comparison, and model comparison to final selection logic.
