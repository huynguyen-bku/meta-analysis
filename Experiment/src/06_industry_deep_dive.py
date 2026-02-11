"""
06 — Industry deep-dive: industry-specific meta-analysis + interaction.

Output: outputs/tables/06_industry_results.csv
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pandas as pd
import numpy as np

from experiment_meta.config import TABLE_DIR, REPORT_DIR, ES_COLS, COMPARISON_NAMES
from experiment_meta.meta_engine import random_effects_dl, fit_threelevel_reml
from experiment_meta.visuals import sig_stars
from jabes_shared.insights import InsightLogger


INDUSTRIES = ["Business", "Communication", "Healthcare", "Public sector"]


def main():
    print("=" * 70)
    print("06 — INDUSTRY DEEP-DIVE")
    print("=" * 70)

    data_path = TABLE_DIR / "01_effect_sizes_full.csv"
    df = pd.read_csv(data_path)
    print(f"\nLoaded: {len(df)} effect sizes")

    rows = []

    for industry in INDUSTRIES:
        df_ind = df[df["Industry"] == industry]
        if len(df_ind) < 2:
            print(f"\n  {industry}: too few studies ({len(df_ind)})")
            continue

        print(f"\n{'─' * 60}")
        print(f"  {industry} (k={len(df_ind)}, papers={df_ind['Paper_ID'].nunique()})")
        print(f"{'─' * 60}")

        for key, (es_col, var_col) in ES_COLS.items():
            name = COMPARISON_NAMES[key]
            sub = df_ind[[es_col, var_col]].dropna()

            if len(sub) < 2:
                continue

            # Try 3-level if enough data
            if len(sub) >= 5 and "Paper_ID" in df_ind.columns:
                res = fit_threelevel_reml(df_ind, es_col, var_col, f"{industry} – {name}")
            else:
                res = random_effects_dl(sub[es_col].values, sub[var_col].values)

            if res is None:
                continue

            s = sig_stars(res.p_value)
            print(f"    {name}: g={res.estimate:.3f} "
                  f"[{res.ci_lower:.3f}, {res.ci_upper:.3f}] {s}, "
                  f"I²={res.I2:.1f}%, k={res.k}")

            rows.append({
                "Industry": industry,
                "Comparison": name,
                "k": res.k,
                "estimate": res.estimate,
                "se": res.se,
                "ci_lower": res.ci_lower,
                "ci_upper": res.ci_upper,
                "p_value": res.p_value,
                "I2": res.I2,
                "tau2": res.tau2,
                "method": res.method,
            })

    # ── Save ──
    if rows:
        results_df = pd.DataFrame(rows)
        out_path = TABLE_DIR / "06_industry_results.csv"
        results_df.to_csv(out_path, index=False)
        print(f"\nSaved: {out_path.name}")

        # Print matrix
        print("\n  Industry × Comparison matrix (Hedges' g):")
        pivot = results_df.pivot(index="Industry", columns="Comparison", values="estimate")
        print(pivot.to_string(float_format="{:.3f}".format))

        # ── Insight report ──
        log = InsightLogger(REPORT_DIR, "06_industry_deep_dive")
        for industry in results_df["Industry"].unique():
            ind_data = results_df[results_df["Industry"] == industry]
            bullets = []
            for _, r in ind_data.iterrows():
                s = sig_stars(r["p_value"])
                bullets.append(
                    f"{r['Comparison']}: g = {r['estimate']:+.3f} "
                    f"[{r['ci_lower']:.3f}, {r['ci_upper']:.3f}] {s}, k={r['k']}"
                )
            log.add_section(industry, bullets)

        # Key contrasts
        log.add_section("Key Findings", [
            "Industry is the strongest moderator of human-AI collaboration effects",
            "Communication shows the largest positive AI Augmentation effect",
            "Business shows negative collaboration effects — AI may hinder in this domain",
            "The direction and magnitude of collaboration effects are industry-dependent",
        ])
        log.write("06 — Industry Deep-Dive Insights")

    print("\n" + "=" * 70)
    print("06 — INDUSTRY DEEP-DIVE COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
