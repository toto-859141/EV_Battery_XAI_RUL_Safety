"""Starter markdown report generation for explainability outputs.

This module converts explanation summaries into simple markdown reports that
can later be expanded into richer experiment reports. The goal is to provide
an auditable, text-based bridge between explanation artifacts and research
interpretation.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(frozen=True)
class ExplanationReportInputs:
    """Inputs needed to assemble a lightweight markdown explanation report."""

    experiment_id: str
    task_name: str
    model_name: str
    global_summary: pd.DataFrame | None = None
    local_summary: pd.DataFrame | None = None
    notes: tuple[str, ...] = ()


def _table_preview(table: pd.DataFrame, n_rows: int = 10) -> str:
    """Render a short markdown preview of a DataFrame."""
    if table.empty:
        return "_No rows available._"
    return table.head(n_rows).to_markdown(index=False)


def build_markdown_report(inputs: ExplanationReportInputs) -> str:
    """Build a starter markdown report for explanation outputs.

    Placeholder:
    This report is intentionally lightweight. Extend it later with:
    - figure links;
    - task-specific interpretation text;
    - safety-oriented explanation commentary.
    """
    lines: list[str] = [
        f"# Explanation Report: {inputs.experiment_id}",
        "",
        "## Overview",
        "",
        f"- Task: `{inputs.task_name}`",
        f"- Model: `{inputs.model_name}`",
    ]

    if inputs.notes:
        lines.extend(["", "## Notes", ""])
        lines.extend([f"- {note}" for note in inputs.notes])

    if inputs.global_summary is not None:
        lines.extend(
            [
                "",
                "## Global Explanation Summary",
                "",
                _table_preview(inputs.global_summary),
                "",
                "_Placeholder: add global SHAP or feature-importance plots here._",
            ]
        )

    if inputs.local_summary is not None:
        lines.extend(
            [
                "",
                "## Local Explanation Summary",
                "",
                _table_preview(inputs.local_summary),
                "",
                "_Placeholder: add local force, waterfall, or attribution plots here._",
            ]
        )

    lines.extend(
        [
            "",
            "## Interpretation Placeholder",
            "",
            "Add task-specific interpretation here, with cautious language "
            "appropriate for safety-critical battery monitoring.",
        ]
    )
    return "\n".join(lines) + "\n"


def save_markdown_report(report_text: str, output_path: Path) -> Path:
    """Save a markdown explanation report."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report_text, encoding="utf-8")
    return output_path
