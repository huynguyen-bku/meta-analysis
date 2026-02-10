"""
Figure 3 — "Bối cảnh quyết định" (20×16", 600 DPI)

4 rows × 3 columns (12 panels)
  Rows: Industry, Task_Type, AI_Type_Cleaned, Participant_Expert
  Cols: Strong Synergy, Human Augmentation, AI Augmentation
"""

import sys
from pathlib import Path
import textwrap

sys.path.insert(0, str(Path(__file__).parent))

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.lines import Line2D

from experiment_meta.config import TABLE_DIR, FIGURE_DIR, COLORS
from experiment_meta.visuals import (
    apply_plot_style, save_figure, add_panel_label, add_zero_line, sig_stars,
)
from experiment_meta.labels_vi import vi_comparison, vi_moderator, vi_level

apply_plot_style()


def main():
    print("\n[Figure 3] Moderator Forest Plots")

    sub_path = TABLE_DIR / "04_subgroup_results.csv"
    if not sub_path.exists():
        print("  ⚠ 04_subgroup_results.csv not found — run 04 first")
        return

    sub_df = pd.read_csv(sub_path)

    moderators = ["Industry", "Task_Type", "AI_Type_Cleaned", "Participant_Expert"]
    comparisons = ["Strong Synergy", "Human Augmentation", "AI Augmentation"]

    fig = plt.figure(figsize=(20, 16))
    gs = gridspec.GridSpec(4, 3, figure=fig,
                           hspace=0.40, wspace=0.32,
                           left=0.20, right=0.96, top=0.88, bottom=0.09)

    # Store Q-values for column headers
    q_sigs = {(mod, comp): None for mod in moderators for comp in comparisons}

    # First pass: collect Q-between values for all combinations
    for moderator in moderators:
        for comparison in comparisons:
            data = sub_df[
                (sub_df["moderator"] == moderator) &
                (sub_df["comparison"] == comparison)
            ]
            if len(data) > 0:
                q_p = data.iloc[0].get("Q_between_pval", np.nan)
                q_sigs[(moderator, comparison)] = sig_stars(q_p) if pd.notna(q_p) else ""

    # Second pass: plot subplots
    for row_idx, moderator in enumerate(moderators):
        for col_idx, comparison in enumerate(comparisons):
            ax = fig.add_subplot(gs[row_idx, col_idx])

            data = sub_df[
                (sub_df["moderator"] == moderator) &
                (sub_df["comparison"] == comparison)
            ].copy()

            if len(data) == 0:
                ax.text(0.5, 0.5, "Chưa có dữ liệu", transform=ax.transAxes,
                        ha="center", va="center", fontsize=10, color="#999999")
                continue

            data = data.sort_values("estimate")
            n_groups = len(data)
            y_pos = np.arange(n_groups)

            for j, (_, row) in enumerate(data.iterrows()):
                est = row["estimate"]
                ci_lo = row["ci_lower"]
                ci_hi = row["ci_upper"]
                p = row["p_value"]
                k = int(row["k"])

                dot_color = COLORS["sig"] if p < 0.05 else COLORS["nonsig"]
                dot_alpha = 0.9 if p < 0.05 else 0.7

                ax.plot([ci_lo, ci_hi], [y_pos[j], y_pos[j]],
                        color=dot_color, linewidth=2.5,
                        alpha=dot_alpha * 0.7,
                        zorder=2, solid_capstyle="round")

                ax.scatter(est, y_pos[j], s=120, color=dot_color,
                           edgecolors="white", linewidth=1.2,
                           marker="D", zorder=10, alpha=dot_alpha)

            add_zero_line(ax, "v")

            ax.set_yticks(y_pos)
            labels = [vi_level(str(lev)) for lev in data["level"]]
            ax.set_yticklabels(labels, fontsize=9, ha="right")
            ax.set_ylim(-0.5, n_groups - 0.5)

            if row_idx == len(moderators) - 1:
                ax.set_xlabel("Kích thước hiệu ứng (Hedges' g)", fontsize=10)

            # Column titles (comparison names) - only on top row
            if row_idx == 0:
                comp_vi = vi_comparison(comparison)
                q_sig = q_sigs[(moderator, comparison)]
                ax.set_title(f"{comp_vi} {q_sig}",
                             fontsize=11, fontweight="bold", pad=10)

            ax.xaxis.grid(True, alpha=0.15, linestyle="-", linewidth=0.5)

        # Row titles (moderator names) - on the left side with text wrapping
        mod_clean = vi_moderator(moderator)
        # Wrap long moderator names to 2 lines
        wrapped_mod = "\n".join(textwrap.wrap(mod_clean, width=18))
        fig.text(0.07, 0.88 - (row_idx + 0.5) * (0.79 / len(moderators)),
                wrapped_mod, fontsize=10, fontweight="bold",
                va="center", ha="right", rotation=0, multialignment="right")

    # Legend
    legend_elements = [
        Line2D([0], [0], marker="D", color="w", markerfacecolor=COLORS["sig"],
               markersize=10, markeredgecolor="white", label="p < 0.05"),
        Line2D([0], [0], marker="D", color="w", markerfacecolor=COLORS["nonsig"],
               markersize=10, markeredgecolor="white", label="p >= 0.05"),
    ]
    fig.legend(handles=legend_elements,
               loc="lower center", bbox_to_anchor=(0.5, 0.01),
               ncol=2, frameon=True, fancybox=False,
               framealpha=0.95, edgecolor="#cccccc", fontsize=10)

    fig.suptitle("Phân tích yếu tố điều chỉnh: kích thước hiệu ứng theo nhóm con",
                 fontsize=16, fontweight="bold", y=0.96)

    save_figure(fig, FIGURE_DIR / "Figure3_Moderator_ForestPlots")


if __name__ == "__main__":
    main()
