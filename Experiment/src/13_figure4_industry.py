"""
Figure 4 — "Ngành là chìa khóa" (20×12", 600 DPI)

Row 1: [A: Violin SS×Industry] [B: Violin HU×Industry] [C: Violin AI×Industry]
Row 2: [D: Forest tổng hợp Industry×Comparison] [E: Heatmap 4×3]
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
from matplotlib.lines import Line2D
import seaborn as sns

from experiment_meta.config import TABLE_DIR, FIGURE_DIR, COLORS
from experiment_meta.visuals import (
    apply_plot_style, save_figure, add_panel_label, add_zero_line, sig_stars,
)
from experiment_meta.labels_vi import vi_level

apply_plot_style()

INDUSTRIES = ["Business", "Communication", "Healthcare", "Public sector"]


def main():
    print("\n[Figure 4] Industry Comprehensive")

    df = pd.read_csv(TABLE_DIR / "01_effect_sizes_full.csv")
    sub_path = TABLE_DIR / "04_subgroup_results.csv"
    sub_df = pd.read_csv(sub_path) if sub_path.exists() else None

    fig = plt.figure(figsize=(20, 12))
    gs = gridspec.GridSpec(2, 4, figure=fig,
                           height_ratios=[1, 1.2],
                           hspace=0.40, wspace=0.30,
                           left=0.06, right=0.97, top=0.90, bottom=0.10)

    comparisons_info = [
        ("es_s", "Cộng hưởng mạnh", COLORS["synergy"]),
        ("es_h", "AI hỗ trợ người", COLORS["human_aug"]),
        ("es_a", "Người hỗ trợ AI", COLORS["ai_aug"]),
    ]

    # ── Top row (A-C): Violin plots ──
    for i, (es_col, title, color) in enumerate(comparisons_info):
        ax = fig.add_subplot(gs[0, i])

        plot_data = []
        plot_labels = []
        for ind in INDUSTRIES:
            ind_data = df[df["Industry"] == ind][es_col].dropna()
            if len(ind_data) > 0:
                plot_data.append(ind_data.values)
                plot_labels.append(f"{vi_level(ind)}\n(n={len(ind_data)})")
            else:
                plot_data.append(np.array([0]))
                plot_labels.append(f"{vi_level(ind)}\n(n=0)")

        parts = ax.violinplot(plot_data, positions=range(len(INDUSTRIES)),
                               showmeans=True, showmedians=False,
                               showextrema=False)

        for pc in parts["bodies"]:
            pc.set_facecolor(color)
            pc.set_alpha(0.3)
            pc.set_edgecolor(color)
            pc.set_linewidth(1)
        parts["cmeans"].set_color(color)
        parts["cmeans"].set_linewidth(2)

        for j, dat in enumerate(plot_data):
            rng = np.random.default_rng(20260207 + i * 17 + j)
            jitter = rng.normal(0, 0.06, len(dat))
            ax.scatter(j + jitter, dat, s=12, alpha=0.4, color=color,
                       edgecolors="none", zorder=5)

        add_zero_line(ax, "h")

        ax.set_xticks(range(len(INDUSTRIES)))
        ax.set_xticklabels(plot_labels, fontsize=8, rotation=45, ha="right")
        ax.set_ylabel("Kích thước hiệu ứng (Hedges' g)" if i == 0 else "", fontsize=10)
        ax.set_title(title, fontsize=12, fontweight="bold", pad=8)
        
    # ── Top-right panel: sample sizes ──
    ax_legend = fig.add_subplot(gs[0, 3])
    ax_legend.axis("off")
    ax_legend.set_xlim(0, 1)
    ax_legend.set_ylim(0, 1)

    # Draw legend box background - properly framed around content
    legend_box = mpatches.FancyBboxPatch(
        (0.06, 0.08), 0.88, 0.87,
        boxstyle="round,pad=0.02", facecolor="white", edgecolor="#cccccc",
        linewidth=0.8, alpha=0.98, transform=ax_legend.transAxes)
    ax_legend.add_patch(legend_box)

    ax_legend.text(0.10, 0.90, "Cỡ mẫu theo ngành", fontsize=10,
                   fontweight="bold", va="top", ha="left", transform=ax_legend.transAxes)

    for j, ind in enumerate(INDUSTRIES):
        n_total = len(df[df["Industry"] == ind])
        ax_legend.text(0.10, 0.82 - j * 0.12,
                       f"{vi_level(ind)}: n={n_total}",
                       fontsize=8.5, va="top", ha="left", transform=ax_legend.transAxes)

    y_start = 0.28
    ax_legend.text(0.10, y_start, "Comparisons:", fontsize=9,
                   fontweight="bold", va="top", ha="left", transform=ax_legend.transAxes)

    y_start = 0.21
    for (_, title, color) in comparisons_info:
        ax_legend.add_patch(mpatches.Rectangle(
            (0.10, y_start - 0.02), 0.04, 0.025,
            facecolor=color, edgecolor="none",
            alpha=0.75, transform=ax_legend.transAxes))
        ax_legend.text(0.16, y_start - 0.0075, title, fontsize=8, va="center", ha="left",
                       transform=ax_legend.transAxes)
        y_start -= 0.065

    # ── Bottom-left (D): Aggregated forest ──
    ax_agg = fig.add_subplot(gs[1, :3])

    if sub_df is not None:
        industry_data = sub_df[sub_df["moderator"] == "Industry"].copy()
        comparisons_list = ["Strong Synergy", "Human Augmentation", "AI Augmentation"]
        comp_colors_map = {
            "Strong Synergy": COLORS["synergy"],
            "Human Augmentation": COLORS["human_aug"],
            "AI Augmentation": COLORS["ai_aug"],
        }

        y_counter = 0
        y_ticks = []
        y_labels = []

        for comp in comparisons_list:
            comp_data = industry_data[industry_data["comparison"] == comp].sort_values("estimate")
            color = comp_colors_map[comp]

            for _, row in comp_data.iterrows():
                est = row["estimate"]
                ci_lo = row["ci_lower"]
                ci_hi = row["ci_upper"]
                p = row["p_value"]
                k = int(row["k"])

                sig = p < 0.05
                alpha_val = 0.9 if sig else 0.5
                marker = "D" if sig else "o"

                ax_agg.plot([ci_lo, ci_hi], [y_counter, y_counter],
                            color=color, linewidth=2.5,
                            alpha=alpha_val * 0.7, zorder=2, solid_capstyle="round")
                ax_agg.scatter(est, y_counter, s=100, color=color,
                               edgecolors="white", linewidth=1,
                               marker=marker, zorder=10, alpha=alpha_val)

                y_ticks.append(y_counter)
                y_labels.append(f"{vi_level(row['level'])} (k={k})")
                y_counter += 1

            y_counter += 0.7

        add_zero_line(ax_agg, "v")
        ax_agg.set_yticks(y_ticks)
        ax_agg.set_yticklabels(y_labels, fontsize=9)
        ax_agg.set_xlabel("Kích thước hiệu ứng gộp (Hedges' g)", fontsize=11, fontweight="bold")
        ax_agg.set_title("Ngành công nghiệp × Đối sánh: Forest tổng hợp",
                         fontsize=13, fontweight="bold", pad=10)

        legend_elements = [
            Line2D([0], [0], marker="D", color="w", markerfacecolor=COLORS["synergy"],
                   markersize=9, markeredgecolor="white", label="Cộng hưởng mạnh"),
            Line2D([0], [0], marker="D", color="w", markerfacecolor=COLORS["human_aug"],
                   markersize=9, markeredgecolor="white", label="AI hỗ trợ người"),
            Line2D([0], [0], marker="D", color="w", markerfacecolor=COLORS["ai_aug"],
                   markersize=9, markeredgecolor="white", label="Người hỗ trợ AI"),
        ]
        ax_agg.legend(handles=legend_elements,
                      loc="lower center", bbox_to_anchor=(0.5, -0.22),
                      ncol=3, frameon=True, fancybox=False,
                      framealpha=0.95, edgecolor="#cccccc", fontsize=9)

    # ── Bottom-right (E): Heatmap ──
    ax_heat = fig.add_subplot(gs[1, 3])

    if sub_df is not None:
        industry_data = sub_df[sub_df["moderator"] == "Industry"].copy()
        industry_pivot = industry_data.pivot_table(
            index="level", columns="comparison", values="estimate"
        )

        comparisons_list = ["Strong Synergy", "Human Augmentation", "AI Augmentation"]
        row_order = [ind for ind in INDUSTRIES if ind in industry_pivot.index]
        col_order = [c for c in comparisons_list if c in industry_pivot.columns]

        if row_order and col_order:
            industry_pivot = industry_pivot.loc[row_order, col_order]
            col_short = {
                "Strong Synergy": "Cộng\nhưởng",
                "Human Augmentation": "AI hỗ trợ\nngười",
                "AI Augmentation": "Người\nhỗ trợ AI",
            }
            industry_pivot.columns = [col_short.get(c, c) for c in industry_pivot.columns]
            industry_pivot.index = [vi_level(i) for i in industry_pivot.index]

            sns.heatmap(industry_pivot, annot=True, fmt=".2f",
                        cmap="RdYlGn", center=0, vmin=-1.5, vmax=1.5,
                        linewidths=1, linecolor="white",
                        cbar_kws={"label": "Hedges' g", "shrink": 0.8,
                                 "ticks": [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5]},
                        ax=ax_heat,
                        annot_kws={"fontsize": 10, "fontweight": "bold"})
            cbar = ax_heat.collections[0].colorbar
            cbar.ax.tick_params(labelsize=9)
            cbar.ax.set_yticklabels(["-1.5", "-1.0", "-0.5", "0.0", "0.5", "1.0", "1.5"])

            ax_heat.set_xlabel("")
            ax_heat.set_ylabel("")
            ax_heat.set_title("Ma trận kích thước hiệu ứng", fontsize=12,
                              fontweight="bold", pad=10)

    fig.suptitle("Kích thước hiệu ứng theo ngành công nghiệp trong cộng tác người-AI",
                 fontsize=16, fontweight="bold", y=0.985)

    save_figure(fig, FIGURE_DIR / "Figure4_Industry_Comprehensive")


if __name__ == "__main__":
    main()
