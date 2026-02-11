"""
Figure 1 — "Nghịch lý Cộng tác" (18×14", 600 DPI)

Row 1: [A: Histogram es_h] [B: Histogram es_a] [C: Histogram es_s]
Row 2: [D: Forest plot — 3 pooled estimates]
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
from matplotlib.lines import Line2D
from scipy import stats

from experiment_meta.config import TABLE_DIR, FIGURE_DIR, COLORS, COMPARISON_COLORS
from experiment_meta.visuals import apply_plot_style, save_figure, add_panel_label, add_zero_line, sig_stars
from experiment_meta.labels_vi import vi_comparison

apply_plot_style()


def main():
    print("\n[Figure 1] Nghịch lý Cộng tác")

    df = pd.read_csv(TABLE_DIR / "01_effect_sizes_full.csv")
    meta_df = pd.read_csv(TABLE_DIR / "02_meta_results.csv") if (TABLE_DIR / "02_meta_results.csv").exists() else None

    fig = plt.figure(figsize=(18, 14))
    gs = gridspec.GridSpec(2, 3, figure=fig,
                           height_ratios=[1, 1.15],
                           hspace=0.35, wspace=0.28,
                           left=0.06, right=0.98, top=0.91, bottom=0.11)

    comparisons = [
        ("es_h", "AI hỗ trợ người (HAI so với con người)", COLORS["human_aug"]),
        ("es_a", "Người hỗ trợ AI (HAI so với AI đơn lẻ)", COLORS["ai_aug"]),
        ("es_s", "Cộng hưởng mạnh (HAI so với mốc tốt nhất)", COLORS["synergy"]),
    ]

    # ── Row 1: Histograms (A, B, C) ──
    for i, (es_col, title, color) in enumerate(comparisons):
        ax = fig.add_subplot(gs[0, i])
        data = df[es_col].dropna()

        n_bins = min(35, max(15, len(data) // 8))
        ax.hist(data, bins=n_bins, alpha=0.65, color=color,
                edgecolor="white", linewidth=0.6, density=False, zorder=2)

        ax2 = ax.twinx()
        kde_x = np.linspace(data.min() - 0.5, data.max() + 0.5, 300)
        kde = stats.gaussian_kde(data)
        ax2.plot(kde_x, kde(kde_x), color=color, linewidth=2, alpha=0.9, zorder=3)
        ax2.set_ylabel("")
        ax2.set_yticks([])
        ax2.spines["right"].set_visible(False)
        ax2.spines["top"].set_visible(False)

        mean_val = data.mean()
        ax.axvline(mean_val, color="#222222", linewidth=1.8, linestyle="--", alpha=0.8, zorder=4)
        ax.axvline(0, color=COLORS["zero"], linewidth=1.2, linestyle="-", alpha=0.5, zorder=1)

        n_pos = (data > 0).sum()
        pct_pos = n_pos / len(data) * 100
        stats_text = (
            f"n = {len(data)}\n"
            f"Trung bình = {mean_val:.3f}\n"
            f"SD = {data.std():.3f}\n"
            f"Biên độ: [{data.min():.2f}, {data.max():.2f}]\n"
            f"Dương tính: {n_pos} ({pct_pos:.1f}%)"
        )
        ax.text(0.97, 0.97, stats_text,
                transform=ax.transAxes, va="top", ha="right",
                fontsize=8.5, family="monospace",
                bbox=dict(boxstyle="round,pad=0.5", facecolor="white",
                          edgecolor="#bbbbbb", alpha=0.95, linewidth=0.8))

        ax.set_xlabel("Kích thước hiệu ứng (Hedges' g)", fontsize=11)
        ax.set_ylabel("Tần suất", fontsize=11)
        ax.set_title(title, fontsize=12, fontweight="bold", pad=10)

    # ── Row 2 (D): Forest plot ──
    ax_forest = fig.add_subplot(gs[1, :])

    if meta_df is not None and len(meta_df) > 0:
        n_comp = len(meta_df)
        y_positions = np.arange(n_comp)[::-1]

        for idx, row in meta_df.iterrows():
            y = y_positions[idx]
            est = row["estimate"]
            ci_lo = row["ci_lower"]
            ci_hi = row["ci_upper"]
            p = row["p_value"]

            if "Strong" in row["comparison"]:
                color = COLORS["synergy"]
            elif "Human" in row["comparison"]:
                color = COLORS["human_aug"]
            else:
                color = COLORS["ai_aug"]

            ax_forest.plot([ci_lo, ci_hi], [y, y],
                           color=color, linewidth=3, alpha=0.7, zorder=2,
                           solid_capstyle="round")
            ax_forest.scatter(est, y, s=200, color=color,
                              edgecolors="white", linewidth=1.5,
                              marker="D", zorder=10)

            # Annotation
            stars = sig_stars(p)
            i2_val = row.get("I2", np.nan)
            anno = f"g = {est:.3f} [{ci_lo:.3f}, {ci_hi:.3f}] {stars}"
            if pd.notna(i2_val):
                anno += f", I² = {i2_val:.1f}%"
            ax_forest.text(ci_hi + 0.05, y, anno, va="center", ha="left", fontsize=9.5)

        add_zero_line(ax_forest, "v")

        xlim_lo = min(meta_df["ci_lower"].min() - 0.45, -1.0)
        xlim_hi = max(meta_df["ci_upper"].max() + 1.8, 1.5)
        ax_forest.set_xlim(xlim_lo, xlim_hi)
        ax_forest.set_ylim(-0.6, n_comp - 0.25)

        ax_forest.set_yticks(y_positions)
        ax_forest.set_yticklabels(
            [vi_comparison(r).replace(" ", "\n") for r in meta_df["comparison"]],
            fontsize=11, fontweight="bold")
        ax_forest.set_xlabel("Kích thước hiệu ứng gộp (Hedges' g)", fontsize=12,
                             fontweight="bold")
        ax_forest.set_title("Hiệu ứng gộp (mô hình 3 mức)",
                            fontsize=13, fontweight="bold", pad=16)

        legend_elements = [
            Line2D([0], [0], marker="D", color="w", markerfacecolor=COLORS["synergy"],
                   markersize=10, markeredgecolor="white", label="Cộng hưởng mạnh"),
            Line2D([0], [0], marker="D", color="w", markerfacecolor=COLORS["human_aug"],
                   markersize=10, markeredgecolor="white", label="AI hỗ trợ người"),
            Line2D([0], [0], marker="D", color="w", markerfacecolor=COLORS["ai_aug"],
                   markersize=10, markeredgecolor="white", label="Người hỗ trợ AI"),
        ]
        ax_forest.legend(handles=legend_elements,
                         loc="lower center", bbox_to_anchor=(0.5, -0.23),
                         ncol=3, frameon=True, fancybox=False,
                         framealpha=0.95, edgecolor="#cccccc", fontsize=9)

    fig.suptitle("Tổng quan về kích thước hiệu ứng trong meta-phân tích cộng tác người-AI",
                 fontsize=16, fontweight="bold", y=0.985)

    save_figure(fig, FIGURE_DIR / "Figure1_Overview")


if __name__ == "__main__":
    main()
