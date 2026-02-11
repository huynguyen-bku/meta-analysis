"""
Figure 2 — "Sai lệch công bố" (18×12", 600 DPI)

Row 1: [A: Contour funnel SS] [B: Contour funnel HU] [C: Contour funnel AI]
Row 2: [D: Egger regr SS]     [E: Egger regr HU]     [F: Egger regr AI]
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
from scipy import stats

from experiment_meta.config import TABLE_DIR, FIGURE_DIR, COLORS
from experiment_meta.visuals import apply_plot_style, save_figure, add_panel_label

apply_plot_style()


def main():
    print("\n[Figure 2] Sai lệch công bố")

    df = pd.read_csv(TABLE_DIR / "01_effect_sizes_full.csv")
    meta_path = TABLE_DIR / "02_meta_results.csv"
    meta_df = pd.read_csv(meta_path) if meta_path.exists() else None

    # Get pooled estimates
    pooled = {}
    if meta_df is not None:
        for _, row in meta_df.iterrows():
            if "Strong" in row["comparison"]:
                pooled["es_s"] = row["estimate"]
            elif "Human" in row["comparison"]:
                pooled["es_h"] = row["estimate"]
            elif "AI" in row["comparison"]:
                pooled["es_a"] = row["estimate"]

    fig = plt.figure(figsize=(18, 12))
    gs = gridspec.GridSpec(2, 3, figure=fig,
                           hspace=0.42, wspace=0.28,
                           left=0.06, right=0.97, top=0.91, bottom=0.08)

    comparisons = [
        ("es_s", "var_es_s", "Cộng hưởng mạnh", COLORS["synergy"]),
        ("es_h", "var_es_h", "AI hỗ trợ người", COLORS["human_aug"]),
        ("es_a", "var_es_a", "Người hỗ trợ AI", COLORS["ai_aug"]),
    ]

    for i, (es_col, var_col, title, color) in enumerate(comparisons):
        plot_data = df[[es_col, var_col]].dropna().copy()
        plot_data["SE"] = np.sqrt(plot_data[var_col])
        center = pooled.get(es_col, plot_data[es_col].mean())

        # ── Top row: Contour funnel ──
        ax_funnel = fig.add_subplot(gs[0, i])
        se_max = plot_data["SE"].max() * 1.1
        se_range = np.linspace(0.001, se_max, 200)

        z_001 = 2.576
        ax_funnel.fill_betweenx(se_range,
                                 center - z_001 * se_range,
                                 center + z_001 * se_range,
                                 color="#E8F5E9", alpha=0.5, zorder=0, label="p < 0.01")
        z_005 = 1.96
        ax_funnel.fill_betweenx(se_range,
                                 center - z_005 * se_range,
                                 center + z_005 * se_range,
                                 color="#FFF9C4", alpha=0.5, zorder=0, label="p < 0.05")
        z_010 = 1.645
        ax_funnel.fill_betweenx(se_range,
                                 center - z_010 * se_range,
                                 center + z_010 * se_range,
                                 color="#FFECB3", alpha=0.5, zorder=0, label="p < 0.10")

        ax_funnel.scatter(plot_data[es_col], plot_data["SE"],
                          s=30, alpha=0.55, color=color,
                          edgecolors="white", linewidths=0.4, zorder=5)
        ax_funnel.axvline(center, color="#E74C3C", linewidth=1.8,
                          linestyle="--", alpha=0.8, zorder=6)
        ax_funnel.invert_yaxis()
        ax_funnel.set_xlabel("Kích thước hiệu ứng (Hedges' g)", fontsize=11)
        ax_funnel.set_ylabel("Sai số chuẩn" if i == 0 else "", fontsize=11)
        ax_funnel.set_title(title, fontsize=12, fontweight="bold", pad=10)

        # ── Bottom row: Egger regression ──
        ax_egger = fig.add_subplot(gs[1, i])

        precision = 1.0 / plot_data["SE"]
        std_effect = plot_data[es_col] / plot_data["SE"]

        slope, intercept, r_val, p_val, se_slope = stats.linregress(precision, std_effect)

        ax_egger.scatter(precision, std_effect,
                         s=25, alpha=0.45, color=color,
                         edgecolors="white", linewidths=0.3, zorder=5)

        x_fit = np.linspace(precision.min(), precision.max(), 100)
        y_fit = slope * x_fit + intercept
        ax_egger.plot(x_fit, y_fit, color="#E74C3C", linewidth=2,
                      linestyle="-", alpha=0.8, zorder=6)

        y_expected = slope * x_fit
        ax_egger.plot(x_fit, y_expected, color="#999999", linewidth=1,
                      linestyle=":", alpha=0.6, zorder=4)

        ax_egger.set_xlabel("Độ chính xác (1/SE)", fontsize=11)
        ax_egger.set_ylabel("Hiệu ứng chuẩn hóa (g/SE)" if i == 0 else "", fontsize=11)
        ax_egger.set_title(f"Kiểm định Egger: {title}", fontsize=12,
                           fontweight="bold", pad=10)

        bias_detected = p_val < 0.05
        box_color = "#FFEBEE" if bias_detected else "#E8F5E9"
        border_color = "#C0392B" if bias_detected else "#27AE60"
        text_color = "#C0392B" if bias_detected else "#27AE60"
        bias_label = "PHÁT HIỆN SAI LỆCH" if bias_detected else "Không phát hiện sai lệch"
        p_str = "< 0.001" if p_val < 0.001 else f"= {p_val:.3f}"
        result_text = f"{bias_label}\nHệ số chặn = {intercept:.2f}\np {p_str}"

        ax_egger.text(0.97, 0.97, result_text,
                      transform=ax_egger.transAxes, va="top", ha="right",
                      fontsize=9, fontweight="bold", color=text_color,
                      bbox=dict(boxstyle="round,pad=0.5", facecolor=box_color,
                                edgecolor=border_color, linewidth=1.5, alpha=0.95))

    fig.suptitle("Đánh giá sai lệch công bố",
                 fontsize=16, fontweight="bold", y=0.985)

    save_figure(fig, FIGURE_DIR / "Figure2_Publication_Bias")


if __name__ == "__main__":
    main()
