"""
07 — Meta-regression: mixed-effects regression with multiple moderators.

Uses rma.mv() via rpy2/metafor with 3-level structure (Paper_ID / Exp_ID).
Falls back to DL-based WLS meta-regression if R is unavailable.

Output: outputs/tables/07_meta_regression.csv
"""

import os
import sys
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
import pandas as pd
from scipy import stats

from experiment_meta.config import TABLE_DIR, REPORT_DIR, ES_COLS, COMPARISON_NAMES

# ── R_HOME setup ────────────────────────────────────────────────────
_CONDA_PREFIX = os.environ.get("CONDA_PREFIX", "")
_R_HOME_CANDIDATES = [
    os.environ.get("R_HOME", ""),
    os.path.join(_CONDA_PREFIX, "lib", "R") if _CONDA_PREFIX else "",
    "/home/duyle/miniconda3/envs/duylv/lib/R",
]
for _rh in _R_HOME_CANDIDATES:
    if _rh and os.path.isdir(_rh):
        os.environ["R_HOME"] = _rh
        break


def _check_r():
    try:
        import rpy2.robjects as ro
        from rpy2.robjects.packages import importr
        importr("metafor")
        return True
    except Exception:
        return False


# ── Moderator definitions ───────────────────────────────────────────
# Reference levels chosen as largest group for stable estimation
CATEGORICAL_MODS = {
    "Industry":           {"ref": "Healthcare"},
    "Task_Type":          {"ref": "Decide"},
    "AI_Type_Cleaned":    {"ref": "Deep"},
    "Participant_Expert": {"ref": "No"},
    "AI_Expl_Incl":       {"ref": "No"},
}
CONTINUOUS_MODS = ["Year"]
YEAR_CENTER = 2022  # center Year for interpretability


# ── R-based meta-regression (primary) ──────────────────────────────

