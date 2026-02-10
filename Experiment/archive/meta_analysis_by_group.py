"""
Meta-Analysis By Group: Human-AI Collaboration
Chia dữ liệu theo Task và Industry, sau đó chạy meta-analysis riêng cho từng nhóm

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
os.makedirs('Figures/ByTask', exist_ok=True)
os.makedirs('Figures/ByIndustry', exist_ok=True)
os.makedirs('Data/ByTask', exist_ok=True)
os.makedirs('Data/ByIndustry', exist_ok=True)


# ============================================================================
# SECTION 1: CORE FUNCTIONS (từ meta-analysis.py)
# ============================================================================

def compute_hedges_g(m1, m2, sd1, sd2, n1, n2):
    """Tính Hedges' g (Standardized Mean Difference)"""
    if sd1 <= 0 or sd2 <= 0 or n1 <= 1 or n2 <= 1:
        return np.nan, np.nan

    sd_pooled = np.sqrt(((n1 - 1) * sd1**2 + (n2 - 1) * sd2**2) / (n1 + n2 - 2))

    if sd_pooled == 0:
        return np.nan, np.nan

    d = (m1 - m2) / sd_pooled
    df = n1 + n2 - 2
    j = 1 - (3 / (4 * df - 1))
    g = j * d
    var_g = ((n1 + n2) / (n1 * n2) + (g**2) / (2 * (n1 + n2))) * (j**2)

    return g, var_g


def compute_all_effect_sizes(df):
    """Tính tất cả effect sizes cho dataframe"""
    n = len(df)
    es_s, var_s = np.zeros(n), np.zeros(n)
    es_h, var_h = np.zeros(n), np.zeros(n)
    es_a, var_a = np.zeros(n), np.zeros(n)
    es_n, var_n = np.zeros(n), np.zeros(n)

    for i in range(n):
        row = df.iloc[i]

        m_hai = row['Avg_Perf_HumanAI_Adj']
        m_h = row['Avg_Perf_Human_Adj']
        m_ai = row['Avg_Perf_AI_Adj']
        m_base = row['Avg_Perf_Baseline_Adj']
        m_worse = row.get('Avg_Perf_Worse_Adj', np.nan)

        sd_hai = row['Sd_Perf_HumanAI']
        sd_h = row['Sd_Perf_Human']
        sd_ai = row['Sd_Perf_AI']
        sd_base = row['Sd_Perf_Baseline']
        sd_worse = row.get('Sd_Perf_Worse', np.nan)

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


def random_effects_meta(effect_sizes, variances):
    """Random-effects meta-analysis (DerSimonian-Laird)"""
    mask = ~np.isnan(effect_sizes) & ~np.isnan(variances) & (variances > 0)
    es = effect_sizes[mask]
    var = variances[mask]
    k = len(es)

    if k < 2:
        return None

    w = 1 / var
    fe_estimate = np.sum(w * es) / np.sum(w)
    Q = np.sum(w * (es - fe_estimate)**2)
    df = k - 1
    Q_pval = 1 - stats.chi2.cdf(Q, df)

    C = np.sum(w) - np.sum(w**2) / np.sum(w)
    tau2 = max(0, (Q - df) / C)

    w_re = 1 / (var + tau2)
    re_estimate = np.sum(w_re * es) / np.sum(w_re)
    se = np.sqrt(1 / np.sum(w_re))

    ci_lower = re_estimate - 1.96 * se
    ci_upper = re_estimate + 1.96 * se

    z = re_estimate / se
    p_value = 2 * (1 - norm.cdf(abs(z)))

    I2 = 100 * (Q - df) / Q if Q > df else 0
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


