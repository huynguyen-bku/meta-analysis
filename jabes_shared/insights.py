"""Shared manuscript insight logging utilities."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Iterable


class InsightLogger:
    """Write insight bullets to markdown and plain text files.

    Usage::

        log = InsightLogger(report_dir, "02_meta_results")
        log.add_section("Overall Effects", [
            "Human Augmentation: g = +0.494, p < 0.001",
            "AI Augmentation: g = +0.145, p = 0.128 (ns)",
        ])
        log.write("Meta-Analysis Insights")
    """

    def __init__(self, report_dir: Path, stem: str):
        self.report_dir = Path(report_dir)
        self.report_dir.mkdir(parents=True, exist_ok=True)
        self.md_path = self.report_dir / f"{stem}.md"
        self.txt_path = self.report_dir / f"{stem}.txt"
        self._sections: list[tuple[str, list[str]]] = []

    def add_section(self, title: str, bullets: Iterable[str]) -> None:
        clean = [b.strip() for b in bullets if b and str(b).strip()]
        self._sections.append((title, clean))

    def write(self, header: str = "Analysis Insights") -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        md_lines = [f"# {header}", "", f"Generated: {timestamp}", ""]
        txt_lines = [header.upper(), f"Generated: {timestamp}", ""]

        for title, bullets in self._sections:
            md_lines.extend([f"## {title}", ""])
            txt_lines.extend([title, "-" * len(title)])
            for bullet in bullets:
                md_lines.append(f"- {bullet}")
                txt_lines.append(f"- {bullet}")
            md_lines.append("")
            txt_lines.append("")

        self.md_path.write_text("\n".join(md_lines), encoding="utf-8")
        self.txt_path.write_text("\n".join(txt_lines), encoding="utf-8")
        print(f"  Report: {self.md_path.name}")