def _run_metareg_r(df, es_col, var_col, comparison_name):
    """Run meta-regression via metafor::rma.mv() with 3-level structure."""
    import rpy2.robjects as ro
    from rpy2.robjects import pandas2ri

    # Prepare data
    model_df = df.copy()
    model_df["Year_c"] = model_df["Year"] - YEAR_CENTER

    cols_needed = [es_col, var_col, "Paper_ID", "Exp_ID_Cleaned",
                   "Year_c"] + list(CATEGORICAL_MODS.keys())
    model_df = model_df[cols_needed].dropna()

    # Ensure categorical columns are strings
    for col in CATEGORICAL_MODS:
        model_df[col] = model_df[col].astype(str)

    with ro.conversion.localconverter(ro.default_converter + pandas2ri.converter):
        r_data = ro.conversion.py2rpy(model_df)
    ro.globalenv["mdf"] = r_data

    # Build relevel commands for reference categories
    relevel_cmds = []
    for col, info in CATEGORICAL_MODS.items():
        relevel_cmds.append(
            f'mdf${col} <- relevel(factor(mdf${col}), ref = "{info["ref"]}")'
        )
    relevel_code = "\n".join(relevel_cmds)

    # Build formula
    mod_terms = list(CATEGORICAL_MODS.keys()) + ["Year_c"]
    formula_rhs = " + ".join(mod_terms)

    r_code = f"""
    library(metafor)
    {relevel_code}

    model <- rma.mv(
        yi = {es_col}, V = {var_col},
        mods = ~ {formula_rhs},
        random = ~ 1 | Paper_ID / Exp_ID_Cleaned,
        data = mdf, method = "REML", test = "t", sparse = TRUE
    )

    # Omnibus moderator test
    QM     <- model$QM
    QMdf1  <- model$QMdf[1]
    QMdf2  <- model$QMdf[2]
    QMp    <- model$QMp

    # Residual heterogeneity
    QE   <- model$QE
    QEdf <- model$QEdf
    QEp  <- model$QEp

    # R² (pseudo) — proportion of heterogeneity explained
    # Compare to intercept-only model
    model0 <- rma.mv(
        yi = {es_col}, V = {var_col},
        random = ~ 1 | Paper_ID / Exp_ID_Cleaned,
        data = mdf, method = "REML", test = "t", sparse = TRUE
    )
    tau2_null <- sum(model0$sigma2)
    tau2_mod  <- sum(model$sigma2)
    R2 <- max(0, (tau2_null - tau2_mod) / tau2_null) * 100

    list(
        coef_names = rownames(model$beta),
        coef       = as.numeric(model$beta),
        se         = as.numeric(model$se),
        ci_lower   = as.numeric(model$ci.lb),
        ci_upper   = as.numeric(model$ci.ub),
        pval       = as.numeric(model$pval),
        zval       = as.numeric(model$zval),
        k          = model$k,
        p          = model$p,
        QM         = as.numeric(QM),
        QMdf1      = as.numeric(QMdf1),
        QMdf2      = as.numeric(QMdf2),
        QMp        = as.numeric(QMp),
        QE         = as.numeric(QE),
        QEdf       = as.numeric(QEdf),
        QEp        = as.numeric(QEp),
        tau2_total = tau2_mod,
        R2         = R2,
        sigma2_1   = model$sigma2[1],
        sigma2_2   = model$sigma2[2]
    )
    """

    result = ro.r(r_code)

    # Extract coefficient names
    coef_names_r = result.rx2("coef_names")
    coef_names = [str(coef_names_r[i]) for i in range(len(coef_names_r))]

    coefs = np.array(result.rx2("coef"))
    ses = np.array(result.rx2("se"))
    ci_lo = np.array(result.rx2("ci_lower"))
    ci_hi = np.array(result.rx2("ci_upper"))
    pvals = np.array(result.rx2("pval"))
    tvals = np.array(result.rx2("zval"))

    rows = []
    for i, name in enumerate(coef_names):
        rows.append({
            "comparison": comparison_name,
            "term": name,
            "estimate": float(coefs[i]),
            "se": float(ses[i]),
            "ci_lower": float(ci_lo[i]),
            "ci_upper": float(ci_hi[i]),
            "t_value": float(tvals[i]),
            "p_value": float(pvals[i]),
        })

    model_info = {
        "comparison": comparison_name,
        "k": int(result.rx2("k")[0]),
        "p_params": int(result.rx2("p")[0]),
        "QM": float(result.rx2("QM")[0]),
        "QM_df1": int(result.rx2("QMdf1")[0]),
        "QM_df2": int(result.rx2("QMdf2")[0]),
        "QM_p": float(result.rx2("QMp")[0]),
        "QE": float(result.rx2("QE")[0]),
        "QE_df": int(result.rx2("QEdf")[0]),
        "QE_p": float(result.rx2("QEp")[0]),
        "tau2_residual": float(result.rx2("tau2_total")[0]),
        "R2_pct": float(result.rx2("R2")[0]),
        "sigma2_between": float(result.rx2("sigma2_1")[0]),
        "sigma2_within": float(result.rx2("sigma2_2")[0]),
        "method": "REML-3level",
    }

    return pd.DataFrame(rows), model_info


# ── Python fallback: DL-based WLS meta-regression ──────────────────

