# Literature Review Workflow

## Purpose

This workflow provides a structured process for conducting the literature review for the project:

**Explainable Artificial Intelligence for Safety Risk and Remaining Useful Life Prediction of Electric Vehicle Batteries**

The workflow is designed to ensure that paper identification, screening, extraction, synthesis, and gap analysis are transparent and reproducible. Only studies with a verifiable DOI should enter the formal review matrix.

## Step 1: Define the Review Scope

Before searching, confirm the review boundaries.

### Tasks

- Use the five predefined themes in `theme_structure.md`.
- Confirm the conceptual distinction between battery health, safety risk, and remaining useful life.
- Confirm that the review is focused on scholarly literature with DOI records.

### Output

- A fixed thematic and conceptual scope for the review.

## Step 2: Build the Search Strategy

Construct database queries using the terms in `search_keywords.md`.

### Tasks

- Select databases appropriate for engineering and machine learning research.
- Combine battery-domain terms with task terms and explainability terms.
- Run both theme-specific and cross-theme queries.
- Record the exact search strings used for transparency.

### Output

- A documented set of search strings and database sources.

## Step 3: Collect and De-duplicate Records

Gather candidate papers and remove duplicate records.

### Tasks

- Export citations from each database.
- Merge records into a single working list.
- Remove duplicated items across databases.
- Record the DOI for each candidate where available.

### Output

- A de-duplicated paper list with DOI information where available.

## Step 4: Conduct Title and Abstract Screening

Screen papers against the inclusion and exclusion criteria.

### Tasks

- Review titles and abstracts for thematic relevance.
- Exclude papers without verifiable DOI information.
- Apply the labels `include`, `exclude`, or `maybe`.
- Record the primary theme for each paper.

### Output

- A screened shortlist for full-text review.

## Step 5: Conduct Full-Text Screening

Evaluate the shortlisted papers using the full article.

### Tasks

- Confirm the paper contains sufficient technical detail.
- Confirm that the topic aligns with at least one review theme.
- Verify whether the study contributes to variables, targets, models, or explainability questions relevant to the project.
- Confirm and record the DOI.

### Output

- A final set of included papers for extraction.

## Step 6: Extract Structured Evidence

Populate the literature matrix using `literature_matrix.md`.

### Tasks

- Add one row per included paper.
- Record dataset, features, model, explainability method, safety aspect, findings, limitations, and research gap.
- Add the verified DOI in the citation notes section.
- Keep entries concise and comparable across papers.

### Output

- A completed or progressively updated review matrix.

## Step 7: Synthesize by Theme

Review the extracted studies within each major theme.

### Tasks

- Group papers under the five review themes.
- Compare definitions of targets, predictors, and evaluation methods.
- Identify recurring datasets, features, model families, and explainability methods.
- Note where the literature distinguishes or confuses battery health, safety risk, and RUL.

### Output

- Thematic summaries with emerging patterns and unresolved issues.

## Step 8: Identify Cross-Theme Gaps

Move from description to critical synthesis.

### Tasks

- Compare what is known about RUL, safety risk, battery health, and XAI.
- Identify where the literature remains fragmented.
- Determine whether studies jointly address battery monitoring, safety, RUL, and explainability.
- Record the strongest unresolved methodological and practical gaps.

### Output

- A defensible statement of the research gap linked to the project aims.

## Step 9: Translate Findings into Proposal Inputs

Use the literature review to refine the proposal documents.

### Tasks

- refine the problem statement;
- refine the research gap;
- adjust objectives and hypotheses where necessary;
- clarify variable definitions and target assumptions; and
- justify the conceptual framework and methodology choices.

### Output

- A literature-grounded proposal framing package.

## Step 10: Maintain an Update Log

The review should remain traceable as new papers are added.

### Tasks

- Record search date, database, query string, and number of hits.
- Record reasons for excluding borderline papers.
- Update the matrix and theme summaries incrementally.
- Revisit keyword combinations if important themes are underrepresented.

### Output

- An auditable review process that can be reported in a proposal, thesis, or manuscript.

## Recommended Review Sequence

The review should ideally proceed in the following order:

1. RUL prediction literature
2. Battery health monitoring literature
3. Battery safety risk literature
4. Explainable AI for prognostics
5. Interpretable machine learning for safety-critical systems
6. Cross-theme synthesis

This sequence is recommended because it establishes the battery domain first, then adds interpretability and safety-critical reasoning.
