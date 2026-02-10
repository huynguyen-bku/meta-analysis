"""
Subgroup analysis + Q-between test for moderator variables (shared).
"""

import numpy as np
import pandas as pd
from scipy import stats

from .meta_engine import random_effects_dl, MetaResult


def subgroup_analysis(df, moderator, es_col, var_col):
    """
    Run DL random-effects meta within each level of *moderator*.

    Returns list of dicts with keys:
        moderator, level, k, estimate, se, ci_lower, ci_upper,
        p_value, I2, Q, Q_pval, Q_between, Q_between_df, Q_between_pval
    """
    data = df[[moderator, es_col, var_col]].dropna()
    if len(data) < 3:
        return []

    levels = sorted(data[moderator].unique())
    if len(levels) < 2:
        return []

    results = []
    for level in levels:
        sub = data[data[moderator] == level]
        r = random_effects_dl(sub[es_col].values, sub[var_col].values)
        if r is not None:
            results.append({
                "moderator": moderator,
                "level": str(level),
                "k": r.k,
                "estimate": r.estimate,
                "se": r.se,
                "ci_lower": r.ci_lower,
                "ci_upper": r.ci_upper,
                "p_value": r.p_value,
                "I2": r.I2,
                "tau2": r.tau2,
                "Q": r.Q,
                "Q_pval": r.Q_pval,
            })

    if len(results) < 2:
        return results

    # ── Q-between test ──
    overall = random_effects_dl(data[es_col].values, data[var_col].values)
    Q_within = sum(r["Q"] for r in results)
    Q_total = overall.Q if overall else Q_within
    Q_between = max(0.0, Q_total - Q_within)
    df_between = len(results) - 1
    Q_between_pval = 1 - stats.chi2.cdf(Q_between, df_between) if df_between > 0 else 1.0

    for r in results:
        r["Q_between"] = Q_between
        r["Q_between_df"] = df_between
        r["Q_between_pval"] = Q_between_pval

    return results


def run_all_moderators(df, moderators, es_col, var_col, comparison_name=""):
    """Run subgroup analysis for every moderator; return combined DataFrame."""
    all_rows = []
    for mod in moderators:
        if mod not in df.columns:
            continue
        rows = subgroup_analysis(df, mod, es_col, var_col)
        for r in rows:
            r["comparison"] = comparison_name
        all_rows.extend(rows)
    return pd.DataFrame(all_rows)
