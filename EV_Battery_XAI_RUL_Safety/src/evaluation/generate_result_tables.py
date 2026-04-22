"""Generate markdown-ready result tables from evaluation outputs.

This module converts structured DataFrames into compact markdown tables that
can be copied into experiment reports, thesis chapters, or manuscript drafts.
The goal is to standardize reporting early, even before the final dataset and
full experiment pipeline are finalized.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def dataframe_to_markdown_table(
    frame: pd.DataFrame,
    title: str,
    notes: tuple[str, ...] = (),
) -> str:
    """Render a DataFrame as a markdown section with optional notes."""
    lines = [f"## {title}", ""]
    if frame.empty:
        lines.append("_No results available._")
    else:
        lines.append(frame.to_markdown(index=False))
    if notes:
        lines.extend(["", "Notes:"])
        lines.extend([f"- {note}" for note in notes])
    return "\n".join(lines) + "\n"


def save_markdown_table(markdown_text: str, output_path: Path) -> Path:
    """Save a markdown-formatted result table."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown_text, encoding="utf-8")
    return output_path


def build_rul_result_table(frame: pd.DataFrame) -> str:
    """Create a markdown-ready RUL result table.

    Placeholder:
    Align column names with the final experiment-tracking schema once the
    project standardizes all evaluation outputs.
    """
    return dataframe_to_markdown_table(
        frame,
        title="RUL Results",
        notes=(
            "Lower MAE and RMSE indicate better RUL regression performance.",
            "Add late-life error commentary once life-stage analysis is implemented.",
        ),
    )


def build_safety_result_table(frame: pd.DataFrame) -> str:
    """Create a markdown-ready safety-risk result table."""
    return dataframe_to_markdown_table(
        frame,
        title="Safety Risk Results",
        notes=(
            "Interpret recall carefully for high-risk classes.",
            "False negatives and false positives should be discussed in the narrative report.",
        ),
    )


def build_robustness_result_table(frame: pd.DataFrame) -> str:
    """Create a markdown-ready robustness summary table."""
    return dataframe_to_markdown_table(
        frame,
        title="Robustness Results",
        notes=(
            "Compare subgroup performance against the reference condition.",
            "Add explanation-shift commentary where applicable.",
        ),
    )
