"""
Meta-analytic engines (shared across Analysis + Experiment pipelines):
  - DerSimonian-Laird random-effects (Python, 2-level)
  - 3-level REML via rpy2/metafor (gold standard)
"""

import numpy as np
from scipy import stats
from dataclasses import dataclass
import warnings


@dataclass
class MetaResult:
    """Uniform container for meta-analysis results."""
    comparison: str = ""
    k: int = 0
    estimate: float = np.nan
    se: float = np.nan
    ci_lower: float = np.nan
    ci_upper: float = np.nan
    p_value: float = np.nan
    tau2: float = np.nan
    I2: float = np.nan
    Q: float = np.nan
    Q_df: int = 0
    Q_pval: float = np.nan
    pred_lower: float = np.nan
    pred_upper: float = np.nan
    # 3-level extras
    sigma2_within: float = np.nan
    sigma2_between: float = np.nan
    I2_between: float = np.nan
    I2_within: float = np.nan
    method: str = "DL"


def random_effects_dl(effect_sizes, variances):
    """
    DerSimonian-Laird random-effects meta-analysis.

    Parameters
    ----------
    effect_sizes, variances : array-like
        Must be same length; NaN/non-positive variances are dropped.

    Returns
    -------
    MetaResult or None if k < 2.
    """
    es = np.asarray(effect_sizes, dtype=float)
    var = np.asarray(variances, dtype=float)
    mask = np.isfinite(es) & np.isfinite(var) & (var > 0)
    es, var = es[mask], var[mask]
    k = len(es)

    if k < 2:
        return None

    w = 1.0 / var
    fe_est = np.sum(w * es) / np.sum(w)

    Q = float(np.sum(w * (es - fe_est) ** 2))
    df = k - 1
    Q_pval = 1 - stats.chi2.cdf(Q, df)

    C = np.sum(w) - np.sum(w**2) / np.sum(w)
    tau2 = max(0.0, (Q - df) / C)

    w_re = 1.0 / (var + tau2)
    estimate = float(np.sum(w_re * es) / np.sum(w_re))
    se = float(np.sqrt(1.0 / np.sum(w_re)))

    ci_lower = estimate - 1.96 * se
    ci_upper = estimate + 1.96 * se

    z = estimate / se
    p_value = float(2 * (1 - stats.norm.cdf(abs(z))))

    I2 = max(0.0, 100 * (Q - df) / Q) if Q > df else 0.0

    # Prediction interval
    pred_se = np.sqrt(tau2 + se**2)
    pred_lower = estimate - 1.96 * pred_se
    pred_upper = estimate + 1.96 * pred_se

    return MetaResult(
        k=k, estimate=estimate, se=se,
        ci_lower=ci_lower, ci_upper=ci_upper,
        p_value=p_value, tau2=tau2, I2=I2,
        Q=Q, Q_df=df, Q_pval=Q_pval,
        pred_lower=pred_lower, pred_upper=pred_upper,
        method="DL",
    )


# ── 3-level REML via rpy2 ────────────────────────────────────────────

_R_AVAILABLE = None  # lazy check


def _check_r():
    global _R_AVAILABLE
    if _R_AVAILABLE is not None:
        return _R_AVAILABLE
    try:
        import rpy2.robjects as ro
        from rpy2.robjects.packages import importr
        importr("metafor")
        _R_AVAILABLE = True
    except Exception:
        _R_AVAILABLE = False
    return _R_AVAILABLE


def fit_threelevel_reml(df, es_col, var_col, comparison_name=""):
    """
    Fit 3-level random-effects model: rma.mv(yi, V, ~ 1 | Paper_ID / Exp_ID_Cleaned).

    Returns MetaResult or None.
    """
    if not _check_r():
        warnings.warn("rpy2/metafor not available — falling back to DL 2-level")
        return random_effects_dl(df[es_col].values, df[var_col].values)

    import rpy2.robjects as ro
    from rpy2.robjects import pandas2ri

    model_data = df[[es_col, var_col, "Paper_ID", "Exp_ID_Cleaned", "ES_ID"]].dropna()
    if len(model_data) < 5:
        return None

    with ro.conversion.localconverter(ro.default_converter + pandas2ri.converter):
        r_data = ro.conversion.py2rpy(model_data)

    ro.globalenv["model_data"] = r_data

    r_code = f"""
    library(metafor)
    model <- rma.mv(
        yi = {es_col}, V = {var_col},
        random = ~ 1 | Paper_ID / Exp_ID_Cleaned,
        data = model_data, method = "REML", test = "t", sparse = TRUE
    )

    sigma2_w <- model$sigma2[2]
    sigma2_b <- model$sigma2[1]

    W <- diag(1/model_data${var_col})
    X <- model.matrix(model)
    P <- W - W %*% X %*% solve(t(X) %*% W %*% X) %*% t(X) %*% W
    denom <- sum(model$sigma2) + (model$k - model$p) / sum(diag(P))
    I2_total   <- sum(model$sigma2) / denom * 100
    I2_between <- sigma2_b / denom * 100
    I2_within  <- sigma2_w / denom * 100

    pred_se <- sqrt(sum(model$sigma2) + as.numeric(model$se)^2)
    t_crit  <- qt(0.975, df = as.numeric(model$dfs))
    pred_lo <- as.numeric(model$beta) - t_crit * pred_se
    pred_hi <- as.numeric(model$beta) + t_crit * pred_se

    list(
        estimate   = as.numeric(model$beta),
        se         = as.numeric(model$se),
        ci_lower   = as.numeric(model$ci.lb),
        ci_upper   = as.numeric(model$ci.ub),
        p_value    = as.numeric(model$pval),
        k          = model$k,
        sigma2_w   = sigma2_w,
        sigma2_b   = sigma2_b,
        I2_total   = I2_total,
        I2_between = I2_between,
        I2_within  = I2_within,
        Q          = as.numeric(model$QE),
        Q_df       = as.numeric(model$QEdf),
        Q_pval     = as.numeric(model$QEp),
        pred_lo    = pred_lo,
        pred_hi    = pred_hi
    )
    """

    try:
        r = ro.r(r_code)
        return MetaResult(
            comparison=comparison_name,
            k=int(r.rx2("k")[0]),
            estimate=float(r.rx2("estimate")[0]),
            se=float(r.rx2("se")[0]),
            ci_lower=float(r.rx2("ci_lower")[0]),
            ci_upper=float(r.rx2("ci_upper")[0]),
            p_value=float(r.rx2("p_value")[0]),
            tau2=float(r.rx2("sigma2_w")[0]) + float(r.rx2("sigma2_b")[0]),
            I2=float(r.rx2("I2_total")[0]),
            Q=float(r.rx2("Q")[0]),
            Q_df=int(r.rx2("Q_df")[0]),
            Q_pval=float(r.rx2("Q_pval")[0]),
            pred_lower=float(r.rx2("pred_lo")[0]),
            pred_upper=float(r.rx2("pred_hi")[0]),
            sigma2_within=float(r.rx2("sigma2_w")[0]),
            sigma2_between=float(r.rx2("sigma2_b")[0]),
            I2_between=float(r.rx2("I2_between")[0]),
            I2_within=float(r.rx2("I2_within")[0]),
            method="REML-3level",
        )
    except Exception as exc:
        warnings.warn(f"3-level model failed ({exc}); falling back to DL")
        res = random_effects_dl(model_data[es_col].values, model_data[var_col].values)
        if res:
            res.comparison = comparison_name
        return res