def _run_metareg_python(df, es_col, var_col, comparison_name):
    """Fallback: DL method-of-moments meta-regression using WLS."""
    import statsmodels.api as sm

    model_df = df.copy()
    model_df["Year_c"] = model_df["Year"] - YEAR_CENTER

    # Create design matrix
    dummies_list = []
    for col, info in CATEGORICAL_MODS.items():
        dummies = pd.get_dummies(model_df[col], prefix=col, drop_first=False, dtype=float)
        ref_col = f"{col}_{info['ref']}"
        if ref_col in dummies.columns:
            dummies = dummies.drop(columns=[ref_col])
        dummies_list.append(dummies)
    X_cat = pd.concat(dummies_list, axis=1)
    X = pd.concat([X_cat, model_df[["Year_c"]]], axis=1)
    X = sm.add_constant(X)

    y = model_df[es_col].values
    v = model_df[var_col].values

    # Drop rows with missing data
    mask = np.isfinite(y) & np.isfinite(v) & (v > 0) & X.notna().all(axis=1)
    y, v, X = y[mask], v[mask], X[mask].values
    k = len(y)
    p = X.shape[1]

    # Step 1: Fixed-effects WLS to estimate tau²
    w_fe = 1.0 / v
    W_fe = np.diag(w_fe)
    XtWX = X.T @ W_fe @ X
    XtWy = X.T @ W_fe @ y
    beta_fe = np.linalg.solve(XtWX, XtWy)
    resid_fe = y - X @ beta_fe
    Q_E = float(w_fe @ (resid_fe ** 2))

    # DL estimator for tau²
    C = np.sum(w_fe) - np.trace(W_fe @ X @ np.linalg.solve(XtWX, X.T @ W_fe))
    tau2 = max(0.0, (Q_E - (k - p)) / C)

    # Step 2: Random-effects WLS
    w_re = 1.0 / (v + tau2)
    W_re = np.diag(w_re)
    XtWX_re = X.T @ W_re @ X
    XtWy_re = X.T @ W_re @ y
    beta_re = np.linalg.solve(XtWX_re, XtWy_re)
    cov_beta = np.linalg.inv(XtWX_re)
    se_beta = np.sqrt(np.diag(cov_beta))

    # z-tests for individual coefficients
    z_vals = beta_re / se_beta
    p_vals = 2 * (1 - stats.norm.cdf(np.abs(z_vals)))
    ci_lo = beta_re - 1.96 * se_beta
    ci_hi = beta_re + 1.96 * se_beta

    # Omnibus test QM (Wald test for all moderators, excluding intercept)
    beta_mods = beta_re[1:]
    cov_mods = cov_beta[1:, 1:]
    QM = float(beta_mods @ np.linalg.solve(cov_mods, beta_mods))
    QM_df = p - 1
    QM_p = 1 - stats.chi2.cdf(QM, QM_df)

    # Residual heterogeneity
    resid_re = y - X @ beta_re
    QE_re = float(w_re @ (resid_re ** 2))
    QE_df = k - p
    QE_p = 1 - stats.chi2.cdf(QE_re, QE_df)

    # R² (pseudo): compare to intercept-only tau²
    from jabes_shared.meta_engine import random_effects_dl
    null_model = random_effects_dl(y, v)
    tau2_null = null_model.tau2 if null_model else tau2
    R2 = max(0, (tau2_null - tau2) / tau2_null) * 100 if tau2_null > 0 else 0.0

    # Build column names
    col_names = ["intrcpt"]
    for col_info in CATEGORICAL_MODS.items():
        col = col_info[0]
        ref = col_info[1]["ref"]
        levels = sorted(model_df[col].dropna().unique())
        for lev in levels:
            if str(lev) != str(ref):
                col_names.append(f"{col}{lev}")
    col_names.append("Year_c")

    rows = []
    for i in range(p):
        term_name = col_names[i] if i < len(col_names) else f"X{i}"
        rows.append({
            "comparison": comparison_name,
            "term": term_name,
            "estimate": float(beta_re[i]),
            "se": float(se_beta[i]),
            "ci_lower": float(ci_lo[i]),
            "ci_upper": float(ci_hi[i]),
            "t_value": float(z_vals[i]),
            "p_value": float(p_vals[i]),
        })

    model_info = {
        "comparison": comparison_name,
        "k": k,
        "p_params": p,
        "QM": float(QM),
        "QM_df1": QM_df,
        "QM_df2": 0,
        "QM_p": float(QM_p),
        "QE": float(QE_re),
        "QE_df": QE_df,
        "QE_p": float(QE_p),
        "tau2_residual": float(tau2),
        "R2_pct": float(R2),
        "sigma2_between": np.nan,
        "sigma2_within": np.nan,
        "method": "DL",
    }

    return pd.DataFrame(rows), model_info


