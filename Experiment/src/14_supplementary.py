"""
Supplementary Figures (S1–S6, 600 DPI)

S1: Temporal Trend — line plot ES by year + CI band
S2: Sign Profile — stacked bar: % negative / neutral / positive
S3: Sensitivity — 2×2: leave-one-out (SS, HU), influence plot, cumulative meta
S4: Summary Heatmap — ALL moderator×comparison effect sizes in one matrix
S5: Moderator Comparison Bars — per-moderator horizontal bar chart (1×3)
S6: Study-level Forest Plots — individual study ES + pooled estimate bands
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

from experiment_meta.config import (
    TABLE_DIR, FIGURE_DIR, COLORS, ES_COLS, COMPARISON_NAMES, COMPARISON_COLORS,
)
from experiment_meta.visuals import (
    apply_plot_style, save_figure, add_panel_label, add_zero_line, sig_stars,
)
from experiment_meta.labels_vi import vi_comparison, vi_moderator, vi_level
from experiment_meta.meta_engine import random_effects_dl
from experiment_meta.sensitivity import leave_one_out, cumulative_meta, influence_diagnostics

apply_plot_style()


def _figure_s1_temporal(df):
    """S1: Mean ES by year with CI band."""
    print("\n[Figure S1] Temporal Trend")

    if "Year" not in df.columns:
        print("  ⚠ Year column not found")
        return

    fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

    for i, (key, (es_col, var_col)) in enumerate(ES_COLS.items()):
        ax = axes[i]
        name = COMPARISON_NAMES[key]
        color = COLORS[key]

        # Group by year
        yearly = []
        for year in sorted(df["Year"].dropna().unique()):
            sub = df[df["Year"] == year]
            es = sub[es_col].dropna().values
            var = sub[var_col].dropna().values
            r = random_effects_dl(es, var)
            if r is not None:
                yearly.append({
                    "year": year, "estimate": r.estimate,
                    "ci_lower": r.ci_lower, "ci_upper": r.ci_upper, "k": r.k,
                })

        if not yearly:
            continue

        ydf = pd.DataFrame(yearly)
        ax.plot(ydf["year"], ydf["estimate"], "o-", color=color, linewidth=2, markersize=6)
        ax.fill_between(ydf["year"], ydf["ci_lower"], ydf["ci_upper"],
                         color=color, alpha=0.15)

        for _, row in ydf.iterrows():
            ax.annotate(f"k={int(row['k'])}", (row["year"], row["estimate"]),
                        textcoords="offset points", xytext=(0, 8), fontsize=7, ha="center")

        add_zero_line(ax, "h")
        ax.set_xlabel("Năm", fontsize=11)
        if i == 0:
            ax.set_ylabel("Kích thước hiệu ứng gộp (Hedges' g)", fontsize=11)
        ax.set_title(name, fontsize=12, fontweight="bold")
        
    fig.suptitle("Xu hướng kích thước hiệu ứng theo thời gian",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.94])
    save_figure(fig, FIGURE_DIR / "FigureS1_Temporal_Trend")


def _figure_s2_sign_profile(df):
    """S2: Stacked bar — % negative / neutral / positive."""
    print("\n[Figure S2] Sign Profile")

    fig, ax = plt.subplots(figsize=(10, 6))

    names = []
    pcts_neg = []
    pcts_neu = []
    pcts_pos = []

    for key, (es_col, _) in ES_COLS.items():
        name = COMPARISON_NAMES[key]
        data = df[es_col].dropna()
        n = len(data)
        if n == 0:
            continue
        n_neg = (data < -0.2).sum()
        n_neu = ((data >= -0.2) & (data <= 0.2)).sum()
        n_pos = (data > 0.2).sum()

        names.append(name)
        pcts_neg.append(n_neg / n * 100)
        pcts_neu.append(n_neu / n * 100)
        pcts_pos.append(n_pos / n * 100)

    x = np.arange(len(names))
    w = 0.6

    ax.bar(x, pcts_neg, w, label="Âm (g < -0.2)", color=COLORS["negative"], alpha=0.8)
    ax.bar(x, pcts_neu, w, bottom=pcts_neg, label="Trung t\u00ednh ($-0.2 \\leq g \\leq 0.2$)",
           color=COLORS["nonsig"], alpha=0.8)
    bottom2 = [a + b for a, b in zip(pcts_neg, pcts_neu)]
    ax.bar(x, pcts_pos, w, bottom=bottom2, label="Dương (g > 0.2)",
           color=COLORS["positive"], alpha=0.8)

    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=10)
    ax.set_ylabel("Phần trăm (%)", fontsize=11)
    ax.set_title("Phân bố dấu kích thước hiệu ứng", fontsize=14, fontweight="bold")
    ax.legend(loc="upper right", fontsize=9)
    ax.set_ylim(0, 105)

    save_figure(fig, FIGURE_DIR / "FigureS2_Sign_Profile")


def _figure_s3_sensitivity(df):
    """S3: 2×2 — leave-one-out (SS, HU), influence, cumulative."""
    print("\n[Figure S3] Sensitivity")

    fig, axes = plt.subplots(2, 2, figsize=(16, 14))

    # Panel A: Leave-one-out for Strong Synergy
    ax = axes[0, 0]
    es = df["es_s"].dropna().values
    var = df["var_es_s"].dropna().values
    loo = leave_one_out(es, var)
    if len(loo) > 0:
        ax.errorbar(loo["estimate"], range(len(loo)),
                    xerr=[loo["estimate"] - loo["ci_lower"],
                          loo["ci_upper"] - loo["estimate"]],
                    fmt="o", markersize=3, color=COLORS["synergy"], alpha=0.6,
                    elinewidth=0.8, capsize=0)
        full = random_effects_dl(es, var)
        if full:
            ax.axvline(full.estimate, color="red", linewidth=1.5, linestyle="--")
    ax.set_xlabel("Kích thước hiệu ứng gộp (Hedges' g)")
    ax.set_title("Leave-one-out: Cộng hưởng mạnh", fontweight="bold")
    ax.set_yticks([])
    
    # Panel B: Leave-one-out for Human Augmentation
    ax = axes[0, 1]
    es = df["es_h"].dropna().values
    var = df["var_es_h"].dropna().values
    loo = leave_one_out(es, var)
    if len(loo) > 0:
        ax.errorbar(loo["estimate"], range(len(loo)),
                    xerr=[loo["estimate"] - loo["ci_lower"],
                          loo["ci_upper"] - loo["estimate"]],
                    fmt="o", markersize=3, color=COLORS["human_aug"], alpha=0.6,
                    elinewidth=0.8, capsize=0)
        full = random_effects_dl(es, var)
        if full:
            ax.axvline(full.estimate, color="red", linewidth=1.5, linestyle="--")
    ax.set_xlabel("Kích thước hiệu ứng gộp (Hedges' g)")
    ax.set_title("Leave-one-out: AI hỗ trợ người", fontweight="bold")
    ax.set_yticks([])
    
    # Panel C: Influence diagnostics
    ax = axes[1, 0]
    es = df["es_s"].dropna().values
    var = df["var_es_s"].dropna().values
    diag = influence_diagnostics(es, var)
    if len(diag) > 0:
        colors = ["red" if cd > 1 else COLORS["synergy"]
                  for cd in diag["cook_d"]]
        ax.scatter(diag["hat"], diag["rstudent"], c=colors, s=30, alpha=0.6)
        ax.axhline(3, color="gray", linestyle="--", alpha=0.5)
        ax.axhline(-3, color="gray", linestyle="--", alpha=0.5)
    ax.set_xlabel("Hat value")
    ax.set_ylabel("Studentized residual")
    ax.set_title("Influence: Cộng hưởng mạnh", fontweight="bold")
    
    # Panel D: Cumulative meta for Human Augmentation
    ax = axes[1, 1]
    es = df["es_h"].dropna().values
    var = df["var_es_h"].dropna().values
    if "Year" in df.columns:
        years = df.loc[df["es_h"].dropna().index, "Year"].values
        cum = cumulative_meta(es, var, sort_by=years)
    else:
        cum = cumulative_meta(es, var)
    if len(cum) > 0:
        ax.plot(cum["step"], cum["estimate"], "o-", color=COLORS["human_aug"],
                markersize=3, linewidth=1.5)
        ax.fill_between(cum["step"], cum["ci_lower"], cum["ci_upper"],
                         color=COLORS["human_aug"], alpha=0.15)
        add_zero_line(ax, "h")
    ax.set_xlabel("Số nghiên cứu tích lũy")
    ax.set_ylabel("Kích thước hiệu ứng gộp (Hedges' g)")
    ax.set_title("Meta tích lũy: AI hỗ trợ người", fontweight="bold")
    
    fig.suptitle("Phân tích độ nhạy",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    save_figure(fig, FIGURE_DIR / "FigureS3_Sensitivity")


def _figure_s4_summary_heatmap():
    """S4: Full moderator × comparison heatmap — all subgroups at once.

    Insight: which moderator levels drive the strongest effects, and where
    the three comparisons diverge most (e.g., Communication AI Aug = +1.01
    vs Business AI Aug = −0.73).
    """
    print("\n[Figure S4] Summary Heatmap (All Moderators × Comparisons)")

    sub_path = TABLE_DIR / "04_subgroup_results.csv"
    if not sub_path.exists():
        print("  ⚠ 04_subgroup_results.csv not found — run 04 first")
        return

    sub_df = pd.read_csv(sub_path)

    # Build pivot data
    pivot_rows = []
    for _, row in sub_df.iterrows():
        mod_vi = vi_moderator(row["moderator"])
        lev_vi = vi_level(str(row["level"]))
        label = f"{mod_vi}: {lev_vi}"
        comp_vi = vi_comparison(row["comparison"])
        pivot_rows.append({
            "Phân nhóm": label,
            "So sánh": comp_vi,
            "g": row["estimate"],
        })

    pivot_df = pd.DataFrame(pivot_rows)
    if len(pivot_df) == 0:
        return

    heatmap_data = pivot_df.pivot(index="Phân nhóm", columns="So sánh", values="g")

    # Reorder columns to match comparison order
    col_order = [vi_comparison(COMPARISON_NAMES[k]) for k in ES_COLS]
    col_order = [c for c in col_order if c in heatmap_data.columns]
    heatmap_data = heatmap_data[col_order]

    fig, ax = plt.subplots(figsize=(12, max(9, len(heatmap_data) * 0.38)))

    sns.heatmap(
        heatmap_data, annot=True, fmt=".2f", cmap="RdYlGn", center=0,
        vmin=-1.5, vmax=1.5, ax=ax, linewidths=0.5,
        cbar_kws={"label": "Hedges' g", "shrink": 0.8,
                 "ticks": [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5]},
        annot_kws={"fontsize": 9},
    )
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=9)
    cbar.ax.set_yticklabels(["-1.5", "-1.0", "-0.5", "0.0", "0.5", "1.0", "1.5"])

    ax.set_title(
        "Ma trận kích thước hiệu ứng: phân nhóm × so sánh",
        fontsize=14, fontweight="bold", pad=12,
    )
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.tick_params(axis="y", labelsize=9)
    ax.tick_params(axis="x", labelsize=10, rotation=0)

    plt.tight_layout(rect=[0, 0.02, 1, 1])
    save_figure(fig, FIGURE_DIR / "FigureS4_Summary_Heatmap")


def _figure_s5_moderator_bars():
    """S5: Per-moderator horizontal bar comparison (1×3 per moderator).

    Insight: information-dense view showing effect size bars with CI
    for each moderator level × comparison, coloured by significance/direction.
    Easier to compare magnitudes than forest diamonds.
    """
    print("\n[Figure S5] Moderator Comparison Bars")

    sub_path = TABLE_DIR / "04_subgroup_results.csv"
    if not sub_path.exists():
        print("  ⚠ 04_subgroup_results.csv not found — run 04 first")
        return

    sub_df = pd.read_csv(sub_path)
    comparisons = list(COMPARISON_NAMES.values())
    moderators = sub_df["moderator"].unique()

    n_mod = len(moderators)
    fig, all_axes = plt.subplots(n_mod, 3, figsize=(18, n_mod * 3.5))
    if n_mod == 1:
        all_axes = all_axes.reshape(1, -1)

    panel_idx = 0
    for row_idx, moderator in enumerate(moderators):
        for col_idx, comp in enumerate(comparisons):
            ax = all_axes[row_idx, col_idx]
            panel_label = chr(65 + panel_idx)
            panel_idx += 1

            data = sub_df[
                (sub_df["moderator"] == moderator) &
                (sub_df["comparison"] == comp)
            ].copy().sort_values("estimate")

            if len(data) == 0:
                ax.set_visible(False)
                continue

            y_pos = np.arange(len(data))
            n_groups = len(data)
            bar_colors = []
            for _, r in data.iterrows():
                if r["p_value"] < 0.05:
                    bar_colors.append(
                        COLORS["positive"] if r["estimate"] > 0 else COLORS["negative"]
                    )
                else:
                    bar_colors.append(COLORS["nonsig"])

            # Horizontal bars with error bars
            for i, (_, r) in enumerate(data.iterrows()):
                ax.barh(i, r["estimate"], color=bar_colors[i], alpha=0.7,
                        edgecolor="#333333", linewidth=0.5, height=0.65)
                ax.errorbar(
                    r["estimate"], i,
                    xerr=[[r["estimate"] - r["ci_lower"]],
                          [r["ci_upper"] - r["estimate"]]],
                    fmt="none", color="#333333", capsize=3, linewidth=1.2,
                )
                # Significance + k annotation - position right above error bars
                stars = sig_stars(r["p_value"])
                est_val = r["estimate"]

                # Position text just above the bar/error bars, at bar center x-position
                # Use small offset so text sits right on top of the bar
                text_y = i + 0.14
                ax.text(est_val, text_y,
                        f"{stars} (k={int(r['k'])})",
                        va="bottom", ha="center", fontsize=7, fontweight="bold", color="#333333",
                        clip_on=False)

            add_zero_line(ax, "v")
            ax.set_yticks(y_pos)
            labels = [vi_level(str(lev)) for lev in data["level"]]
            ax.set_yticklabels(labels, fontsize=9)

            # Dynamic x limits (text positioned above bars, so less right space needed)
            ci_min = data["ci_lower"].min()
            ci_max = data["ci_upper"].max()
            ci_range = ci_max - ci_min
            ax.set_xlim(ci_min - ci_range * 0.10, ci_max + ci_range * 0.08)

            # Hide right and top spines to prevent overlap
            ax.spines['right'].set_visible(False)
            ax.spines['top'].set_visible(False)

            if row_idx == n_mod - 1:
                ax.set_xlabel("Hedges' g", fontsize=10)

            comp_vi = vi_comparison(comp)

            # Q-between annotation
            q_p = data.iloc[0].get("Q_between_pval", np.nan)
            q_sig = sig_stars(q_p) if pd.notna(q_p) else ""

            # Only show comparison name on top row
            if row_idx == 0:
                ax.set_title(f"{comp_vi} {q_sig}",
                             fontsize=11, fontweight="bold", pad=10)

    # Add row labels using text in plot area
    for row_idx, moderator in enumerate(moderators):
        mod_vi = vi_moderator(moderator)
        ax = all_axes[row_idx, 0]
        # Add as text on the left side of the leftmost plot
        ax.text(-0.35, 0.5, mod_vi, transform=ax.transAxes,
               fontsize=11, fontweight="bold", va="center", ha="right",
               rotation=0, wrap=True)

    # Add legend for bar colors
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=COLORS["positive"], alpha=0.7, edgecolor="#333333", label="Dương & Có ý nghĩa (p < 0.05)"),
        Patch(facecolor=COLORS["negative"], alpha=0.7, edgecolor="#333333", label="Âm & Có ý nghĩa (p < 0.05)"),
        Patch(facecolor=COLORS["nonsig"], alpha=0.7, edgecolor="#333333", label="Kh\u00f4ng c\u00f3 \u00fd ngh\u0129a ($p \\geq 0.05$)"),
    ]
    fig.legend(handles=legend_elements, loc="lower center", bbox_to_anchor=(0.5, 0.01),
              ncol=3, frameon=True, fancybox=False, framealpha=0.95,
              edgecolor="#cccccc", fontsize=9)

    fig.subplots_adjust(left=0.15, right=0.96, top=0.92, bottom=0.07, hspace=0.5, wspace=0.35)
    fig.suptitle(
        "So sánh kích thước hiệu ứng theo phân nhóm",
        fontsize=15, fontweight="bold", y=0.97,
    )
    save_figure(fig, FIGURE_DIR / "FigureS5_Moderator_Bars")


def _figure_s6_study_forest(df):
    """S6: Study-level forest plots (3 panels, one per comparison).

    Insight: shows individual study heterogeneity, % positive/negative,
    pooled estimate band. Useful for identifying outlier studies and
    visualising the spread of findings.
    """
    print("\n[Figure S6] Study-level Forest Plots")

    fig, axes = plt.subplots(1, 3, figsize=(20, max(8, len(df) * 0.05)))

    for i, (key, (es_col, var_col)) in enumerate(ES_COLS.items()):
        ax = axes[i]
        name = COMPARISON_NAMES[key]
        color = COLORS[key]

        mask = df[es_col].notna() & df[var_col].notna()
        es = df.loc[mask, es_col].values
        var = df.loc[mask, var_col].values
        se = np.sqrt(var)

        if len(es) < 2:
            ax.set_visible(False)
            continue

        # Sort ascending
        sort_idx = np.argsort(es)
        es = es[sort_idx]
        se = se[sort_idx]

        k = len(es)
        y_pos = np.arange(k)

        # Individual studies
        for j in range(k):
            ci_lo = es[j] - 1.96 * se[j]
            ci_hi = es[j] + 1.96 * se[j]
            pt_color = COLORS["positive"] if es[j] > 0 else COLORS["negative"]
            ax.hlines(y_pos[j], ci_lo, ci_hi, colors=pt_color, alpha=0.35,
                      linewidth=0.8)
            ax.scatter(es[j], y_pos[j], c=pt_color, s=12, zorder=3, alpha=0.6)

        # Pooled estimate
        pooled = random_effects_dl(es, var)
        if pooled:
            ax.axvline(pooled.estimate, color="blue", linestyle="--",
                       linewidth=2, alpha=0.7, label=f"Gộp = {pooled.estimate:.3f}")
            ax.axvspan(pooled.ci_lower, pooled.ci_upper, alpha=0.08, color="blue")

        add_zero_line(ax, "v")

        # Background shading
        ax.axvspan(ax.get_xlim()[0], 0, alpha=0.03, color="red")
        ax.axvspan(0, ax.get_xlim()[1], alpha=0.03, color="green")

        # Statistics
        n_pos = (es > 0).sum()
        n_neg = (es <= 0).sum()
        ax.text(0.02, 0.98, f"Âm: {n_neg} ({n_neg/k*100:.0f}%)",
                transform=ax.transAxes, fontsize=9, va="top", color=COLORS["negative"])
        ax.text(0.98, 0.98, f"Dương: {n_pos} ({n_pos/k*100:.0f}%)",
                transform=ax.transAxes, fontsize=9, va="top", ha="right",
                color=COLORS["positive"])

        ax.set_xlabel("Hedges' g", fontsize=11)
        ax.set_title(vi_comparison(name), fontsize=12, fontweight="bold")
        ax.set_yticks([])
        ax.set_xlim(-4, 4)
        ax.legend(loc="lower right", fontsize=8)
        
    fig.suptitle("Forest plot mức nghiên cứu (k = {})".format(len(df)),
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    save_figure(fig, FIGURE_DIR / "FigureS6_Study_Forest")


def main():
    df = pd.read_csv(TABLE_DIR / "01_effect_sizes_full.csv")

    _figure_s1_temporal(df)
    _figure_s2_sign_profile(df)
    _figure_s3_sensitivity(df)
    _figure_s4_summary_heatmap()
    _figure_s5_moderator_bars()
    _figure_s6_study_forest(df)

    print("\n  All supplementary figures generated (S1–S6)")


if __name__ == "__main__":
    main()