def eggers_test(effect_sizes, variances):
    """Egger's regression test for publication bias"""
    mask = ~np.isnan(effect_sizes) & ~np.isnan(variances) & (variances > 0)
    es = effect_sizes[mask]
    se = np.sqrt(variances[mask])

    if len(es) < 3:
        return None

    precision = 1 / se
    std_es = es / se

    X = sm.add_constant(precision)
    model = sm.OLS(std_es, X).fit()

    return {
        'intercept': model.params[0],
        'intercept_se': model.bse[0],
        'intercept_p': model.pvalues[0],
        'slope': model.params[1],
        'slope_p': model.pvalues[1]
    }


def rank_correlation_test(effect_sizes, variances):
    """Begg and Mazumdar rank correlation test"""
    mask = ~np.isnan(effect_sizes) & ~np.isnan(variances) & (variances > 0)
    es = effect_sizes[mask]
    se = np.sqrt(variances[mask])

    if len(es) < 3:
        return None

    tau, p_value = stats.kendalltau(es, se)
    return {'tau': tau, 'p_value': p_value}


# ============================================================================
# SECTION 2: VISUALIZATION FUNCTIONS
# ============================================================================

def create_forest_plot(effect_sizes, variances, title, filename, pooled_result):
    """Tạo forest plot"""
    mask = ~np.isnan(effect_sizes) & ~np.isnan(variances)
    es = effect_sizes[mask]
    var = variances[mask]
    se = np.sqrt(var)

    if len(es) < 2:
        print(f"  Skipped forest plot (insufficient data): {filename}")
        return

    sort_idx = np.argsort(es)
    es = es[sort_idx]
    se = se[sort_idx]

    k = len(es)

    fig, ax = plt.subplots(figsize=(11.5, max(6.5, k * 0.22)))

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

    ax.text(0.02, 0.98, f"Negative: {n_neg} ({n_neg/k*100:.1f}%)",
            transform=ax.transAxes, fontsize=10, verticalalignment='top', color='darkred')
    ax.text(0.98, 0.98, f"Positive: {n_pos} ({n_pos/k*100:.1f}%)",
            transform=ax.transAxes, fontsize=10, verticalalignment='top',
            horizontalalignment='right', color='darkgreen')

    if pooled_result:
        pooled_text = (
            f"Pooled: g = {pooled_result['estimate']:.3f} "
            f"[{pooled_result['ci_lower']:.3f}, {pooled_result['ci_upper']:.3f}]"
        )
        ax.text(0.5, -0.10, pooled_text, transform=ax.transAxes, fontsize=10.5,
                horizontalalignment='center', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.18), frameon=True)

    plt.tight_layout(rect=[0, 0.06, 1, 1])
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {filename}")


def create_funnel_plot(effect_sizes, variances, title, filename, pooled_estimate):
    """Tạo funnel plot"""
    mask = ~np.isnan(effect_sizes) & ~np.isnan(variances) & (variances > 0)
    es = effect_sizes[mask]
    se = np.sqrt(variances[mask])

    if len(es) < 3:
        print(f"  Skipped funnel plot (insufficient data): {filename}")
        return

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
    print(f"  Saved: {filename}")


# ============================================================================
# SECTION 3: META-ANALYSIS FOR A SINGLE GROUP
# ============================================================================