# ── Main ────────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("07 — META-REGRESSION")
    print("=" * 70)

    data_path = TABLE_DIR / "01_effect_sizes_full.csv"
    df = pd.read_csv(data_path)
    print(f"\nLoaded: {len(df)} effect sizes")

    use_r = _check_r()
    if use_r:
        print("Using: rpy2/metafor rma.mv() [3-level REML]")
        run_fn = _run_metareg_r
    else:
        print("Using: Python DL-based WLS meta-regression [fallback]")
        run_fn = _run_metareg_python

    all_coefs = []
    all_models = []

    for key, (es_col, var_col) in ES_COLS.items():
        name = COMPARISON_NAMES[key]
        print(f"\n{'─' * 60}")
        print(f"  {name}")
        print(f"{'─' * 60}")

        try:
            coef_df, model_info = run_fn(df, es_col, var_col, name)
            all_coefs.append(coef_df)
            all_models.append(model_info)

            # Print summary
            print(f"  k = {model_info['k']}, params = {model_info['p_params']}")
            print(f"  QM = {model_info['QM']:.2f}, df = {model_info['QM_df1']}, "
                  f"p = {model_info['QM_p']:.4f}")
            print(f"  R² = {model_info['R2_pct']:.1f}%")
            print(f"  τ² (residual) = {model_info['tau2_residual']:.4f}")
            print(f"  QE = {model_info['QE']:.2f}, p = {model_info['QE_p']:.4f}")
            print()
            for _, row in coef_df.iterrows():
                sig = "***" if row["p_value"] < 0.001 else "**" if row["p_value"] < 0.01 else "*" if row["p_value"] < 0.05 else ""
                print(f"  {row['term']:35s}  β = {row['estimate']:+.4f}  "
                      f"SE = {row['se']:.4f}  p = {row['p_value']:.4f} {sig}")

        except Exception as exc:
            warnings.warn(f"Meta-regression failed for {name}: {exc}")
            import traceback
            traceback.print_exc()

    # ── Save coefficients ──
    if all_coefs:
        coef_combined = pd.concat(all_coefs, ignore_index=True)
        out_coef = TABLE_DIR / "07_meta_regression.csv"
        coef_combined.to_csv(out_coef, index=False)
        print(f"\nSaved: {out_coef.name} ({len(coef_combined)} rows)")

    # ── Save model summaries ──
    if all_models:
        model_df = pd.DataFrame(all_models)
        out_model = TABLE_DIR / "07_meta_regression_summary.csv"
        model_df.to_csv(out_model, index=False)
        print(f"Saved: {out_model.name}")

    # ── Insight report ──
    if all_models:
        from jabes_shared.insights import InsightLogger
        log = InsightLogger(REPORT_DIR, "07_meta_regression")

        for info in all_models:
            bullets = [
                f"k = {info['k']}, predictors = {info['p_params'] - 1}",
                f"Omnibus test: QM({info['QM_df1']}) = {info['QM']:.2f}, p = {info['QM_p']:.6f}",
                f"R² = {info['R2_pct']:.1f}% of heterogeneity explained",
                f"Residual τ² = {info['tau2_residual']:.4f}",
                f"Residual QE({info['QE_df']}) = {info['QE']:.1f}, p = {info['QE_p']:.4f}",
            ]
            log.add_section(f"Model: {info['comparison']}", bullets)

        # Significant predictors
        if all_coefs:
            coef_combined = pd.concat(all_coefs, ignore_index=True)
            sig_df = coef_combined[
                (coef_combined["p_value"] < 0.05) & (coef_combined["term"] != "intrcpt")
            ]
            if len(sig_df) > 0:
                sig_bullets = []
                for _, r in sig_df.iterrows():
                    sig_bullets.append(
                        f"{r['comparison']} / {r['term']}: β = {r['estimate']:+.3f}, "
                        f"p = {r['p_value']:.4f}"
                    )
                log.add_section("Significant Predictors (p < .05)", sig_bullets)

        log.write("07 — Meta-Regression Insights")

    print("\n" + "=" * 70)
    print("07 — META-REGRESSION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
