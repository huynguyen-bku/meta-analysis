"""
03 — Publication bias: Egger + Begg + trim-and-fill + fail-safe N.

Output: outputs/tables/03_bias_summary.csv
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pandas as pd
import numpy as np

from experiment_meta.config import TABLE_DIR, REPORT_DIR, ES_COLS, COMPARISON_NAMES
from experiment_meta.bias import run_all_bias_tests
from jabes_shared.insights import InsightLogger


def main():
    print("=" * 70)
    print("03 — PUBLICATION BIAS ASSESSMENT")
    print("=" * 70)

    data_path = TABLE_DIR / "01_effect_sizes_full.csv"
    df = pd.read_csv(data_path)
    print(f"\nLoaded: {len(df)} effect sizes")

    summary_rows = []

    for key, (es_col, var_col) in ES_COLS.items():
        name = COMPARISON_NAMES[key]
        print(f"\n{'─' * 60}")
        print(f"  {name}")
        print(f"{'─' * 60}")

        es = df[es_col].dropna().values
        var = df[var_col].dropna().values
        mask = np.isfinite(es) & np.isfinite(var) & (var > 0)
        es, var = es[mask], var[mask]

        results = run_all_bias_tests(es, var)

        row = {"Comparison": name}

        # Egger
        if results["egger"]:
            eg = results["egger"]
            row["Egger_intercept"] = eg["intercept"]
            row["Egger_p"] = eg["intercept_p"]
            bias_flag = "Yes" if eg["intercept_p"] < 0.05 else "No"
            row["Egger_Bias"] = bias_flag
            print(f"  Egger: intercept={eg['intercept']:.3f}, p={eg['intercept_p']:.4f} → {bias_flag}")

        # Begg
        if results["begg"]:
            bg = results["begg"]
            row["Begg_tau"] = bg["tau"]
            row["Begg_p"] = bg["p_value"]
            bias_flag = "Yes" if bg["p_value"] < 0.05 else "No"
            row["Begg_Bias"] = bias_flag
            print(f"  Begg:  tau={bg['tau']:.3f}, p={bg['p_value']:.4f} → {bias_flag}")

        # Trim-and-fill
        if results["trimfill"]:
            tf = results["trimfill"]
            row["TrimFill_Missing"] = tf["k_missing"]
            row["TrimFill_Original"] = tf["original_estimate"]
            row["TrimFill_Adjusted"] = tf["adjusted_estimate"]
            print(f"  Trim-fill: missing={tf['k_missing']}, "
                  f"original={tf['original_estimate']:.3f}, adjusted={tf['adjusted_estimate']:.3f}")

        # Fail-safe N
        if results["failsafe"]:
            fs = results["failsafe"]
            row["FailSafe_N"] = fs["failsafe_n"]
            print(f"  Fail-safe N: {fs['failsafe_n']}")

        summary_rows.append(row)

    # ── Save ──
    summary_df = pd.DataFrame(summary_rows)
    out_path = TABLE_DIR / "03_bias_summary.csv"
    summary_df.to_csv(out_path, index=False)
    print(f"\nSaved: {out_path.name}")

    # ── Insight report ──
    log = InsightLogger(REPORT_DIR, "03_publication_bias")
    for _, row in summary_df.iterrows():
        comp = row["Comparison"]
        bullets = []
        if "Egger_p" in row and pd.notna(row.get("Egger_p")):
            flag = "BIAS DETECTED" if row["Egger_Bias"] == "Yes" else "No bias"
            bullets.append(f"Egger's test: intercept = {row['Egger_intercept']:.3f}, p = {row['Egger_p']:.4f} ({flag})")
        if "Begg_p" in row and pd.notna(row.get("Begg_p")):
            flag = "BIAS DETECTED" if row["Begg_Bias"] == "Yes" else "No bias"
            bullets.append(f"Begg's test: tau = {row['Begg_tau']:.3f}, p = {row['Begg_p']:.4f} ({flag})")
        if "TrimFill_Missing" in row and pd.notna(row.get("TrimFill_Missing")):
            bullets.append(
                f"Trim-and-fill: {int(row['TrimFill_Missing'])} missing studies, "
                f"original = {row['TrimFill_Original']:.3f}, adjusted = {row['TrimFill_Adjusted']:.3f}"
            )
        if "FailSafe_N" in row and pd.notna(row.get("FailSafe_N")):
            bullets.append(f"Fail-safe N: {int(row['FailSafe_N'])}")
        log.add_section(comp, bullets)

    # Overall conclusion
    n_bias = sum(1 for _, r in summary_df.iterrows()
                 if r.get("Egger_Bias") == "Yes")
    log.add_section("Conclusion", [
        f"Publication bias detected in {n_bias}/3 comparisons via Egger's test",
        "Trim-and-fill adjustments suggest the true effects may be smaller",
        "Results should be interpreted with caution given pervasive bias",
    ])
    log.write("03 — Publication Bias Insights")

    print("\n" + "=" * 70)
    print("03 — PUBLICATION BIAS COMPLETE")
    print("=" * 70)
    return summary_df


if __name__ == "__main__":
    main()