def run_meta_analysis_for_group(df_group, group_name, output_dir, figures_dir):
    """
    Chạy full meta-analysis cho một group (như meta-analysis.py)

    Parameters:
    -----------
    df_group : DataFrame - dữ liệu của group
    group_name : str - tên group (vd: "Healthcare", "Classification")
    output_dir : str - thư mục lưu data
    figures_dir : str - thư mục lưu figures

    Returns:
    --------
    dict với kết quả meta-analysis
    """
    print(f"\n{'='*60}")
    print(f"META-ANALYSIS: {group_name}")
    print(f"{'='*60}")

    # Sanitize group name for filenames
    safe_name = group_name.replace(' ', '_').replace('/', '_').replace('\\', '_')

    # -------------------------------------------------------------------------
    # 1. Basic Info
    # -------------------------------------------------------------------------
    print(f"\n[1] Data Overview:")
    print(f"    - Effect sizes: {len(df_group)}")
    print(f"    - Papers: {df_group['Paper_ID'].nunique()}")
    print(f"    - Experiments: {df_group['Exp_ID_Cleaned'].nunique()}")

    if len(df_group) < 2:
        print(f"    WARNING: Insufficient data (need at least 2 effect sizes)")
        return None

    # -------------------------------------------------------------------------
    # 2. Compute Effect Sizes
    # -------------------------------------------------------------------------
    print(f"\n[2] Computing effect sizes...")

    es_s, var_s, es_h, var_h, es_a, var_a, es_n, var_n = compute_all_effect_sizes(df_group)

    df_group = df_group.copy()
    df_group['es_s'], df_group['variance_s'] = es_s, var_s
    df_group['es_h'], df_group['variance_h'] = es_h, var_h
    df_group['es_a'], df_group['variance_a'] = es_a, var_a
    df_group['es_n'], df_group['variance_n'] = es_n, var_n

    # -------------------------------------------------------------------------
    # 3. Run Meta-Analysis
    # -------------------------------------------------------------------------
    print(f"\n[3] Running meta-analysis...")

    results_human = random_effects_meta(df_group['es_h'].values, df_group['variance_h'].values)
    results_ai = random_effects_meta(df_group['es_a'].values, df_group['variance_a'].values)
    results_strong = random_effects_meta(df_group['es_s'].values, df_group['variance_s'].values)

    # Print results
    comparisons = [
        ('Human Augmentation (HAI vs Human)', results_human),
        ('AI Augmentation (HAI vs AI)', results_ai),
        ('Strong Synergy (HAI vs max)', results_strong)
    ]

    for name, res in comparisons:
        if res:
            sig = '***' if res['p_value'] < 0.001 else '**' if res['p_value'] < 0.01 else '*' if res['p_value'] < 0.05 else ''
            print(f"    {name}:")
            print(f"      g = {res['estimate']:.4f} [{res['ci_lower']:.4f}, {res['ci_upper']:.4f}]")
            print(f"      z = {res['z']:.3f}, p = {res['p_value']:.4f} {sig}")
            print(f"      tau2 = {res['tau2']:.4f}, I2 = {res['I2']:.1f}%")
        else:
            print(f"    {name}: Insufficient data")

    # -------------------------------------------------------------------------
    # 4. Publication Bias Tests
    # -------------------------------------------------------------------------
    print(f"\n[4] Publication bias tests...")

    bias_results = []
    for name, es_col, var_col in [
        ('Human Augmentation', df_group['es_h'].values, df_group['variance_h'].values),
        ('AI Augmentation', df_group['es_a'].values, df_group['variance_a'].values),
        ('Strong Synergy', df_group['es_s'].values, df_group['variance_s'].values)
    ]:
        egger = eggers_test(es_col, var_col)
        rank = rank_correlation_test(es_col, var_col)

        if egger and rank:
            print(f"    {name}:")
            print(f"      Egger's: intercept = {egger['intercept']:.3f}, p = {egger['intercept_p']:.4f}")
            print(f"      Rank: tau = {rank['tau']:.3f}, p = {rank['p_value']:.4f}")

            bias_results.append({
                'Comparison': name,
                'Egger_intercept': egger['intercept'],
                'Egger_p': egger['intercept_p'],
                'Rank_tau': rank['tau'],
                'Rank_p': rank['p_value']
            })

    # -------------------------------------------------------------------------
    # 5. Create Visualizations
    # -------------------------------------------------------------------------
    print(f"\n[5] Creating visualizations...")

    # Forest plots
    if results_human:
        create_forest_plot(
            df_group['es_h'].values, df_group['variance_h'].values,
            f"Human Augmentation: {group_name}",
            f"{figures_dir}/ForestPlot_Human_{safe_name}.png",
            results_human
        )

    if results_ai:
        create_forest_plot(
            df_group['es_a'].values, df_group['variance_a'].values,
            f"AI Augmentation: {group_name}",
            f"{figures_dir}/ForestPlot_AI_{safe_name}.png",
            results_ai
        )

    if results_strong:
        create_forest_plot(
            df_group['es_s'].values, df_group['variance_s'].values,
            f"Strong Synergy: {group_name}",
            f"{figures_dir}/ForestPlot_Synergy_{safe_name}.png",
            results_strong
        )

    # Funnel plots
    if results_human:
        create_funnel_plot(
            df_group['es_h'].values, df_group['variance_h'].values,
            f"Funnel Plot Human: {group_name}",
            f"{figures_dir}/FunnelPlot_Human_{safe_name}.png",
            results_human['estimate']
        )

    if results_ai:
        create_funnel_plot(
            df_group['es_a'].values, df_group['variance_a'].values,
            f"Funnel Plot AI: {group_name}",
            f"{figures_dir}/FunnelPlot_AI_{safe_name}.png",
            results_ai['estimate']
        )

    if results_strong:
        create_funnel_plot(
            df_group['es_s'].values, df_group['variance_s'].values,
            f"Funnel Plot Synergy: {group_name}",
            f"{figures_dir}/FunnelPlot_Synergy_{safe_name}.png",
            results_strong['estimate']
        )

    # -------------------------------------------------------------------------
    # 6. Save Results
    # -------------------------------------------------------------------------
    print(f"\n[6] Saving results...")

    # Save main results
    main_results = []
    for name, res in [('Human Augmentation', results_human),
                      ('AI Augmentation', results_ai),
                      ('Strong Synergy', results_strong)]:
        if res:
            main_results.append({
                'Group': group_name,
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

    results_df = pd.DataFrame(main_results)
    results_df.to_csv(f"{output_dir}/Results_{safe_name}.csv", index=False)

    # Save data with effect sizes
    df_group.to_csv(f"{output_dir}/Data_{safe_name}.csv", index=False)

    # Save bias results
    if bias_results:
        bias_df = pd.DataFrame(bias_results)
        bias_df['Group'] = group_name
        bias_df.to_csv(f"{output_dir}/Bias_{safe_name}.csv", index=False)

    print(f"    Saved: Results_{safe_name}.csv, Data_{safe_name}.csv")

    return {
        'group': group_name,
        'n_effects': len(df_group),
        'n_papers': df_group['Paper_ID'].nunique(),
        'human_augmentation': results_human,
        'ai_augmentation': results_ai,
        'strong_synergy': results_strong
    }


# ============================================================================
# SECTION 4: MAIN ANALYSIS BY TASK AND INDUSTRY
# ============================================================================

def run_analysis_by_grouping(df, grouping_col, output_base, figures_base):
    """
    Chia data theo grouping_col và chạy meta-analysis cho từng nhóm

    Parameters:
    -----------
    df : DataFrame
    grouping_col : str - cột để chia nhóm (vd: 'Task_Type', 'Industry')
    output_base : str - thư mục base cho output
    figures_base : str - thư mục base cho figures
    """
    print(f"\n{'#'*70}")
    print(f"# ANALYSIS BY: {grouping_col}")
    print(f"{'#'*70}")

    # Get unique groups
    groups = df[grouping_col].dropna().unique()
    print(f"\nFound {len(groups)} groups: {list(groups)}")

    all_results = []

    for group in sorted(groups):
        # Filter data for this group
        df_group = df[df[grouping_col] == group].copy()

        # Run meta-analysis
        result = run_meta_analysis_for_group(
            df_group,
            group_name=f"{grouping_col}: {group}",
            output_dir=output_base,
            figures_dir=figures_base
        )

        if result:
            all_results.append(result)

    return all_results


def create_comparison_plot(all_results, grouping_col, filename):
    """Tạo plot so sánh kết quả giữa các groups"""
    if not all_results:
        return

    # Prepare data for plotting
    data = []
    for result in all_results:
        group_name = result['group'].replace(f"{grouping_col}: ", "")

        for comp_name, comp_key in [
            ('Human Aug.', 'human_augmentation'),
            ('AI Aug.', 'ai_augmentation'),
            ('Synergy', 'strong_synergy')
        ]:
            res = result[comp_key]
            if res:
                data.append({
                    'Group': group_name,
                    'Comparison': comp_name,
                    'g': res['estimate'],
                    'CI_lower': res['ci_lower'],
                    'CI_upper': res['ci_upper'],
                    'p_value': res['p_value'],
                    'k': res['k']
                })

    if not data:
        return

    plot_df = pd.DataFrame(data)

    # Create figure
    fig, axes = plt.subplots(1, 3, figsize=(17, max(5.5, len(all_results) * 0.55)))

    comparisons = ['Human Aug.', 'AI Aug.', 'Synergy']
    titles = ['HAI vs Human', 'HAI vs AI', 'HAI vs max(H,AI)']

    for idx, (comp, title) in enumerate(zip(comparisons, titles)):
        ax = axes[idx]
        comp_data = plot_df[plot_df['Comparison'] == comp].sort_values('g')

        if len(comp_data) == 0:
            ax.set_visible(False)
            continue

        y_pos = np.arange(len(comp_data))
        colors = ['darkgreen' if (g > 0 and p < 0.05) else
                  'darkred' if (g < 0 and p < 0.05) else 'gray'
                  for g, p in zip(comp_data['g'], comp_data['p_value'])]

        # Plot bars with error bars
        for i, (_, row) in enumerate(comp_data.iterrows()):
            ax.barh(i, row['g'], color=colors[i], alpha=0.7, edgecolor='black')
            ax.errorbar(row['g'], i,
                       xerr=[[row['g'] - row['CI_lower']], [row['CI_upper'] - row['g']]],
                       fmt='none', color='black', capsize=3)

            # Add significance marker
            sig = '***' if row['p_value'] < 0.001 else '**' if row['p_value'] < 0.01 else '*' if row['p_value'] < 0.05 else ''
            x_margin = 0.06
            x_pos = row['CI_upper'] + x_margin if row['g'] >= 0 else row['CI_lower'] - x_margin
            ha = 'left' if row['g'] >= 0 else 'right'
            ax.text(x_pos, i, f"{sig} (k={row['k']})", va='center', ha=ha, fontsize=8)

        ax.axvline(0, color='black', linestyle='--', linewidth=1)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(comp_data['Group'])
        ax.set_xlabel("Hedges' g")
        ax.set_title(title, fontweight='bold', pad=8)
        ci_min = comp_data['CI_lower'].min()
        ci_max = comp_data['CI_upper'].max()
        pad = max(0.12, 0.08 * (ci_max - ci_min))
        ax.set_xlim(ci_min - pad, ci_max + pad)

    plt.suptitle(f"Meta-Analysis Results by {grouping_col}", fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0, 0.02, 1, 0.96])
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"\nSaved comparison plot: {filename}")


