"""
Effect Size Computation — Single canonical implementation (shared).

Computes Hedges' g (bias-corrected SMD) for three comparisons:
  1. Strong Synergy:      HAI vs max(Human, AI)
  2. Human Augmentation:  HAI vs Human
  3. AI Augmentation:     HAI vs AI
"""

import numpy as np
import pandas as pd


def compute_hedges_g(m1, m2, sd1, sd2, n1, n2):
    """
    Compute Hedges' g with small-sample bias correction.

    Returns
    -------
    g, var_g, se_g, ci_lower, ci_upper
    """
    if any(pd.isna([m1, m2, sd1, sd2, n1, n2])):
        return np.nan, np.nan, np.nan, np.nan, np.nan
    if n1 <= 0 or n2 <= 0 or sd1 < 0 or sd2 < 0:
        return np.nan, np.nan, np.nan, np.nan, np.nan

    sd_pooled = np.sqrt(((n1 - 1) * sd1**2 + (n2 - 1) * sd2**2) / (n1 + n2 - 2))

    if sd_pooled == 0:
        if m1 == m2:
            return 0.0, 0.0, 0.0, 0.0, 0.0
        return np.nan, np.nan, np.nan, np.nan, np.nan

    d = (m1 - m2) / sd_pooled
    df = n1 + n2 - 2
    j = 1 - (3 / (4 * df - 1))
    g = j * d

    var_g = ((n1 + n2) / (n1 * n2) + (g**2) / (2 * (n1 + n2))) * (j**2)
    se_g = np.sqrt(var_g)
    ci_lower = g - 1.96 * se_g
    ci_upper = g + 1.96 * se_g

    return g, var_g, se_g, ci_lower, ci_upper


def compute_all_effect_sizes(df):
    """
    Add effect-size columns to *df* (in-place copy returned).

    Columns added per comparison (x = s, h, a):
        es_x, var_es_x, se_es_x, ci_lower_x, ci_upper_x
    """
    df = df.copy()

    # --- Strong Synergy: HAI vs max(Human, AI) ---
    df["_max_perf"] = df[["Avg_Perf_Human_Adj", "Avg_Perf_AI_Adj"]].max(axis=1)
    df["_max_sd"] = np.where(
        df["Avg_Perf_AI_Adj"] >= df["Avg_Perf_Human_Adj"],
        df["Sd_Perf_AI"], df["Sd_Perf_Human"],
    )
    df["_max_n"] = np.where(
        df["Avg_Perf_AI_Adj"] >= df["Avg_Perf_Human_Adj"],
        df.get("N_Exp", df["N_Human"]), df["N_Human"],
    )

    _apply_es(df, "Avg_Perf_HumanAI_Adj", "_max_perf",
              "Sd_Perf_HumanAI", "_max_sd", "N_HumanAI", "_max_n", "s")

    # --- Human Augmentation: HAI vs Human ---
    _apply_es(df, "Avg_Perf_HumanAI_Adj", "Avg_Perf_Human_Adj",
              "Sd_Perf_HumanAI", "Sd_Perf_Human", "N_HumanAI", "N_Human", "h")

    # --- AI Augmentation: HAI vs AI ---
    n2_col = "N_Exp" if "N_Exp" in df.columns else "N_Human"
    _apply_es(df, "Avg_Perf_HumanAI_Adj", "Avg_Perf_AI_Adj",
              "Sd_Perf_HumanAI", "Sd_Perf_AI", "N_HumanAI", n2_col, "a")

    # Cleanup helper columns
    df.drop(columns=[c for c in df.columns if c.startswith("_max_") or c.startswith("_min_")],
            errors="ignore", inplace=True)

    return df


def _apply_es(df, m1_col, m2_col, sd1_col, sd2_col, n1_col, n2_col, suffix):
    """Vectorised helper — row-by-row ES via apply."""
    results = df.apply(
        lambda row: compute_hedges_g(
            row[m1_col], row[m2_col],
            row[sd1_col], row[sd2_col],
            row[n1_col], row[n2_col],
        ),
        axis=1,
    )
    df[f"es_{suffix}"] = [r[0] for r in results]
    df[f"var_es_{suffix}"] = [r[1] for r in results]
    df[f"se_es_{suffix}"] = [r[2] for r in results]
    df[f"ci_lower_{suffix}"] = [r[3] for r in results]
    df[f"ci_upper_{suffix}"] = [r[4] for r in results]


def flag_edge_cases(df):
    """Add boolean flag columns for SD=0, |g|>3, CI width>2."""
    df = df.copy()

    df["flag_sd_zero"] = (
        (df["Sd_Perf_AI"] == 0)
        | (df["Sd_Perf_Human"] == 0)
        | (df["Sd_Perf_HumanAI"] == 0)
    )

    df["flag_extreme_es"] = False
    for s in ("s", "h", "a"):
        col = f"es_{s}"
        if col in df.columns:
            df["flag_extreme_es"] = df["flag_extreme_es"] | (df[col].abs() > 3)

    df["flag_wide_ci"] = False
    for s in ("s", "h", "a"):
        lo, hi = f"ci_lower_{s}", f"ci_upper_{s}"
        if lo in df.columns and hi in df.columns:
            df["flag_wide_ci"] = df["flag_wide_ci"] | ((df[hi] - df[lo]) > 2)

    return df
