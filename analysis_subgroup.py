"""
Subgroup Meta-Analysis: Human-AI Collaboration
Chia nhóm theo các moderators và so sánh

Author: [Your Name]
Date: 2026
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

warnings.filterwarnings('ignore')

# Create output directories
os.makedirs('Figures', exist_ok=True)
os.makedirs('Data', exist_ok=True)


# ============================================================================
# SECTION 1: CORE FUNCTIONS
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

    for i in range(n):
        row = df.iloc[i]

        m_hai = row['Avg_Perf_HumanAI_Adj']
        m_h = row['Avg_Perf_Human_Adj']
        m_ai = row['Avg_Perf_AI_Adj']
        m_base = row['Avg_Perf_Baseline_Adj']

        sd_hai = row['Sd_Perf_HumanAI']
        sd_h = row['Sd_Perf_Human']
        sd_ai = row['Sd_Perf_AI']
        sd_base = row['Sd_Perf_Baseline']

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

        except Exception:
            es_s[i], var_s[i] = np.nan, np.nan
            es_h[i], var_h[i] = np.nan, np.nan
            es_a[i], var_a[i] = np.nan, np.nan

    return es_s, var_s, es_h, var_h, es_a, var_a


def random_effects_meta(effect_sizes, variances):
    """Random-effects meta-analysis"""
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

    return {
        'k': k,
        'g': re_estimate,
        'se': se,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'z': z,
        'p': p_value,
        'tau2': tau2,
        'I2': I2,
        'Q': Q,
        'Q_df': df,
        'Q_p': Q_pval
    }


# ============================================================================
# SECTION 2: SUBGROUP ANALYSIS FUNCTIONS
# ============================================================================

def subgroup_analysis(df, moderator, es_col, var_col):
    """
    Thực hiện subgroup analysis cho một moderator

    Parameters:
    -----------
    df : DataFrame với effect sizes
    moderator : tên cột moderator
    es_col : tên cột effect size
    var_col : tên cột variance

    Returns:
    --------
    DataFrame với kết quả cho từng subgroup
    """
    results = []

    for group in sorted(df[moderator].dropna().unique()):
        mask = df[moderator] == group
        es = df.loc[mask, es_col].values
        var = df.loc[mask, var_col].values

        meta_result = random_effects_meta(es, var)

        if meta_result:
            # Xác định significance level
            p = meta_result['p']
            if p < 0.001:
                sig = '***'
            elif p < 0.01:
                sig = '**'
            elif p < 0.05:
                sig = '*'
            else:
                sig = ''

            results.append({
                'Moderator': moderator,
                'Group': group,
                'k': meta_result['k'],
                'g': meta_result['g'],
                'SE': meta_result['se'],
                'CI_lower': meta_result['ci_lower'],
                'CI_upper': meta_result['ci_upper'],
                'z': meta_result['z'],
                'p': meta_result['p'],
                'sig': sig,
                'tau2': meta_result['tau2'],
                'I2': meta_result['I2'],
                'Q': meta_result['Q'],
                'Q_p': meta_result['Q_p']
            })

    return pd.DataFrame(results)


def run_all_subgroup_analyses(df, moderators, es_col, var_col, comparison_name):
    """
    Chạy subgroup analysis cho tất cả moderators

    Parameters:
    -----------
    df : DataFrame
    moderators : list of moderator column names
    es_col : effect size column
    var_col : variance column
    comparison_name : tên của comparison (vd: "Human Augmentation")

    Returns:
    --------
    DataFrame với tất cả kết quả
    """
    all_results = []

    for mod in moderators:
        if mod in df.columns:
            result = subgroup_analysis(df, mod, es_col, var_col)
            if len(result) > 0:
                result['Comparison'] = comparison_name
                all_results.append(result)

    if all_results:
        return pd.concat(all_results, ignore_index=True)
    else:
        return pd.DataFrame()


# ============================================================================
# SECTION 3: VISUALIZATION FUNCTIONS
# ============================================================================

def plot_subgroup_forest(results_df, comparison_name, filename):
    """
    Tạo forest plot cho subgroup analysis
    """
    if len(results_df) == 0:
        return

    fig, ax = plt.subplots(figsize=(12, max(6, len(results_df) * 0.4)))

    y_pos = np.arange(len(results_df))

    # Colors based on significance and direction
    colors = []
    for _, row in results_df.iterrows():
        if row['p'] < 0.05:
            if row['g'] > 0:
                colors.append('darkgreen')
            else:
                colors.append('darkred')
        else:
            colors.append('gray')

    # Plot effect sizes with CI
    for i, (_, row) in enumerate(results_df.iterrows()):
        ax.errorbar(row['g'], i,
                   xerr=[[row['g'] - row['CI_lower']], [row['CI_upper'] - row['g']]],
                   fmt='o', color=colors[i], capsize=4, capthick=2, markersize=8)

    # Reference line at 0
    ax.axvline(0, color='black', linestyle='--', linewidth=1)

    # Shading
    ax.axvspan(-3, 0, alpha=0.05, color='red')
    ax.axvspan(0, 3, alpha=0.05, color='green')

    # Labels
    labels = [f"{row['Moderator']}: {row['Group']} (k={row['k']}) {row['sig']}"
              for _, row in results_df.iterrows()]
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.set_xlabel("Effect Size (Hedges' g)", fontsize=12)
    ax.set_title(f"Subgroup Analysis: {comparison_name}", fontsize=14, fontweight='bold')
    ax.set_xlim(-1.5, 1.5)

    # Add text for effect sizes
    for i, (_, row) in enumerate(results_df.iterrows()):
        ax.text(1.2, i, f"g={row['g']:.2f}", va='center', fontsize=9)

    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filename}")


def plot_moderator_comparison(results_df, moderator, filename):
    """
    Tạo bar chart so sánh effect sizes giữa các groups của một moderator
    """
    mod_data = results_df[results_df['Moderator'] == moderator].copy()

    if len(mod_data) == 0:
        return

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    comparisons = ['Human Augmentation', 'AI Augmentation', 'Strong Synergy']
    titles = ['HAI vs Human', 'HAI vs AI', 'HAI vs max(H,AI)']

    for idx, (comp, title) in enumerate(zip(comparisons, titles)):
        ax = axes[idx]
        data = mod_data[mod_data['Comparison'] == comp]

        if len(data) == 0:
            ax.set_visible(False)
            continue

        groups = data['Group'].values
        effects = data['g'].values
        errors = [(data['g'] - data['CI_lower']).values,
                  (data['CI_upper'] - data['g']).values]

        colors = ['darkgreen' if e > 0 and p < 0.05 else
                  'darkred' if e < 0 and p < 0.05 else 'gray'
                  for e, p in zip(effects, data['p'].values)]

        bars = ax.barh(groups, effects, xerr=errors, color=colors,
                       capsize=4, alpha=0.7, edgecolor='black')

        ax.axvline(0, color='black', linestyle='--', linewidth=1)
        ax.set_xlabel("Hedges' g")
        ax.set_title(title, fontweight='bold')

        # Add significance markers
        for i, (_, row) in enumerate(data.iterrows()):
            x_pos = row['g'] + 0.05 if row['g'] > 0 else row['g'] - 0.15
            ax.text(x_pos, i, row['sig'], va='center', fontsize=10, fontweight='bold')

    plt.suptitle(f"Effect Sizes by {moderator}", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filename}")


def create_summary_heatmap(all_results, filename):
    """
    Tạo heatmap tổng hợp effect sizes theo moderators
    """
    # Pivot table
    pivot_data = []

    for comp in ['Human Augmentation', 'AI Augmentation', 'Strong Synergy']:
        comp_data = all_results[all_results['Comparison'] == comp]
        for _, row in comp_data.iterrows():
            pivot_data.append({
                'Moderator_Group': f"{row['Moderator']}: {row['Group']}",
                'Comparison': comp,
                'g': row['g'],
                'sig': row['sig']
            })

    pivot_df = pd.DataFrame(pivot_data)

    if len(pivot_df) == 0:
        return

    # Create pivot table
    heatmap_data = pivot_df.pivot(index='Moderator_Group', columns='Comparison', values='g')

    # Create figure
    fig, ax = plt.subplots(figsize=(10, max(8, len(heatmap_data) * 0.3)))

    # Heatmap
    sns.heatmap(heatmap_data, annot=True, fmt='.2f', cmap='RdYlGn', center=0,
                vmin=-1, vmax=1, ax=ax, linewidths=0.5,
                cbar_kws={'label': "Hedges' g"})

    ax.set_title('Summary Heatmap: Effect Sizes by Subgroups', fontsize=14, fontweight='bold')
    ax.set_xlabel('')
    ax.set_ylabel('')

    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filename}")


# ============================================================================
# SECTION 4: MAIN ANALYSIS
# ============================================================================

def main():
    """Main function"""

    print("=" * 70)
    print("SUBGROUP META-ANALYSIS: HUMAN-AI COLLABORATION")
    print("=" * 70)

    # -------------------------------------------------------------------------
    # 1. Load and Prepare Data
    # -------------------------------------------------------------------------
    print("\n[1] Loading data...")
    df = pd.read_excel("Data_Extraction_communication_public.xlsx")

    print(f"Total effect sizes: {len(df)}")
    print(f"Papers: {df['Paper_ID'].nunique()}")
    print(f"Experiments: {df['Exp_ID_Cleaned'].nunique()}")

    # -------------------------------------------------------------------------
    # 2. Compute Effect Sizes
    # -------------------------------------------------------------------------
    print("\n[2] Computing effect sizes...")
    es_s, var_s, es_h, var_h, es_a, var_a = compute_all_effect_sizes(df)

    df['es_s'], df['var_s'] = es_s, var_s
    df['es_h'], df['var_h'] = es_h, var_h
    df['es_a'], df['var_a'] = es_a, var_a

    # -------------------------------------------------------------------------
    # 3. Overall Meta-Analysis
    # -------------------------------------------------------------------------
    print("\n[3] Overall meta-analysis...")

    overall_results = []

    # Human Augmentation
    res_h = random_effects_meta(df['es_h'].values, df['var_h'].values)
    if res_h:
        res_h['Comparison'] = 'Human Augmentation'
        overall_results.append(res_h)
        print(f"  Human Augmentation: g = {res_h['g']:.3f} [{res_h['ci_lower']:.3f}, {res_h['ci_upper']:.3f}], p = {res_h['p']:.4f}")

    # AI Augmentation
    res_a = random_effects_meta(df['es_a'].values, df['var_a'].values)
    if res_a:
        res_a['Comparison'] = 'AI Augmentation'
        overall_results.append(res_a)
        print(f"  AI Augmentation: g = {res_a['g']:.3f} [{res_a['ci_lower']:.3f}, {res_a['ci_upper']:.3f}], p = {res_a['p']:.4f}")

    # Strong Synergy
    res_s = random_effects_meta(df['es_s'].values, df['var_s'].values)
    if res_s:
        res_s['Comparison'] = 'Strong Synergy'
        overall_results.append(res_s)
        print(f"  Strong Synergy: g = {res_s['g']:.3f} [{res_s['ci_lower']:.3f}, {res_s['ci_upper']:.3f}], p = {res_s['p']:.4f}")

    # -------------------------------------------------------------------------
    # 4. Subgroup Analysis
    # -------------------------------------------------------------------------
    print("\n[4] Subgroup analysis...")

    # Define moderators
    moderators = [
        'Industry',
        'Task_Type',
        'AI_Type_Cleaned',
        'Participant_Expert',
        'AI_Expl_Incl',
        'Task_Output_Cleaned',
        'Baseline',
        'Comp_Type',
        'Year'
    ]

    # Filter to existing moderators
    moderators = [m for m in moderators if m in df.columns]

    # Run subgroup analyses
    print("\n  Human Augmentation (HAI vs Human):")
    results_h = run_all_subgroup_analyses(df, moderators, 'es_h', 'var_h', 'Human Augmentation')

    print("\n  AI Augmentation (HAI vs AI):")
    results_a = run_all_subgroup_analyses(df, moderators, 'es_a', 'var_a', 'AI Augmentation')

    print("\n  Strong Synergy (HAI vs max):")
    results_s = run_all_subgroup_analyses(df, moderators, 'es_s', 'var_s', 'Strong Synergy')

    # Combine all results
    all_results = pd.concat([results_h, results_a, results_s], ignore_index=True)

    # -------------------------------------------------------------------------
    # 5. Print Results
    # -------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SUBGROUP RESULTS")
    print("=" * 70)

    for mod in moderators:
        mod_data = all_results[all_results['Moderator'] == mod]
        if len(mod_data) > 0:
            print(f"\n### {mod}")
            print("-" * 60)

            for comp in ['Human Augmentation', 'AI Augmentation', 'Strong Synergy']:
                comp_data = mod_data[mod_data['Comparison'] == comp]
                if len(comp_data) > 0:
                    print(f"\n  {comp}:")
                    for _, row in comp_data.iterrows():
                        print(f"    {row['Group']}: g = {row['g']:.3f} [{row['CI_lower']:.3f}, {row['CI_upper']:.3f}], "
                              f"k={row['k']}, p={row['p']:.4f}{row['sig']}, I²={row['I2']:.1f}%")

    # -------------------------------------------------------------------------
    # 6. Create Visualizations
    # -------------------------------------------------------------------------
    print("\n[5] Creating visualizations...")

    # Forest plots for each comparison
    if len(results_h) > 0:
        plot_subgroup_forest(results_h, 'Human Augmentation', 'Figures/Subgroup_Forest_Human.png')

    if len(results_a) > 0:
        plot_subgroup_forest(results_a, 'AI Augmentation', 'Figures/Subgroup_Forest_AI.png')

    if len(results_s) > 0:
        plot_subgroup_forest(results_s, 'Strong Synergy', 'Figures/Subgroup_Forest_Synergy.png')

    # Bar charts for each moderator
    for mod in moderators:
        if mod in all_results['Moderator'].values:
            plot_moderator_comparison(all_results, mod, f'Figures/Subgroup_{mod}.png')

    # Summary heatmap
    create_summary_heatmap(all_results, 'Figures/Subgroup_Heatmap.png')

    # -------------------------------------------------------------------------
    # 7. Save Results
    # -------------------------------------------------------------------------
    print("\n[6] Saving results...")

    # Save detailed results
    all_results.to_csv('Data/Subgroup_All_Results.csv', index=False)
    results_h.to_csv('Data/Subgroup_Human_Augmentation.csv', index=False)
    results_a.to_csv('Data/Subgroup_AI_Augmentation.csv', index=False)
    results_s.to_csv('Data/Subgroup_Strong_Synergy.csv', index=False)

    # Save summary table
    summary = all_results.pivot_table(
        index=['Moderator', 'Group'],
        columns='Comparison',
        values=['g', 'p', 'k'],
        aggfunc='first'
    )
    summary.to_csv('Data/Subgroup_Summary_Pivot.csv')

    # Save data with effect sizes
    df.to_csv('Data/Data_with_EffectSizes.csv', index=False)

    print("\nFiles saved:")
    print("  - Data/Subgroup_All_Results.csv")
    print("  - Data/Subgroup_Human_Augmentation.csv")
    print("  - Data/Subgroup_AI_Augmentation.csv")
    print("  - Data/Subgroup_Strong_Synergy.csv")
    print("  - Data/Subgroup_Summary_Pivot.csv")
    print("  - Figures/Subgroup_*.png")

    # -------------------------------------------------------------------------
    # 8. Summary Report
    # -------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SUMMARY REPORT")
    print("=" * 70)

    print("\n📊 KEY FINDINGS BY MODERATOR:\n")

    # Find significant effects
    sig_results = all_results[all_results['p'] < 0.05]

    for mod in moderators:
        mod_sig = sig_results[sig_results['Moderator'] == mod]
        if len(mod_sig) > 0:
            print(f"  {mod}:")
            for _, row in mod_sig.iterrows():
                direction = "+" if row['g'] > 0 else "-"
                print(f"    • {row['Group']} ({row['Comparison']}): g = {direction}{abs(row['g']):.2f}{row['sig']}")
            print()

    print("=" * 70)
    print("ANALYSIS COMPLETE!")
    print("=" * 70)

    return df, all_results


if __name__ == "__main__":
    df, results = main()