def main():
    """Main function"""

    print("=" * 70)
    print("META-ANALYSIS BY GROUP: HUMAN-AI COLLABORATION")
    print("Chia theo Task và Industry, chạy meta-analysis riêng cho từng nhóm")
    print("=" * 70)

    # -------------------------------------------------------------------------
    # 1. Load Data
    # -------------------------------------------------------------------------
    print("\n[1] Loading data...")
    df = pd.read_excel("Data_Extraction_communication_public.xlsx")

    print(f"\nTotal data:")
    print(f"  - Effect sizes: {len(df)}")
    print(f"  - Papers: {df['Paper_ID'].nunique()}")
    print(f"  - Experiments: {df['Exp_ID_Cleaned'].nunique()}")

    # Show distribution
    print(f"\nTask_Type distribution:")
    print(df['Task_Type'].value_counts())

    print(f"\nIndustry distribution:")
    print(df['Industry'].value_counts())

    # -------------------------------------------------------------------------
    # 2. Analysis by Task
    # -------------------------------------------------------------------------
    task_results = run_analysis_by_grouping(
        df,
        grouping_col='Task_Type',
        output_base='Data/ByTask',
        figures_base='Figures/ByTask'
    )

    # Create comparison plot for tasks
    create_comparison_plot(task_results, 'Task_Type', 'Figures/ByTask/Comparison_ByTask.png')

    # -------------------------------------------------------------------------
    # 3. Analysis by Industry
    # -------------------------------------------------------------------------
    industry_results = run_analysis_by_grouping(
        df,
        grouping_col='Industry',
        output_base='Data/ByIndustry',
        figures_base='Figures/ByIndustry'
    )

    # Create comparison plot for industry
    create_comparison_plot(industry_results, 'Industry', 'Figures/ByIndustry/Comparison_ByIndustry.png')

    # -------------------------------------------------------------------------
    # 4. Summary Report
    # -------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SUMMARY REPORT")
    print("=" * 70)

    # Summary by Task
    print("\n### BY TASK TYPE ###")
    for result in task_results:
        group = result['group']
        print(f"\n{group} (k={result['n_effects']}, papers={result['n_papers']}):")

        for name, key in [('Human Aug', 'human_augmentation'),
                          ('AI Aug', 'ai_augmentation'),
                          ('Synergy', 'strong_synergy')]:
            res = result[key]
            if res:
                sig = '*' if res['p_value'] < 0.05 else ''
                print(f"  {name}: g = {res['estimate']:.3f} [{res['ci_lower']:.3f}, {res['ci_upper']:.3f}] {sig}")

    # Summary by Industry
    print("\n### BY INDUSTRY ###")
    for result in industry_results:
        group = result['group']
        print(f"\n{group} (k={result['n_effects']}, papers={result['n_papers']}):")

        for name, key in [('Human Aug', 'human_augmentation'),
                          ('AI Aug', 'ai_augmentation'),
                          ('Synergy', 'strong_synergy')]:
            res = result[key]
            if res:
                sig = '*' if res['p_value'] < 0.05 else ''
                print(f"  {name}: g = {res['estimate']:.3f} [{res['ci_lower']:.3f}, {res['ci_upper']:.3f}] {sig}")

    # -------------------------------------------------------------------------
    # 5. Save Combined Summary
    # -------------------------------------------------------------------------
    print("\n[5] Saving combined summary...")

    # Combine all results
    all_summary = []

    for result in task_results + industry_results:
        for name, key in [('Human Augmentation', 'human_augmentation'),
                          ('AI Augmentation', 'ai_augmentation'),
                          ('Strong Synergy', 'strong_synergy')]:
            res = result[key]
            if res:
                all_summary.append({
                    'Grouping': result['group'].split(':')[0].strip(),
                    'Group': result['group'].split(':')[1].strip() if ':' in result['group'] else result['group'],
                    'Comparison': name,
                    'k': res['k'],
                    'n_papers': result['n_papers'],
                    'g': res['estimate'],
                    'SE': res['se'],
                    'CI_lower': res['ci_lower'],
                    'CI_upper': res['ci_upper'],
                    'p_value': res['p_value'],
                    'I2': res['I2'],
                    'tau2': res['tau2']
                })

    summary_df = pd.DataFrame(all_summary)
    summary_df.to_csv('Data/Summary_ByGroup.csv', index=False)

    print("\nFiles saved:")
    print("  - Data/Summary_ByGroup.csv (combined summary)")
    print("  - Data/ByTask/*.csv (detailed by task)")
    print("  - Data/ByIndustry/*.csv (detailed by industry)")
    print("  - Figures/ByTask/*.png")
    print("  - Figures/ByIndustry/*.png")

    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE!")
    print("=" * 70)

    return df, task_results, industry_results


if __name__ == "__main__":
    df, task_results, industry_results = main()
