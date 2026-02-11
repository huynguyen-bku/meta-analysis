#!/usr/bin/env python3
"""Figure 5 — Meta-regression coefficient plot.

Horizontal forest plot of β estimates ± 95% CI for each predictor,
one panel per comparison.  Significant coefficients (p < .05) are
shown as filled markers; non-significant as open markers.

Output: outputs/figures/Figure5_MetaRegression_Coefficients.{png,pdf}
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from experiment_meta.config import TABLE_DIR, FIGURE_DIR, COMPARISON_COLORS
from experiment_meta.visuals import apply_plot_style, save_figure, add_panel_label, add_zero_line, sig_stars

apply_plot_style()

# ── Vietnamese labels for predictor terms ────────────────────────────
TERM_LABELS = {
    "IndustryBusiness":           "Kinh doanh",
    "IndustryCommunication":      "Truyền thông",
    "IndustryPublic sector":      "Khu vực công",
    "Task_TypeCreate":            "Sáng tạo",
    "AI_Type_CleanedRule-Based":  "Dựa trên quy luật",
    "AI_Type_CleanedShallow":     "ML truyền thống",
    "AI_Type_CleanedSimulated-AI":"AI mô phỏng",
    "AI_Type_CleanedWizard of Oz":"Wizard of Oz",
    "Participant_ExpertYes":      "Chuyên gia",
    "AI_Expl_InclYes":            "Có giải thích",
    "Year_c":                     "Năm (tâm 2022)",
}

# Group headers inserted before these terms (for visual separation)
GROUP_HEADERS = {
    "IndustryBusiness":           "Ngành (ref: Y tế)",
    "Task_TypeCreate":            "Nhiệm vụ (ref: Quyết định)",
    "AI_Type_CleanedRule-Based":  "Kiến trúc AI (ref: Deep Learning)",
    "Participant_ExpertYes":      "Trình độ (ref: Không chuyên)",
    "AI_Expl_InclYes":            "Giải thích AI (ref: Không)",
    "Year_c":                     "Xu hướng thời gian",
}

TERM_ORDER = list(TERM_LABELS.keys())

COMPARISON_ORDER = ["Strong Synergy", "Human Augmentation", "AI Augmentation"]
PANEL_TITLES = {
    "Strong Synergy":       "Cộng hưởng mạnh",
    "Human Augmentation":   "AI hỗ trợ người",
    "AI Augmentation":      "Người hỗ trợ AI",
}
PANEL_LETTERS = ["A", "B", "C"]


def _build_plot_data(df_coef, comparison):
    """Return rows for plotting (bottom-to-top order) with group headers."""
    sub = df_coef[df_coef["comparison"] == comparison].copy()
    sub = sub[sub["term"] != "intrcpt"]
    sub = sub.set_index("term").reindex(TERM_ORDER).reset_index()

    labels, estimates, ci_lo, ci_hi, pvals, is_header = [], [], [], [], [], []
    for term in TERM_ORDER:
        # Insert group header if applicable
        if term in GROUP_HEADERS:
            labels.append(GROUP_HEADERS[term])
            estimates.append(np.nan)
            ci_lo.append(np.nan)
            ci_hi.append(np.nan)
            pvals.append(np.nan)
            is_header.append(True)

        row = sub[sub["term"] == term]
        labels.append("   " + TERM_LABELS[term])
        estimates.append(float(row["estimate"].iloc[0]))
        ci_lo.append(float(row["ci_lower"].iloc[0]))
        ci_hi.append(float(row["ci_upper"].iloc[0]))
        pvals.append(float(row["p_value"].iloc[0]))
        is_header.append(False)

    # Reverse for bottom-to-top plotting (matplotlib plots y=0 at bottom)
    return (list(reversed(labels)), list(reversed(estimates)),
            list(reversed(ci_lo)), list(reversed(ci_hi)),
            list(reversed(pvals)), list(reversed(is_header)))


def main():
    df_coef = pd.read_csv(TABLE_DIR / "07_meta_regression.csv")
    df_summ = pd.read_csv(TABLE_DIR / "07_meta_regression_summary.csv")

    n_rows = len(TERM_ORDER) + len(GROUP_HEADERS)  # terms + group headers

    fig = plt.figure(figsize=(18, 10))
    gs = gridspec.GridSpec(1, 3, wspace=0.32, left=0.10, right=0.97,
                           top=0.90, bottom=0.08)

    for idx, comp in enumerate(COMPARISON_ORDER):
        ax = fig.add_subplot(gs[0, idx])
        color = COMPARISON_COLORS[comp]

        labels, est, lo, hi, pv, hdr = _build_plot_data(df_coef, comp)

        y_positions = np.arange(n_rows)

        # Plot each point
        for i in range(n_rows):
            if hdr[i]:
                continue  # skip header rows — no data point
            is_sig = pv[i] < 0.05
            marker_fc = color if is_sig else "white"
            marker_ec = color
            ax.plot(est[i], y_positions[i], "o",
                    markersize=7, markerfacecolor=marker_fc,
                    markeredgecolor=marker_ec, markeredgewidth=1.5,
                    zorder=5)
            ax.plot([lo[i], hi[i]], [y_positions[i], y_positions[i]],
                    color=color, linewidth=1.8, solid_capstyle="round",
                    zorder=4)
            # Annotate significance stars
            stars = sig_stars(pv[i])
            if stars != "ns":
                ax.annotate(stars, (hi[i], y_positions[i]),
                            xytext=(4, 0), textcoords="offset points",
                            fontsize=9, fontweight="bold", color=color,
                            va="center", ha="left")

        # Zero reference line
        add_zero_line(ax, "v")

        # Y-axis labels
        ax.set_yticks(y_positions)
        tick_labels = []
        for i, lab in enumerate(labels):
            tick_labels.append(lab)
        ax.set_yticklabels(tick_labels, fontsize=10)

        # Bold the group headers
        for i, (lab, is_h) in enumerate(zip(labels, hdr)):
            if is_h:
                ax.get_yticklabels()[i].set_fontweight("bold")
                ax.get_yticklabels()[i].set_fontsize(9)
                ax.get_yticklabels()[i].set_color("#444444")

        ax.set_ylim(-0.7, n_rows - 0.3)
        ax.set_xlabel("Hệ số hồi quy (β)", fontsize=11)

        # Panel title
        ax.set_title(PANEL_TITLES[comp], fontsize=13, fontweight="bold",
                     color=color)

        # QM omnibus annotation
        summ = df_summ[df_summ["comparison"] == comp].iloc[0]
        qm_val = summ["QM"]
        qm_p = summ["QM_p"]
        qm_stars = sig_stars(qm_p)
        qm_text = f"QM(11) = {qm_val:.1f}{qm_stars}"
        ax.annotate(qm_text, xy=(0.97, 0.02), xycoords="axes fraction",
                    fontsize=9.5, ha="right", va="bottom",
                    fontfamily="monospace",
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="#f7f7f7",
                              edgecolor="#cccccc", alpha=0.9))

        # Panel label
        add_panel_label(ax, PANEL_LETTERS[idx], x=-0.28, y=1.04)

        # Light horizontal lines for readability
        for i in range(n_rows):
            if not hdr[i]:
                ax.axhline(y_positions[i], color="#EEEEEE", linewidth=0.4,
                           zorder=0)

    fig.suptitle("Hệ số meta-regression đa biến (mô hình 3 bậc REML)",
                 fontsize=15, fontweight="bold", y=0.96)

    # Legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor="#555",
               markeredgecolor="#555", markersize=7, label="Có ý nghĩa (p < .05)"),
        Line2D([0], [0], marker="o", color="w", markerfacecolor="white",
               markeredgecolor="#555", markeredgewidth=1.5, markersize=7,
               label="Không có ý nghĩa"),
    ]
    fig.legend(handles=legend_elements, loc="lower center", ncol=2,
               fontsize=10, frameon=True, edgecolor="#CCCCCC",
               bbox_to_anchor=(0.5, 0.005))

    save_figure(fig, FIGURE_DIR / "Figure5_MetaRegression_Coefficients")
    print("  Figure 5: Meta-regression coefficient plot saved.")


if __name__ == "__main__":
    main()
