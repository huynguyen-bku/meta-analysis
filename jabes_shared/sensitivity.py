"""
Sensitivity analyses (shared across Analysis + Experiment):
  - Leave-one-out
  - Cumulative meta-analysis
  - Influence diagnostics
  - Outlier exclusion
"""

import numpy as np
import pandas as pd

from .meta_engine import random_effects_dl


def leave_one_out(effect_sizes, variances, study_labels=None):
    """
    Drop each study in turn and re-run DL meta.

    Returns DataFrame with columns:
        excluded, k, estimate, se, ci_lower, ci_upper, p_value, I2
    """
    es = np.asarray(effect_sizes, dtype=float)
    var = np.asarray(variances, dtype=float)
    mask = np.isfinite(es) & np.isfinite(var) & (var > 0)
    es, var = es[mask], var[mask]
    k = len(es)

    if study_labels is not None:
        labels = np.asarray(study_labels)[mask]
    else:
        labels = np.arange(k)

    rows = []
    for i in range(k):
        es_i = np.delete(es, i)
        var_i = np.delete(var, i)
        r = random_effects_dl(es_i, var_i)
        if r is not None:
            rows.append({
                "excluded": labels[i],
                "k": r.k,
                "estimate": r.estimate,
                "se": r.se,
                "ci_lower": r.ci_lower,
                "ci_upper": r.ci_upper,
                "p_value": r.p_value,
                "I2": r.I2,
            })

    return pd.DataFrame(rows)


def cumulative_meta(effect_sizes, variances, study_labels=None, sort_by=None):
    """
    Cumulative meta-analysis: add studies one-by-one (optionally sorted).

    Returns DataFrame with cumulative pooled estimates.
    """
    es = np.asarray(effect_sizes, dtype=float)
    var = np.asarray(variances, dtype=float)
    mask = np.isfinite(es) & np.isfinite(var) & (var > 0)
    es, var = es[mask], var[mask]

    if sort_by is not None:
        sort_by = np.asarray(sort_by)[mask]
        order = np.argsort(sort_by)
    else:
        order = np.arange(len(es))

    es, var = es[order], var[order]
    if study_labels is not None:
        labels = np.asarray(study_labels)[mask][order]
    else:
        labels = np.arange(len(es))

    rows = []
    for i in range(1, len(es) + 1):
        r = random_effects_dl(es[:i], var[:i])
        if r is not None:
            rows.append({
                "step": i,
                "last_added": labels[i - 1],
                "k": r.k,
                "estimate": r.estimate,
                "se": r.se,
                "ci_lower": r.ci_lower,
                "ci_upper": r.ci_upper,
                "p_value": r.p_value,
                "I2": r.I2,
            })

    return pd.DataFrame(rows)


def influence_diagnostics(effect_sizes, variances, study_labels=None):
    """
    Compute influence diagnostics: hat values, Cook-like distance,
    and studentized residuals.

    Returns DataFrame with per-study diagnostics.
    """
    es = np.asarray(effect_sizes, dtype=float)
    var = np.asarray(variances, dtype=float)
    mask = np.isfinite(es) & np.isfinite(var) & (var > 0)
    es, var = es[mask], var[mask]
    k = len(es)

    if study_labels is not None:
        labels = np.asarray(study_labels)[mask]
    else:
        labels = np.arange(k)

    # Full model
    full = random_effects_dl(es, var)
    if full is None:
        return pd.DataFrame()

    tau2 = full.tau2
    w = 1.0 / (var + tau2)
    W_sum = np.sum(w)

    # Hat values
    h = w / W_sum

    # Studentized residuals
    residuals = es - full.estimate
    rstd = residuals / np.sqrt(var + tau2)

    # Cook-like distance via leave-one-out
    loo = leave_one_out(es, var, labels)
    cook_d = np.full(k, np.nan)
    if len(loo) == k:
        for i in range(k):
            diff = full.estimate - loo.iloc[i]["estimate"]
            cook_d[i] = diff**2 / (full.se**2)

    return pd.DataFrame({
        "study": labels,
        "es": es,
        "hat": h,
        "rstudent": rstd,
        "cook_d": cook_d,
    })


def outlier_exclusion(effect_sizes, variances, threshold=3.0, study_labels=None):
    """
    Exclude studies with |rstudent| > threshold and re-run meta.

    Returns (MetaResult_after, excluded_labels).
    """
    diag = influence_diagnostics(effect_sizes, variances, study_labels)
    if len(diag) == 0:
        return None, []

    outlier_mask = diag["rstudent"].abs() > threshold
    excluded = diag.loc[outlier_mask, "study"].tolist()

    if len(excluded) == 0:
        full = random_effects_dl(
            np.asarray(effect_sizes, dtype=float),
            np.asarray(variances, dtype=float),
        )
        return full, []

    keep = ~outlier_mask
    es_keep = diag.loc[keep, "es"].values
    # Reconstruct variances for kept studies
    es_all = np.asarray(effect_sizes, dtype=float)
    var_all = np.asarray(variances, dtype=float)
    mask_fin = np.isfinite(es_all) & np.isfinite(var_all) & (var_all > 0)
    var_keep = var_all[mask_fin][keep.values]

    result = random_effects_dl(es_keep, var_keep)
    return result, excluded
