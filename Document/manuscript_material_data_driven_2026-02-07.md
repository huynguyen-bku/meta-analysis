# Manuscript Material (Data-Driven)

Source: `Analysis/outputs/tables/04_effect_sizes_full.csv`, `05_threelevel_meta_results.csv`, `06_publication_bias_summary.csv`, `08_subgroup_results.csv`
Date: February 7, 2026

## Results (Draft-Ready)
Across 278 effect sizes from 67 papers (90 experiments; 2020-2024), three-level meta-analysis showed negative strong synergy (g=-0.448, 95% CI [-0.664, -0.233], p<0.001), positive human augmentation (g=0.563, 95% CI [0.443, 0.682], p<0.001), and non-significant AI augmentation (g=0.058, 95% CI [-0.351, 0.467], p=0.780). Heterogeneity was high to extreme in all models (I2=91.3%-99.4%), with most variance at the between-experiment level for AI augmentation.

Moderator analyses indicated substantial context dependence. For strong synergy, task type strongly moderated effects (Create g=0.372 vs Decide g=-0.619; Q-between p<0.001). For AI augmentation, the largest subgroup contrasts were observed for AI type (range=2.192) and industry (range=1.743), with positive effects in Communication (g=1.011) and negative effects in Business (g=-0.732). For human augmentation, effects remained positive across all industries but varied in magnitude (highest in Business g=0.706; lowest in Communication g=0.276; Q-between p<0.001).

Publication bias diagnostics were significant across all comparisons (Egger and Begg tests, all p<0.001). Trim-and-fill analysis estimated 29 missing studies for strong synergy, 11 for human augmentation, and 14 for AI augmentation, suggesting that optimistic collaboration outcomes may be overrepresented in the observed literature.

## Discussion Points (Data-Grounded)
- The evidence supports asymmetric augmentation: AI helps humans consistently, but humans do not reliably improve AI.
- Collaboration is not universally beneficial; context (task, AI type, industry) changes effect direction and magnitude.
- The high heterogeneity profile means average effects alone are insufficient for deployment policy.
- Because publication asymmetry is systematic, conservative interpretation is warranted, especially for claims of strong synergy.

## Practical Implications
1. Use AI as decision support for humans when the objective is human augmentation.
2. Avoid assuming human oversight will improve AI performance by default.
3. Make deployment decisions using domain-specific validation rather than global averages.
4. Prioritize prospective monitoring in settings where subgroup effects switch sign (e.g., industry-sensitive use cases).

## Limitations to Report
- Very high heterogeneity (I2 > 90%) limits one-size-fits-all conclusions.
- Task imbalance (Decide 90.6% vs Create 9.4%) may underpower creative-task inferences.
- Many effect sizes are quality-flagged (78.8%), especially SD=0 patterns.
- Bias diagnostics indicate potential selective reporting.

## Suggested Next Analyses
1. Multivariable meta-regression with Industry + Task_Type + AI_Type_Cleaned.
2. Interaction tests (Industry x AI_Type_Cleaned; Task_Type x Participant_Expert).
3. Sensitivity analyses excluding extreme ES and SD=0 subsets.
4. Decision matrix mapping contexts to recommended human-AI operating mode.
