"""
Publication bias assessment (shared across Analysis + Experiment):
  - Egger's regression test
  - Begg's rank correlation test
  - Trim-and-fill (via rpy2/metafor when available, else simplified Python)
  - Rosenthal fail-safe N
"""

import numpy as np
from scipy import stats
import statsmodels.api as sm

from .meta_engine import random_effects_dl


# ── Egger's regression test ──────────────────────────────────────────

def eggers_test(effect_sizes, variances):
    """
    Egger's regression: Std_ES = intercept + slope * Precision.

    Returns dict with intercept, intercept_p, slope, slope_p or None.
    """
    es = np.asarray(effect_sizes, dtype=float)
    var = np.asarray(variances, dtype=float)
    mask = np.isfinite(es) & np.isfinite(var) & (var > 0)
    es, var = es[mask], var[mask]

    if len(es) < 3:
        return None

    se = np.sqrt(var)
    precision = 1.0 / se
    std_es = es / se

    X = sm.add_constant(precision)
    model = sm.OLS(std_es, X).fit()

    return {
        "intercept": float(model.params[0]),
        "intercept_se": float(model.bse[0]),
        "intercept_p": float(model.pvalues[0]),
        "slope": float(model.params[1]),
        "slope_p": float(model.pvalues[1]),
    }


# ── Begg's rank correlation ──────────────────────────────────────────

def begg_test(effect_sizes, variances):
    """
    Begg and Mazumdar rank correlation test (Kendall's tau).

    Returns dict with tau and p_value, or None.
    """
    es = np.asarray(effect_sizes, dtype=float)
    var = np.asarray(variances, dtype=float)
    mask = np.isfinite(es) & np.isfinite(var) & (var > 0)
    es, var = es[mask], var[mask]

    if len(es) < 3:
        return None

    se = np.sqrt(var)
    tau, p_value = stats.kendalltau(es, se)
    return {"tau": float(tau), "p_value": float(p_value)}


# ── Trim-and-fill ────────────────────────────────────────────────────

def trim_and_fill(effect_sizes, variances):
    """
    Trim-and-fill analysis.

    Tries rpy2/metafor first; falls back to simplified Python estimator.

    Returns dict with k_original, k_missing, original_estimate, adjusted_estimate.
    """
    es = np.asarray(effect_sizes, dtype=float)
    var = np.asarray(variances, dtype=float)
    mask = np.isfinite(es) & np.isfinite(var) & (var > 0)
    es, var = es[mask], var[mask]

    if len(es) < 5:
        return None

    # Try R implementation first
    try:
        return _trim_and_fill_r(es, var)
    except Exception:
        pass

    return _trim_and_fill_python(es, var)


def _trim_and_fill_r(es, var):
    """Trim-and-fill via metafor::trimfill()."""
    import rpy2.robjects as ro
    from rpy2.robjects import numpy2ri
    numpy2ri.activate()

    ro.globalenv["es_vec"] = es
    ro.globalenv["var_vec"] = var

    r_code = """
    library(metafor)
    fit <- rma(yi = es_vec, vi = var_vec, method = "DL")
    tf  <- trimfill(fit)
    list(
        k_orig    = fit$k,
        k_fill    = tf$k0,
        est_orig  = as.numeric(fit$beta),
        est_adj   = as.numeric(tf$beta)
    )
    """
    r = ro.r(r_code)
    numpy2ri.deactivate()

    return {
        "k_original": int(r.rx2("k_orig")[0]),
        "k_missing": int(r.rx2("k_fill")[0]),
        "original_estimate": float(r.rx2("est_orig")[0]),
        "adjusted_estimate": float(r.rx2("est_adj")[0]),
    }


def _trim_and_fill_python(es, var):
    """Simplified L0 estimator (Python-only fallback)."""
    w = 1.0 / var
    wmean = np.sum(w * es) / np.sum(w)

    n_left = int((es < wmean).sum())
    n_right = int((es >= wmean).sum())
    k_missing = abs(n_left - n_right) // 2

    if k_missing == 0:
        return {
            "k_original": len(es),
            "k_missing": 0,
            "original_estimate": float(wmean),
            "adjusted_estimate": float(wmean),
        }

    # Reflect most-extreme studies
    deviations = es - wmean
    abs_dev = np.abs(deviations)
    sorted_idx = np.argsort(abs_dev)[::-1]

    imputed_es = list(es)
    imputed_var = list(var)
    for i in range(k_missing):
        idx = sorted_idx[i]
        imputed_es.append(2 * wmean - es[idx])
        imputed_var.append(var[idx])

    imp_es = np.array(imputed_es)
    imp_var = np.array(imputed_var)
    w2 = 1.0 / imp_var
    adj_est = float(np.sum(w2 * imp_es) / np.sum(w2))

    return {
        "k_original": len(es),
        "k_missing": k_missing,
        "original_estimate": float(wmean),
        "adjusted_estimate": adj_est,
    }


# ── Fail-safe N (Rosenthal) ─────────────────────────────────────────

def failsafe_n(effect_sizes, variances, alpha=0.05):
    """
    Rosenthal fail-safe N: number of null studies needed to make p > alpha.
    """
    es = np.asarray(effect_sizes, dtype=float)
    var = np.asarray(variances, dtype=float)
    mask = np.isfinite(es) & np.isfinite(var) & (var > 0)
    es, var = es[mask], var[mask]

    if len(es) < 2:
        return None

    se = np.sqrt(var)
    z_values = es / se
    z_crit = stats.norm.ppf(1 - alpha / 2)
    k = len(es)

    z_sum = np.sum(z_values)
    nfs = max(0, int(np.ceil((z_sum / z_crit) ** 2 - k)))

    return {"k": k, "failsafe_n": nfs, "z_sum": float(z_sum)}


# ── Convenience runner ───────────────────────────────────────────────

def run_all_bias_tests(es, var):
    """Run Egger + Begg + trim-and-fill + fail-safe N. Returns dict of dicts."""
    return {
        "egger": eggers_test(es, var),
        "begg": begg_test(es, var),
        "trimfill": trim_and_fill(es, var),
        "failsafe": failsafe_n(es, var),
    }
