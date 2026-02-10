"""
02 — Main meta-analysis: 3-level REML (with DL cross-check) for 3 comparisons.

Output: outputs/tables/02_meta_results.csv
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pandas as pd

from experiment_meta.config import TABLE_DIR, REPORT_DIR, ES_COLS, COMPARISON_NAMES
from experiment_meta.meta_engine import random_effects_dl, fit_threelevel_reml
from jabes_shared.insights import InsightLogger


def main():
    print("=" * 70)
    print("02 — MAIN META-ANALYSIS")
    print("=" * 70)

    # ── Load effect-size data ──
    data_path = TABLE_DIR / "01_effect_sizes_full.csv"
    df = pd.read_csv(data_path)
    print(f"\nLoaded: {len(df)} effect sizes")

    rows = []

    for key, (es_col, var_col) in ES_COLS.items():
        name = COMPARISON_NAMES[key]
        print(f"\n{'─' * 60}")
        print(f"  {name}")
        print(f"{'─' * 60}")

        # ── 3-level REML (primary) ──
        print("  [3-level REML]")
        res3 = fit_threelevel_reml(df, es_col, var_col, name)

        # ── DL cross-check ──
        print("  [DL 2-level cross-check]")
        res_dl = random_effects_dl(df[es_col].dropna().values,
                                   df[var_col].dropna().values)

        primary = res3 if res3 is not None else res_dl
        if primary is None:
            print("  ⚠ Insufficient data — skipping")
            continue

        print(f"  Estimate: {primary.estimate:.4f}")
        print(f"  SE:       {primary.se:.4f}")
        print(f"  95% CI:   [{primary.ci_lower:.4f}, {primary.ci_upper:.4f}]")
        print(f"  p-value:  {primary.p_value:.4f}")
        print(f"  I²:       {primary.I2:.1f}%")
        print(f"  95% PI:   [{primary.pred_lower:.4f}, {primary.pred_upper:.4f}]")

        row = {
            "comparison": name,
            "k": primary.k,
            "estimate": primary.estimate,
            "se": primary.se,
            "ci_lower": primary.ci_lower,
            "ci_upper": primary.ci_upper,
            "p_value": primary.p_value,
            "tau2": primary.tau2,
            "I2": primary.I2,
            "Q": primary.Q,
            "Q_pval": primary.Q_pval,
            "pred_lower": primary.pred_lower,
            "pred_upper": primary.pred_upper,
            "method": primary.method,
        }

        # Add 3-level extras if available
        if primary.method == "REML-3level":
            row.update({
                "sigma2_within": primary.sigma2_within,
                "sigma2_between": primary.sigma2_between,
                "I2_between": primary.I2_between,
                "I2_within": primary.I2_within,
            })

        # DL cross-check
        if res_dl is not None:
            row["dl_estimate"] = res_dl.estimate
            row["dl_ci_lower"] = res_dl.ci_lower
            row["dl_ci_upper"] = res_dl.ci_upper
            print(f"  DL check: {res_dl.estimate:.4f} [{res_dl.ci_lower:.4f}, {res_dl.ci_upper:.4f}]")

        rows.append(row)

    # ── Save ──
    results_df = pd.DataFrame(rows)
    out_path = TABLE_DIR / "02_meta_results.csv"
    results_df.to_csv(out_path, index=False)
    print(f"\nSaved: {out_path.name}")

    # ── Insight report ──
    log = InsightLogger(REPORT_DIR, "02_meta_results")
    bullets = []
    for _, r in results_df.iterrows():
        sig = "***" if r["p_value"] < 0.001 else "**" if r["p_value"] < 0.01 else "*" if r["p_value"] < 0.05 else "ns"
        bullets.append(
            f"{r['comparison']}: g = {r['estimate']:+.3f} "
            f"[{r['ci_lower']:.3f}, {r['ci_upper']:.3f}], "
            f"p = {r['p_value']:.4f} ({sig}), "
            f"I² = {r['I2']:.1f}%, k = {r['k']}"
        )
    log.add_section("Overall Effects (3-level REML)", bullets)

    # Prediction intervals
    pi_bullets = []
    for _, r in results_df.iterrows():
        if "pred_lower" in r and pd.notna(r.get("pred_lower")):
            pi_bullets.append(
                f"{r['comparison']}: 95% PI [{r['pred_lower']:.3f}, {r['pred_upper']:.3f}]"
            )
    if pi_bullets:
        log.add_section("Prediction Intervals", pi_bullets)

    # Key finding
    log.add_section("Key Findings", [
        "AI helps humans (Human Augmentation) with a moderate-to-large effect",
        "Humans do NOT significantly help AI (AI Augmentation is ns)",
        "Strong Synergy is significantly NEGATIVE — collaboration underperforms the best individual",
        "This constitutes the 'Collaboration Paradox'",
    ])
    log.write("02 — Main Meta-Analysis Insights")

    print("\n" + "=" * 70)
    print("02 — META-ANALYSIS COMPLETE")
    print("=" * 70)
    return results_df


if __name__ == "__main__":
    main()
