"""
Meta-Analysis: Human-AI Collaboration (Python)
So sánh Hiệu suất: Human-AI vs Human Alone vs AI Alone

Mục tiêu nghiên cứu:
1. So sánh hiệu suất hệ thống Human-AI với con người làm việc độc lập
2. So sánh hiệu suất hệ thống Human-AI với AI làm việc độc lập
3. Đánh giá synergy (cộng hưởng) giữa Human-AI so với max(Human, AI)
4. Phân tích các yếu tố điều tiết (moderators)

Author: [Your Name]
Date: 2026
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

warnings.filterwarnings('ignore')

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
plt.style.use('seaborn-v0_8-whitegrid')

# Create output directories
os.makedirs('Figures', exist_ok=True)
os.makedirs('Data', exist_ok=True)


# ============================================================================
# SECTION 1: UTILITY FUNCTIONS
# ============================================================================

def compute_hedges_g(m1, m2, sd1, sd2, n1, n2):
    """
    Tính Hedges' g (Standardized Mean Difference với hiệu chỉnh mẫu nhỏ)

    Parameters:
    -----------
    m1, m2: mean của nhóm 1 và nhóm 2
    sd1, sd2: standard deviation của nhóm 1 và nhóm 2
    n1, n2: sample size của nhóm 1 và nhóm 2

    Returns:
    --------
    g: Hedges' g effect size
    var_g: variance của Hedges' g
    """
    # Pooled standard deviation
    sd_pooled = np.sqrt(((n1 - 1) * sd1**2 + (n2 - 1) * sd2**2) / (n1 + n2 - 2))

    # Cohen's d
    d = (m1 - m2) / sd_pooled

    # Correction factor for small sample bias (Hedges' g)
    df = n1 + n2 - 2
    j = 1 - (3 / (4 * df - 1))

    # Hedges' g
    g = j * d

    # Variance of Hedges' g (large sample approximation)
    var_g = (n1 + n2) / (n1 * n2) + (g**2) / (2 * (n1 + n2))
    var_g = var_g * (j**2)

    return g, var_g


def compute_all_effect_sizes(df):
    """
    Tính tất cả effect sizes cho dataframe
    """
    n = len(df)
    es_s, var_s = np.zeros(n), np.zeros(n)  # Strong synergy
    es_h, var_h = np.zeros(n), np.zeros(n)  # Human augmentation
    es_a, var_a = np.zeros(n), np.zeros(n)  # AI augmentation
    es_n, var_n = np.zeros(n), np.zeros(n)  # Negative synergy

    for i in range(n):
        row = df.iloc[i]

        # Get values
        m_hai = row['Avg_Perf_HumanAI_Adj']
        m_h = row['Avg_Perf_Human_Adj']
        m_ai = row['Avg_Perf_AI_Adj']
        m_base = row['Avg_Perf_Baseline_Adj']
        m_worse = row['Avg_Perf_Worse_Adj']

        sd_hai = row['Sd_Perf_HumanAI']
        sd_h = row['Sd_Perf_Human']
        sd_ai = row['Sd_Perf_AI']
        sd_base = row['Sd_Perf_Baseline']
        sd_worse = row['Sd_Perf_Worse']

        n_hai = row['N_HumanAI']
        n_h = row['N_Human']

        try:
            # Strong synergy: HAI vs max(H, AI)
            if pd.notna(m_hai) and pd.notna(m_base) and sd_hai > 0 and sd_base > 0:
                es_s[i], var_s[i] = compute_hedges_g(m_hai, m_base, sd_hai, sd_base, n_hai, n_h)
            else:
                es_s[i], var_s[i] = np.nan, np.nan

            # Human augmentation: HAI vs H
            if pd.notna(m_hai) and pd.notna(m_h) and sd_hai > 0 and sd_h > 0:
                es_h[i], var_h[i] = compute_hedges_g(m_hai, m_h, sd_hai, sd_h, n_hai, n_hai)
            else:
                es_h[i], var_h[i] = np.nan, np.nan

            # AI augmentation: HAI vs AI
            if pd.notna(m_hai) and pd.notna(m_ai) and sd_hai > 0 and sd_ai > 0:
                es_a[i], var_a[i] = compute_hedges_g(m_hai, m_ai, sd_hai, sd_ai, n_hai, n_h)
            else:
                es_a[i], var_a[i] = np.nan, np.nan

            # Negative synergy: HAI vs min(H, AI)
            if pd.notna(m_hai) and pd.notna(m_worse) and sd_hai > 0 and sd_worse > 0:
                es_n[i], var_n[i] = compute_hedges_g(m_hai, m_worse, sd_hai, sd_worse, n_hai, n_h)
            else:
                es_n[i], var_n[i] = np.nan, np.nan

        except Exception:
            es_s[i], var_s[i] = np.nan, np.nan
            es_h[i], var_h[i] = np.nan, np.nan
            es_a[i], var_a[i] = np.nan, np.nan
            es_n[i], var_n[i] = np.nan, np.nan

    return es_s, var_s, es_h, var_h, es_a, var_a, es_n, var_n


def random_effects_meta(effect_sizes, variances, method='DL'):
    """
    Thực hiện random-effects meta-analysis

    Parameters:
    -----------
    effect_sizes: array of effect sizes
    variances: array of sampling variances
    method: 'REML' hoặc 'DL' (DerSimonian-Laird)

    Returns:
    --------
    dict với các kết quả
    """
    # Remove NaN
    mask = ~np.isnan(effect_sizes) & ~np.isnan(variances) & (variances > 0)
    es = effect_sizes[mask]
    var = variances[mask]
    k = len(es)

    if k < 2:
        return None

    # Fixed-effect weights
    w = 1 / var

    # Fixed-effect estimate
    fe_estimate = np.sum(w * es) / np.sum(w)

    # Q statistic
    Q = np.sum(w * (es - fe_estimate)**2)
    df = k - 1
    Q_pval = 1 - stats.chi2.cdf(Q, df)

    # Estimate tau^2 (between-study variance) - DerSimonian-Laird
    C = np.sum(w) - np.sum(w**2) / np.sum(w)
    tau2 = max(0, (Q - df) / C)

    # Random-effects weights
    w_re = 1 / (var + tau2)

    # Random-effects estimate
    re_estimate = np.sum(w_re * es) / np.sum(w_re)

    # Standard error
    se = np.sqrt(1 / np.sum(w_re))

    # 95% CI
    ci_lower = re_estimate - 1.96 * se
    ci_upper = re_estimate + 1.96 * se

    # Z-test
    z = re_estimate / se
    p_value = 2 * (1 - norm.cdf(abs(z)))

    # I^2 statistic
    if Q > df:
        I2 = 100 * (Q - df) / Q
    else:
        I2 = 0

    # H^2
    H2 = Q / df if df > 0 else 1

    return {
        'k': k,
        'estimate': re_estimate,
        'se': se,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'z': z,
        'p_value': p_value,
        'tau2': tau2,
        'tau': np.sqrt(tau2),
        'Q': Q,
        'Q_df': df,
        'Q_pval': Q_pval,
        'I2': I2,
        'H2': H2
    }


def print_meta_results(results, name):
    """In kết quả meta-analysis"""
    if results is None:
        print(f"\n{name}: Không đủ dữ liệu")
        return

    print(f"\n{'='*60}")
    print(f"{name}")
    print(f"{'='*60}")
    print(f"Number of effect sizes (k): {results['k']}")
    print(f"\nPooled Effect Size (Hedges' g):")
    print(f"  Estimate: {results['estimate']:.4f}")
    print(f"  SE: {results['se']:.4f}")
    print(f"  95% CI: [{results['ci_lower']:.4f}, {results['ci_upper']:.4f}]")
    print(f"  z = {results['z']:.4f}, p = {results['p_value']:.4f}")
    print(f"\nHeterogeneity:")
    print(f"  tau² = {results['tau2']:.4f}")
    print(f"  tau = {results['tau']:.4f}")
    print(f"  Q({results['Q_df']}) = {results['Q']:.2f}, p = {results['Q_pval']:.4f}")
    print(f"  I² = {results['I2']:.1f}%")
    print(f"  H² = {results['H2']:.2f}")


def eggers_test(effect_sizes, variances):
    """
    Egger's regression test for funnel plot asymmetry
    """
    mask = ~np.isnan(effect_sizes) & ~np.isnan(variances) & (variances > 0)
    es = effect_sizes[mask]
    se = np.sqrt(variances[mask])

    precision = 1 / se
    std_es = es / se

    X = sm.add_constant(precision)
    model = sm.OLS(std_es, X).fit()

    return {
        'intercept': model.params[0],
        'intercept_se': model.bse[0],
        'intercept_t': model.tvalues[0],
        'intercept_p': model.pvalues[0],
        'slope': model.params[1],
        'slope_p': model.pvalues[1]
    }


def rank_correlation_test(effect_sizes, variances):
    """
    Begg and Mazumdar rank correlation test
    """
    mask = ~np.isnan(effect_sizes) & ~np.isnan(variances) & (variances > 0)
    es = effect_sizes[mask]
    se = np.sqrt(variances[mask])

    tau, p_value = stats.kendalltau(es, se)

    return {'tau': tau, 'p_value': p_value}


def subgroup_analysis(df, es_col, var_col, moderator):
    """
    Thực hiện subgroup analysis cho một moderator
    """
    results = []

    for group in df[moderator].dropna().unique():
        mask = df[moderator] == group
        es = df.loc[mask, es_col].values
        var = df.loc[mask, var_col].values

        meta_result = random_effects_meta(es, var)

        if meta_result:
            results.append({
                'Moderator': moderator,
                'Group': group,
                'k': meta_result['k'],
                'g': meta_result['estimate'],
                'CI_lower': meta_result['ci_lower'],
                'CI_upper': meta_result['ci_upper'],
                'p_value': meta_result['p_value'],
                'I2': meta_result['I2']
            })

    return pd.DataFrame(results)


def print_distribution(df, column, title):
    """In phân bố của một biến"""
    print(f"\n{title}")
    print("-" * 40)
    counts = df[column].value_counts()
    percentages = df[column].value_counts(normalize=True) * 100
    for val in counts.index:
        print(f"{val}: {counts[val]} ({percentages[val]:.1f}%)")


# ============================================================================
# SECTION 2: VISUALIZATION FUNCTIONS
# ============================================================================

def create_forest_plot(effect_sizes, variances, title, filename, pooled_result):
    """
    Tạo forest plot
    """
    mask = ~np.isnan(effect_sizes) & ~np.isnan(variances)
    es = effect_sizes[mask]
    var = variances[mask]
    se = np.sqrt(var)

    sort_idx = np.argsort(es)
    es = es[sort_idx]
    se = se[sort_idx]

    k = len(es)

    fig, ax = plt.subplots(figsize=(11.5, max(8, k * 0.18)))

    y_pos = np.arange(k)
    colors = ['darkgreen' if e > 0 else 'darkred' for e in es]

    for i in range(k):
        ci_lower = es[i] - 1.96 * se[i]
        ci_upper = es[i] + 1.96 * se[i]
        ax.hlines(y_pos[i], ci_lower, ci_upper, colors=colors[i], alpha=0.5, linewidth=1)
        ax.scatter(es[i], y_pos[i], c=colors[i], s=20, zorder=3)

    if pooled_result:
        ax.axvline(pooled_result['estimate'], color='blue', linestyle='--', linewidth=2, label='Pooled estimate')
        ax.axvspan(pooled_result['ci_lower'], pooled_result['ci_upper'], alpha=0.1, color='blue')

    ax.axvline(0, color='black', linestyle='-', linewidth=1)
    ax.axvspan(-6, 0, alpha=0.05, color='red')
    ax.axvspan(0, 6, alpha=0.05, color='green')

    ax.set_xlabel("Effect Size (Hedges' g)", fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold', pad=10)
    ax.set_xlim(-4, 4)
    ax.set_yticks([])

    n_pos = np.sum(es > 0)
    n_neg = np.sum(es <= 0)

    ax.text(0.02, 0.98, f"Negative effects: {n_neg} ({n_neg/k*100:.1f}%)",
            transform=ax.transAxes, fontsize=10, verticalalignment='top', color='darkred')
    ax.text(0.98, 0.98, f"Positive effects: {n_pos} ({n_pos/k*100:.1f}%)",
            transform=ax.transAxes, fontsize=10, verticalalignment='top',
            horizontalalignment='right', color='darkgreen')

    if pooled_result:
        pooled_text = (
            f"Pooled: g = {pooled_result['estimate']:.3f} "
            f"[{pooled_result['ci_lower']:.3f}, {pooled_result['ci_upper']:.3f}]"
        )
        ax.text(
            0.5, -0.10, pooled_text, transform=ax.transAxes, fontsize=10.5,
            horizontalalignment='center', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        )
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.18), frameon=True, ncol=1)

    plt.tight_layout(rect=[0, 0.06, 1, 1])
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Forest plot saved: {filename}")


def create_funnel_plot(effect_sizes, variances, title, filename, pooled_estimate):
    """
    Tạo funnel plot để kiểm tra publication bias
    """
    mask = ~np.isnan(effect_sizes) & ~np.isnan(variances) & (variances > 0)
    es = effect_sizes[mask]
    se = np.sqrt(variances[mask])

    fig, ax = plt.subplots(figsize=(11, 8.5))

    ax.scatter(es, se, c='#0072B2', alpha=0.6, s=35, label=f"Studies (k={len(es)})")
    ax.axvline(pooled_estimate, color='red', linestyle='--', linewidth=2,
               label=f'Pooled estimate = {pooled_estimate:.3f}')

    se_range = np.linspace(0.001, max(se) * 1.1, 100)
    ci_lower = pooled_estimate - 1.96 * se_range
    ci_upper = pooled_estimate + 1.96 * se_range

    ax.fill_betweenx(se_range, ci_lower, ci_upper, alpha=0.1, color='gray')
    ax.plot(ci_lower, se_range, 'k--', alpha=0.5, linewidth=1)
    ax.plot(ci_upper, se_range, 'k--', alpha=0.5, linewidth=1)

    ax.invert_yaxis()

    ax.set_xlabel("Effect Size (Hedges' g)", fontsize=12)
    ax.set_ylabel("Standard Error", fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold', pad=10)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=2, frameon=True)

    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Funnel plot saved: {filename}")


# ============================================================================
# SECTION 3: MAIN ANALYSIS
# ============================================================================

def main():
    """Main function to run the meta-analysis"""

    print("=" * 70)
    print("META-ANALYSIS: HUMAN-AI COLLABORATION")
    print("=" * 70)

    # -------------------------------------------------------------------------
    # 1. Load Data
    # -------------------------------------------------------------------------
    print("\n[1] Loading data...")
    df = pd.read_excel("Data_Extraction_communication_public.xlsx")

    print(f"\n{'='*50}")
    print("TỔNG QUAN DỮ LIỆU")
    print(f"{'='*50}")
    print(f"Số effect sizes: {len(df)}")
    print(f"Số papers duy nhất: {df['Paper_ID'].nunique()}")
    print(f"Số experiments duy nhất: {df['Exp_ID_Cleaned'].nunique()}")
    print(f"Giai đoạn: {df['Year'].min()} - {df['Year'].max()}")

    # -------------------------------------------------------------------------
    # 2. Descriptive Statistics
    # -------------------------------------------------------------------------
    print("\n[2] Descriptive Statistics...")

    print_distribution(df, 'Industry', 'Phân bố theo Industry')
    print_distribution(df, 'Year', 'Phân bố theo Năm')
    print_distribution(df, 'Task_Type', 'Phân bố theo Task Type')
    print_distribution(df, 'AI_Type_Cleaned', 'Phân bố theo AI Type')
    print_distribution(df, 'Participant_Expert', 'Phân bố theo Expertise')

    # -------------------------------------------------------------------------
    # 3. Compute Effect Sizes
    # -------------------------------------------------------------------------
    print("\n[3] Computing effect sizes...")

    es_s, var_s, es_h, var_h, es_a, var_a, es_n, var_n = compute_all_effect_sizes(df)

    df['es_s'] = es_s
    df['variance_s'] = var_s
    df['es_h'] = es_h
    df['variance_h'] = var_h
    df['es_a'] = es_a
    df['variance_a'] = var_a
    df['es_n'] = es_n
    df['variance_n'] = var_n

    print(f"Strong synergy (es_s): mean = {np.nanmean(es_s):.3f}, valid n = {np.sum(~np.isnan(es_s))}")
    print(f"Human augmentation (es_h): mean = {np.nanmean(es_h):.3f}, valid n = {np.sum(~np.isnan(es_h))}")
    print(f"AI augmentation (es_a): mean = {np.nanmean(es_a):.3f}, valid n = {np.sum(~np.isnan(es_a))}")

    # -------------------------------------------------------------------------
    # 4. Meta-Analysis
    # -------------------------------------------------------------------------
    print("\n[4] Running meta-analysis...")

    results_strong = random_effects_meta(df['es_s'].values, df['variance_s'].values)
    results_human = random_effects_meta(df['es_h'].values, df['variance_h'].values)
    results_ai = random_effects_meta(df['es_a'].values, df['variance_a'].values)
    results_negative = random_effects_meta(df['es_n'].values, df['variance_n'].values)

    print_meta_results(results_strong, "STRONG SYNERGY: Human-AI vs max(Human, AI)")
    print_meta_results(results_human, "HUMAN AUGMENTATION: Human-AI vs Human alone")
    print_meta_results(results_ai, "AI AUGMENTATION: Human-AI vs AI alone")

    # -------------------------------------------------------------------------
    # 5. Create Visualizations
    # -------------------------------------------------------------------------
    print("\n[5] Creating visualizations...")

    create_forest_plot(df['es_h'].values, df['variance_h'].values,
                       "Human Augmentation: Human-AI vs Human Alone",
                       "Figures/ForestPlot_Human_Augmentation.png", results_human)

    create_forest_plot(df['es_a'].values, df['variance_a'].values,
                       "AI Augmentation: Human-AI vs AI Alone",
                       "Figures/ForestPlot_AI_Augmentation.png", results_ai)

    create_forest_plot(df['es_s'].values, df['variance_s'].values,
                       "Strong Synergy: Human-AI vs max(Human, AI)",
                       "Figures/ForestPlot_Strong_Synergy.png", results_strong)

    if results_human:
        create_funnel_plot(df['es_h'].values, df['variance_h'].values,
                           "Funnel Plot: Human-AI vs Human Alone",
                           "Figures/FunnelPlot_Human.png", results_human['estimate'])

    if results_ai:
        create_funnel_plot(df['es_a'].values, df['variance_a'].values,
                           "Funnel Plot: Human-AI vs AI Alone",
                           "Figures/FunnelPlot_AI.png", results_ai['estimate'])

    if results_strong:
        create_funnel_plot(df['es_s'].values, df['variance_s'].values,
                           "Funnel Plot: Human-AI vs max(Human, AI)",
                           "Figures/FunnelPlot_Strong.png", results_strong['estimate'])

    # -------------------------------------------------------------------------
    # 6. Publication Bias Tests
    # -------------------------------------------------------------------------
    print("\n[6] Publication bias tests...")

    print(f"\n{'='*60}")
    print("PUBLICATION BIAS TESTS")
    print(f"{'='*60}")

    comparisons = [
        ('Human-AI vs Human', df['es_h'].values, df['variance_h'].values),
        ('Human-AI vs AI', df['es_a'].values, df['variance_a'].values),
        ('Human-AI vs max(H,AI)', df['es_s'].values, df['variance_s'].values)
    ]

    bias_results = []
    for name, es, var in comparisons:
        egger = eggers_test(es, var)
        rank = rank_correlation_test(es, var)

        print(f"\n{name}:")
        print(f"  Egger's test: intercept = {egger['intercept']:.3f}, p = {egger['intercept_p']:.4f}")
        print(f"  Rank correlation: tau = {rank['tau']:.3f}, p = {rank['p_value']:.4f}")

        bias_results.append({
            'Comparison': name,
            'Egger_intercept': egger['intercept'],
            'Egger_p': egger['intercept_p'],
            'Rank_tau': rank['tau'],
            'Rank_p': rank['p_value']
        })

    # -------------------------------------------------------------------------
    # 7. Moderator Analysis
    # -------------------------------------------------------------------------
    print("\n[7] Moderator analysis...")

    moderators = ['Task_Type', 'Industry', 'AI_Type_Cleaned', 'Participant_Expert',
                  'AI_Expl_Incl', 'Task_Output_Cleaned', 'Comp_Type']

    print(f"\n{'='*70}")
    print("MODERATOR ANALYSIS - Human Augmentation (HAI vs Human)")
    print(f"{'='*70}")

    all_mod_results = []
    for mod in moderators:
        mod_result = subgroup_analysis(df, 'es_h', 'variance_h', mod)
        if len(mod_result) > 0:
            all_mod_results.append(mod_result)
            print(f"\n{mod}:")
            for _, row in mod_result.iterrows():
                sig = "*" if row['p_value'] < 0.05 else ""
                print(f"  {row['Group']}: g = {row['g']:.3f} [{row['CI_lower']:.3f}, {row['CI_upper']:.3f}], k = {row['k']}, I² = {row['I2']:.1f}% {sig}")

    if all_mod_results:
        moderator_df = pd.concat(all_mod_results, ignore_index=True)
        moderator_df.to_csv('Data/ModeratorAnalysis_Human.csv', index=False)

    # -------------------------------------------------------------------------
    # 8. Export Results
    # -------------------------------------------------------------------------
    print("\n[8] Exporting results...")

    # Main results
    main_results = {
        'Human Augmentation': results_human,
        'AI Augmentation': results_ai,
        'Strong Synergy': results_strong
    }

    final_summary = []
    for name, res in main_results.items():
        if res:
            final_summary.append({
                'Comparison': name,
                'k': res['k'],
                'Hedges_g': res['estimate'],
                'SE': res['se'],
                'CI_lower': res['ci_lower'],
                'CI_upper': res['ci_upper'],
                'z': res['z'],
                'p_value': res['p_value'],
                'tau2': res['tau2'],
                'I2': res['I2'],
                'Q': res['Q'],
                'Q_df': res['Q_df'],
                'Q_p': res['Q_pval']
            })

    final_df = pd.DataFrame(final_summary)
    final_df.to_csv('Data/Main_Results.csv', index=False)

    # Save data with effect sizes
    df.to_csv('Data/Data_with_EffectSizes.csv', index=False)

    # -------------------------------------------------------------------------
    # 9. Summary Report
    # -------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("BÁO CÁO TÓM TẮT KẾT QUẢ META-ANALYSIS")
    print("=" * 70)

    print(f"\n📊 DỮ LIỆU:")
    print(f"   - Tổng số effect sizes: {len(df)}")
    print(f"   - Số papers: {df['Paper_ID'].nunique()}")
    print(f"   - Số experiments: {df['Exp_ID_Cleaned'].nunique()}")
    print(f"   - Giai đoạn: {df['Year'].min()}-{df['Year'].max()}")

    print(f"\n📈 KẾT QUẢ CHÍNH:")

    if results_human:
        sig_h = "✓ Significant" if results_human['p_value'] < 0.05 else "✗ Not significant"
        print(f"\n   1. Human Augmentation (HAI vs Human):")
        print(f"      g = {results_human['estimate']:.3f} [{results_human['ci_lower']:.3f}, {results_human['ci_upper']:.3f}]")
        print(f"      p = {results_human['p_value']:.4f} {sig_h}")
        print(f"      I² = {results_human['I2']:.1f}%")
        if results_human['estimate'] > 0:
            print(f"      → Human-AI tốt hơn Human alone")
        else:
            print(f"      → Human alone tốt hơn Human-AI")

    if results_ai:
        sig_a = "✓ Significant" if results_ai['p_value'] < 0.05 else "✗ Not significant"
        print(f"\n   2. AI Augmentation (HAI vs AI):")
        print(f"      g = {results_ai['estimate']:.3f} [{results_ai['ci_lower']:.3f}, {results_ai['ci_upper']:.3f}]")
        print(f"      p = {results_ai['p_value']:.4f} {sig_a}")
        print(f"      I² = {results_ai['I2']:.1f}%")
        if results_ai['estimate'] > 0:
            print(f"      → Human-AI tốt hơn AI alone")
        else:
            print(f"      → AI alone tốt hơn Human-AI")

    if results_strong:
        sig_s = "✓ Significant" if results_strong['p_value'] < 0.05 else "✗ Not significant"
        print(f"\n   3. Strong Synergy (HAI vs max(H, AI)):")
        print(f"      g = {results_strong['estimate']:.3f} [{results_strong['ci_lower']:.3f}, {results_strong['ci_upper']:.3f}]")
        print(f"      p = {results_strong['p_value']:.4f} {sig_s}")
        print(f"      I² = {results_strong['I2']:.1f}%")
        if results_strong['estimate'] > 0:
            print(f"      → Có synergy thực sự (HAI > cả H và AI)")
        else:
            print(f"      → Không có synergy (HAI không vượt trội)")

    print(f"\n📁 FILES EXPORTED:")
    print(f"   - Data/Main_Results.csv")
    print(f"   - Data/ModeratorAnalysis_Human.csv")
    print(f"   - Data/Data_with_EffectSizes.csv")
    print(f"   - Figures/ForestPlot_*.png")
    print(f"   - Figures/FunnelPlot_*.png")

    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE!")
    print("=" * 70)

    return df, results_human, results_ai, results_strong


if __name__ == "__main__":
    df, results_human, results_ai, results_strong = main()
