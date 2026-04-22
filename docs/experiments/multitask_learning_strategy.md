# Multi-Task Learning Strategy

## Purpose

This document discusses whether the project should model the battery prediction problem as:

- separate tasks;
- joint tasks without shared parameters; or
- multi-task learning with shared representation.

The analysis is framed for the two project outcomes:

- `target_rul`
- `target_safety_risk`

## Conceptual Premise

The two targets are related because both are derived from battery monitoring signals and are influenced by degradation and operating stress. However, they are not equivalent:

- `target_rul` is a long-horizon prognostic outcome;
- `target_safety_risk` is a safety-oriented outcome that may reflect shorter-horizon abnormality or event proximity.

Therefore, the choice of modeling strategy should be empirical and conceptually cautious.

## Option 1: Separate-Task Modeling

### Description

Train one model for `target_rul` and a different model for `target_safety_risk`.

### Advantages

- conceptually clean separation between the two tasks;
- simpler training and interpretation;
- lower risk that one task degrades the other;
- easier to tailor features and metrics to each task.

### Limitations

- may fail to exploit shared information in the input space;
- duplicates training effort across tasks.

### Recommended Use

This is the recommended starting strategy and the default benchmark for the project.

## Option 2: Joint Task Comparison Without Shared Parameters

### Description

Use the same input representation and experimental pipeline for both tasks, but train separate models.

### Purpose

- provide a fair comparison of how the same features behave across tasks;
- compare explanation patterns without enforcing shared learning.

### Advantages

- strong methodological clarity;
- supports direct cross-task interpretation.

### Limitations

- still does not exploit shared representation learning.

## Option 3: Multi-Task Learning

### Description

Train a single model with a shared backbone and task-specific output heads for:

- RUL regression;
- safety risk classification.

### Possible Architecture

- shared encoder for battery observation windows;
- regression head for `target_rul`;
- classification head for `target_safety_risk`.

### Advantages

- may improve representation learning if the tasks truly share informative structure;
- may reduce overfitting in limited-data settings;
- may reveal shared predictors more clearly.

### Limitations

- tasks may compete rather than assist each other;
- loss balancing becomes non-trivial;
- interpretation becomes more complex;
- performance gains are not guaranteed.

## Recommended Strategy

The recommended modeling sequence is:

1. establish separate-task baselines;
2. compare separate-task and matched-pipeline single-task models;
3. introduce multi-task learning only after single-task models are stable.

This sequence is recommended because it prevents the study from attributing gains to multi-task learning without a strong single-task reference.

## Conditions Under Which Multi-Task Learning Is Worth Testing

Multi-task learning is most appropriate when:

- the same observation windows support both labels;
- both labels are available for a substantial subset of the data;
- there is reason to expect shared information in electrical, thermal, and degradation features;
- the dataset is large enough to support a higher-capacity model.

## Conditions Under Which Separate Modeling May Be Preferable

Separate-task models may remain preferable when:

- labels are available for different subsets of the data;
- safety labels are weak or proxy-based;
- the tasks operate at different time horizons;
- interpretability is prioritized over architectural sophistication.

## Multi-Task Design Recommendations

If multi-task learning is attempted, the following design choices should be documented:

### Shared Inputs

- raw sequence channels used;
- engineered feature channels used;
- observation-window definition.

### Task Heads

- regression head for `target_rul`;
- classification head for `target_safety_risk`.

### Loss Design

- weighted sum of regression and classification loss;
- documented justification for task-loss weights.

### Evaluation

- compare against separate-task models using the same train, validation, and test split;
- evaluate whether one task benefits at the expense of the other.

## Performance-Explainability Trade-Off

Separate-task models are generally easier to explain because each model is optimized for a single outcome. Multi-task models may provide better shared representations, but they also make explanation more difficult because:

- variable importance may differ by task head;
- shared features may have different meanings across outputs;
- task interactions may be harder to interpret.

In a project that emphasizes explainability, multi-task learning should therefore be treated as a useful research question rather than a default preferred solution.

## Recommended Conclusion

The most defensible approach for this project is to treat separate-task modeling as the primary reference framework and multi-task learning as an optional advanced experiment. If multi-task learning improves predictive performance without materially reducing interpretability, it may be justified. If not, separate-task models should remain the preferred final formulation.
