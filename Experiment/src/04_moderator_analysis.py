"""
04 — Moderator analysis: subgroup meta + Q-between for 6 moderators.

Output: outputs/tables/04_subgroup_results.csv
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pandas as pd

from experiment_meta.config import TABLE_DIR, REPORT_DIR, ES_COLS, COMPARISON_NAMES, MODERATORS
from experiment_meta.moderators import run_all_moderators
from experiment_meta.visuals import sig_stars
from jabes_shared.insights import InsightLogger


def main():
    print("=" * 70)
    print("04 — MODERATOR ANALYSIS")
    print("=" * 70)

    data_path = TABLE_DIR / "01_effect_sizes_full.csv"
    df = pd.read_csv(data_path)
    print(f"\nLoaded: {len(df)} effect sizes")
    print(f"Moderators: {MODERATORS}")

    all_results = []

    for key, (es_col, var_col) in ES_COLS.items():
        name = COMPARISON_NAMES[key]
        print(f"\n{'─' * 60}")
        print(f"  {name}")
        print(f"{'─' * 60}")

        result_df = run_all_moderators(df, MODERATORS, es_col, var_col, name)

        if len(result_df) > 0:
            all_results.append(result_df)

            # Print summary
            for mod in result_df["moderator"].unique():
                mod_data = result_df[result_df["moderator"] == mod]
                q_p = mod_data.iloc[0].get("Q_between_pval", 1.0)
                sig = sig_stars(q_p) if pd.notna(q_p) else ""
                print(f"\n  {mod} (Q-between {sig}):")
                for _, row in mod_data.iterrows():
                    s = sig_stars(row["p_value"])
                    print(f"    {row['level']}: g={row['estimate']:.3f} "
                          f"[{row['ci_lower']:.3f}, {row['ci_upper']:.3f}], "
                          f"k={row['k']}, I²={row['I2']:.1f}% {s}")

    # ── Combine and save ──
    if all_results:
        combined = pd.concat(all_results, ignore_index=True)
        out_path = TABLE_DIR / "04_subgroup_results.csv"
        combined.to_csv(out_path, index=False)
        print(f"\nSaved: {out_path.name} ({len(combined)} rows)")

        # ── Insight report ──
        log = InsightLogger(REPORT_DIR, "04_moderator_analysis")
        for mod in combined["moderator"].unique():
            mod_data = combined[combined["moderator"] == mod]
            bullets = []
            # Q-between significance
            q_p = mod_data.iloc[0].get("Q_between_pval", None)
            if q_p is not None and pd.notna(q_p):
                sig = sig_stars(q_p)
                bullets.append(f"Q-between p = {q_p:.4f} ({sig})")
            # Subgroup estimates
            for comp in mod_data["comparison"].unique():
                comp_data = mod_data[mod_data["comparison"] == comp]
                for _, row in comp_data.iterrows():
                    s = sig_stars(row["p_value"])
                    bullets.append(
                        f"{comp} / {row['level']}: g = {row['estimate']:+.3f} "
                        f"[{row['ci_lower']:.3f}, {row['ci_upper']:.3f}] {s}, k={row['k']}"
                    )
            log.add_section(f"Moderator: {mod}", bullets)

        # Significant moderators summary
        sig_mods = []
        for mod in combined["moderator"].unique():
            q_p = combined[combined["moderator"] == mod].iloc[0].get("Q_between_pval", 1.0)
            if pd.notna(q_p) and q_p < 0.05:
                sig_mods.append(f"{mod} (Q-between p = {q_p:.4f})")
        log.add_section("Significant Moderators", sig_mods if sig_mods else ["None reached p < 0.05"])
        log.write("04 — Moderator Analysis Insights")
    else:
        print("\n  ⚠ No subgroup results generated")

    print("\n" + "=" * 70)
    print("04 — MODERATOR ANALYSIS COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
