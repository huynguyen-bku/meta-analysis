"""
01 — Data preparation: load Excel, compute effect sizes, flag edge cases.

Output: outputs/tables/01_effect_sizes_full.csv
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pandas as pd
import numpy as np

from experiment_meta.config import DATA_PATH, TABLE_DIR, REPORT_DIR
from experiment_meta.effect_sizes import compute_all_effect_sizes, flag_edge_cases
from jabes_shared.insights import InsightLogger


def main():
    print("=" * 70)
    print("01 — DATA PREPARATION")
    print("=" * 70)

    # ── Load ──
    print(f"\n[1] Loading {DATA_PATH.name} ...")
    df = pd.read_excel(DATA_PATH)
    print(f"    Rows: {len(df)}")
    print(f"    Papers: {df['Paper_ID'].nunique()}")
    print(f"    Experiments: {df['Exp_ID_Cleaned'].nunique()}")
    print(f"    Year range: {df['Year'].min()}–{df['Year'].max()}")

    # ── Ensure ES_ID exists ──
    if "ES_ID" not in df.columns:
        df["ES_ID"] = range(1, len(df) + 1)

    # ── Compute effect sizes ──
    print("\n[2] Computing effect sizes ...")
    df = compute_all_effect_sizes(df)

    for suffix, label in [("s", "Strong Synergy"), ("h", "Human Augmentation"),
                           ("a", "AI Augmentation")]:
        col = f"es_{suffix}"
        valid = df[col].notna().sum()
        mean_val = df[col].mean()
        print(f"    {label}: valid={valid}, mean={mean_val:.3f}")

    # ── Flag edge cases ──
    print("\n[3] Flagging edge cases ...")
    df = flag_edge_cases(df)
    n_flagged = (df["flag_sd_zero"] | df["flag_extreme_es"] | df["flag_wide_ci"]).sum()
    print(f"    Flagged: {n_flagged}/{len(df)}")

    # ── Save ──
    out_path = TABLE_DIR / "01_effect_sizes_full.csv"
    df.to_csv(out_path, index=False)
    print(f"\n[4] Saved: {out_path.name}")

    # Save flagged subset
    flagged = df[df["flag_sd_zero"] | df["flag_extreme_es"] | df["flag_wide_ci"]]
    if len(flagged) > 0:
        flag_path = TABLE_DIR / "01_flagged_effect_sizes.csv"
        flagged.to_csv(flag_path, index=False)
        print(f"    Saved: {flag_path.name} ({len(flagged)} rows)")

    # ── Insight report ──
    log = InsightLogger(REPORT_DIR, "01_data_preparation")
    log.add_section("Dataset Overview", [
        f"Total effect sizes: {len(df)}",
        f"Unique papers: {df['Paper_ID'].nunique()}",
        f"Unique experiments: {df['Exp_ID_Cleaned'].nunique()}",
        f"Year range: {df['Year'].min()}–{df['Year'].max()}",
    ])
    es_bullets = []
    for suffix, label in [("s", "Strong Synergy"), ("h", "Human Augmentation"),
                           ("a", "AI Augmentation")]:
        col = f"es_{suffix}"
        valid = df[col].notna().sum()
        mean_val = df[col].mean()
        median_val = df[col].median()
        es_bullets.append(f"{label}: k={valid}, mean g={mean_val:.3f}, median g={median_val:.3f}")
    log.add_section("Effect Size Summary", es_bullets)
    log.add_section("Edge Cases", [
        f"Flagged observations: {n_flagged}/{len(df)}",
        f"SD=0 flags: {df['flag_sd_zero'].sum()}",
        f"Extreme ES (|g|>3): {df['flag_extreme_es'].sum()}",
        f"Wide CI flags: {df['flag_wide_ci'].sum()}",
    ])
    log.write("01 — Data Preparation Insights")

    print("\n" + "=" * 70)
    print("01 — DATA PREPARATION COMPLETE")
    print("=" * 70)
    return df


if __name__ == "__main__":
    main()
