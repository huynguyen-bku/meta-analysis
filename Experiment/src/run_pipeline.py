#!/usr/bin/env python3
"""
Run the full Experiment meta-analysis pipeline.

Usage:
    python run_pipeline.py           # run everything
    python run_pipeline.py --analysis  # only analysis (01-06)
    python run_pipeline.py --figures   # only figures (10-14)
"""

import sys
import time
import importlib
import argparse
from pathlib import Path

# Ensure src/ is importable
sys.path.insert(0, str(Path(__file__).parent))

ANALYSIS_MODULES = [
    "01_data_preparation",
    "02_main_meta_analysis",
    "03_publication_bias",
    "04_moderator_analysis",
    "05_sensitivity",
    "06_industry_deep_dive",
    "07_meta_regression",
]

FIGURE_MODULES = [
    "10_figure1_overview",
    "11_figure2_bias",
    "12_figure3_moderators",
    "13_figure4_industry",
    "14_supplementary",
    "15_figure5_metaregression",
]


def run_module(name):
    """Import and run a module's main() function."""
    print(f"\n{'#' * 70}")
    print(f"# Running: {name}")
    print(f"{'#' * 70}")
    t0 = time.time()
    mod = importlib.import_module(name)
    mod.main()
    elapsed = time.time() - t0
    print(f"  [{name}] Done in {elapsed:.1f}s")


def main():
    parser = argparse.ArgumentParser(description="Experiment meta-analysis pipeline")
    parser.add_argument("--analysis", action="store_true", help="Run only analysis scripts (01-06)")
    parser.add_argument("--figures", action="store_true", help="Run only figure scripts (10-14)")
    args = parser.parse_args()

    run_analysis = not args.figures or args.analysis
    run_figures = not args.analysis or args.figures

    # If neither flag given, run both
    if not args.analysis and not args.figures:
        run_analysis = True
        run_figures = True

    print("=" * 70)
    print("  EXPERIMENT META-ANALYSIS PIPELINE")
    print("=" * 70)

    t_start = time.time()

    if run_analysis:
        print("\n>>> PHASE 1: Analysis scripts")
        for mod_name in ANALYSIS_MODULES:
            run_module(mod_name)

    if run_figures:
        print("\n>>> PHASE 2: Publication figures")
        for mod_name in FIGURE_MODULES:
            run_module(mod_name)

    total = time.time() - t_start
    print("\n" + "=" * 70)
    print(f"  PIPELINE COMPLETE  ({total:.1f}s total)")
    print("=" * 70)
    print("\n  Outputs:")
    print("    outputs/tables/   — CSV result tables")
    print("    outputs/figures/  — PNG + PDF figures (600 DPI)")
    print("    outputs/reports/  — Markdown insight reports")
    print()


if __name__ == "__main__":
    main()
