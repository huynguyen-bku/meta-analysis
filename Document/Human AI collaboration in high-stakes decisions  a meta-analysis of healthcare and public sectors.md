Routledge
Taylor & Francis Group


Applied Economics Letters

ISSN: 1350-4851 (Print) 1466-4291 (Online) Journal homepage: www.tandfonline.com/journals/rael20

# Human–AI collaboration in high-stakes decisions: a meta-analysis of healthcare and public sectors

**Vu Minh Ngo**

**To cite this article:** Vu Minh Ngo (09 Nov 2025): Human–AI collaboration in high-stakes decisions: a meta-analysis of healthcare and public sectors, Applied Economics Letters, DOI: 10.1080/13504851.2025.2586160

**To link to this article:** [https://doi.org/10.1080/13504851.2025.2586160](https://doi.org/10.1080/13504851.2025.2586160)

*   View supplementary material
*   Published online: 09 Nov 2025.
*   Submit your article to this journal
*   Article views: 69
*   View related articles
*   View Crossmark data


Full Terms & Conditions of access and use can be found at
[https://www.tandfonline.com/action/journalInformation?journalCode=rael20](https://www.tandfonline.com/action/journalInformation?journalCode=rael20)

APPLIED ECONOMICS LETTERS
https://doi.org/10.1080/13504851.2025.2586160
Routledge - Taylor & Francis Group
Check for updates


# Human–AI collaboration in high-stakes decisions: a meta-analysis of healthcare and public sectors

Vu Minh Ngo (ID)
School of Banking, University of Economics Ho Chi Minh City, Ho Chi Minh City, Vietnam

> **ABSTRACT**
> This meta-analysis of 146 experiments in the healthcare and public sectors examines human–AI synergy versus augmentation amid substantial heterogeneity. We find that AI augmentation reliably improves human performance (Hedges’ g = 0.622), whereas synergy effects are generally negative, with AI alone often outperforming human–AI teams (Hedges’ g = −0.380), although publication bias favours positive augmentation results. Additionally, task type, AI transparency, and user expertise significantly moderate outcomes. These results caution against assuming inherent benefits of human–AI collaboration and instead support selective automation of structured tasks with human oversight for ethically complex decisions, guiding policymakers and leaders in optimizing human–AI integration.

**KEYWORDS**
Human–AI collaboration; healthcare; meta-analysis; public sectors

**JEL CLASSIFICATION**
I18; O33; O38

## I. Introduction

Artificial intelligence (AI) is increasingly deployed alongside human experts in high-stakes domains such as healthcare and public services (Esteva et al. 2019), where decisions carry significant societal consequences, including life-or-death outcomes. Consequently, there is an urgent need for reliable, accountable decision-making. Prevailing views suggest that AI should augment, rather than replace, human decision makers (Holzinger et al. 2019). Evidence on human–AI teamwork is mixed. A meta-analysis shows that hybrid pairs usually underperform stronger individual agents, so synergy is not automatic (Vaccaro, Almaatouq, and Malone 2024). Yet, when tasks are complex and complementary errors can be exploited – as in medical decisions (e.g. radiology or diagnosis) – well-designed collaborations beat both humans and models; human experts catch algorithmic misclassifications and vice versa (Freyer et al. 2024; Zöller et al. 2025). The decisive enablers are clear interfaces, transparency, and calibrated oversight that allow humans to interrogate and override AI when needed.

Governments are likewise deploying AI for unemployment risk screening, social benefit allocation, fraud detection, and regulatory enforcement (Van Noordt and Misuraca 2022). Efficiency gains are offset by high stakes: opacity undermines public trust, automation bias can entrench discrimination, and data leaks threaten privacy (Margetts 2022). Scholars therefore urge ‘responsibility by design’: governments must disclose model logic, keep humans liable for final decisions, and co-create systems with affected communities to embed fairness and human-rights safeguards across the AI lifecycle (Van Noordt and Misuraca 2022).

Given the inconsistent outcomes, critical gaps remain in our understanding of human–AI collaboration. Specifically, there is limited clarity about when – and how much – human–AI teams surpass individual capabilities. This meta-analysis addresses these gaps by evaluating studies within healthcare and public-sector contexts, asking: (1) Do humans and AI complement each other effectively? and (2) How significantly do human–AI teams outperform humans or AI alone?

## II. Methodology

Tasks, AI systems, user expertise, and outcomes vary widely across human–AI studies in healthcare and the public sector. Meta-analysis addresses this


**CONTACT** Vu Minh Ngo vunm@ueh.edu.vn School of Banking, University of Economics Ho Chi Minh City, 59C Nguyen Dinh Chieu Street, Ward 6, District 3, Ho Chi Minh City, Vietnam
Supplemental data for this article can be accessed online at https://doi.org/10.1080/13504851.2025.2586160
© 2025 Informa UK Limited, trading as Taylor & Francis Group

2 [icon] V. M. NGO


diversity by aggregating disparate experiments to estimate average synergy/augmentation effects, quantifying between-study variance, and testing moderators (task type, AI transparency, user expertise) that single studies cannot resolve. Building on Vaccaro, Almaatouq, and Malone (2024) but narrowing to high-stakes healthcare and public decisions, we add domain-specific tests for publication bias, heterogeneity, and task-level moderators.

Eligibility required the following: (1) experimental design; (2) human-only, AI-only, and joint conditions; (3) sufficient statistics for effect-size computation; (4) English publications between Jan-2020 and Jun-2024; and (5) clear descriptions of participants, tasks, and systems. We excluded observational designs, simulations without a joint condition, and papers lacking requisite data.

Searches of the ACM Digital Library, Web of Science, and backward/forward citations (strings in Appendix 2 in the online supplementary material) yielded 45 qualifying studies, enabling a sector-focused synthesis of when collaboration helps – and when it does not. From these, 43 healthcare/public-sector studies provided 146 experiments/effect sizes (Appendix 3). Outcomes were standardized as Hedges’ g for: (a) human–AI synergy (joint > both alone), (b) human augmentation (joint > human alone), and (c) AI augmentation (joint > AI alone). Definitions and computation details appear in Appendix 1.

We combined results (‘effects’) from many studies comparing a human with AI support versus a human without AI (or other relevant contrasts). Some papers reported several effects (e.g. multiple tasks, outcomes, or samples). Treating those effects as independent would overstate precision, so we modelled their dependence explicitly. Hedges’ g (a bias-corrected measure for the effect of meta-analysis given the small sample size) involves computing Cohen’s d (raw effect size for large samples) from pooled standard deviations, corrected for small samples bias to ensure accurate meta-analytic comparisons is as follows:

$$Cohen's d = \frac{\bar{X}_1 - \bar{X}_2}{SD_{pooled}}$$ (1)

$$Hedges' g = \left( 1 - \frac{3}{4(n_1 + n_2) - 9} \right) \times Cohen's d$$ (2)

We also assessed heterogeneity with the Q statistic which tests whether the observed variation exceeds what sampling error alone would predict) and the I<sup>2</sup> statistic (the percentage of total variation due to real differences across effects/studies). Pre-specified moderators – task type (create/decide), AI type (deep/shallow/Wizard-of-Oz), inclusion of explanations/confidence, participant expertise, output format, and design – were analysed via subgroup/meta-regression to explain variability and derive context-specific guidance for deployment.

## III. Analyses and results

### Bias test

Figure 1 (funnel plot) tests whether smaller studies report larger effects (publication bias). For human–AI synergy, the funnel is symmetric and the tests are nonsignificant (Egger’s $\beta = 0.158$, $p = 0.785$; rank-correlation $\tau = 0.02$, $p = 0.673$), suggesting

The image shows two funnel plots representing the distribution of effect sizes (Hedges' g) against their standard error.

**Left Plot: Strong Synergy: Human-AI System versus max(Human, AI)**
- The x-axis represents "Effect Size (Hedge's g)" ranging from -3.0 to 3.0.
- The y-axis represents "Standard Error" ranging from 0.00 to 1.20 (inverted scale).
- Data points are scattered around a central vertical line at approximately 0.0, mostly contained within a white triangular "funnel" area against a grey background.

**Right Plot: Weak Synergy: Human-AI System versus Human Alone**
- The x-axis represents "Effect Size (Hedge's g)" ranging from -2.0 to 3.0.
- The y-axis represents "Standard Error" ranging from 0.00 to 1.20 (inverted scale).
- Data points are clustered more densely around a central vertical line at approximately 0.5, with most points falling within the white triangular funnel.

Figure 1. Funnel plot of the Hedges’ g effect size.

APPLIED ECONOMICS LETTERS 3


representative estimates. For human augmentation, clear asymmetry emerges (Egger’s $\beta = 1.05$, $p = 0.006$; $\tau = 0.16$, $p = 0.002$), indicating studies reporting collaboration > human alone are more likely to be published. Thus, the literature likely overstates augmentation benefits. We do not apply formal bias corrections because such methods are unstable under substantial heterogeneity; instead, we report the observed pattern and interpret augmentation effects cautiously.

### Heterogeneity test

Table 1 presents the $I^2$ statistics, which measure the percentage of variability in effect sizes due to real differences between studies rather than chance. All three models – synergy, human augmentation, and AI augmentation – show very high heterogeneity (92–98%). For example, in the synergy model, $I^2 = 96.4\%$, meaning nearly all observed variation comes from actual contextual differences, such as task type, AI sophistication, or user expertise. Because of this, we use a random-effects model that allows the ‘true effect’ to vary across contexts.

Table 1 also reports the average standardized effect sizes (Hedges’ g). For synergy, the effect is negative ($-0.380$, $p < 0.01$), indicating that on average, teams of humans and AI perform worse than the better of the two working alone. For human augmentation, the effect is positive and large ($0.622$, $p < 0.01$), showing that AI assistance consistently improves human performance. In contrast, AI augmentation is small and not statistically significant ($-0.065$, $p > 0.1$), suggesting that adding human input does not reliably improve AI’s standalone performance.

Figure 2 Panel A (synergy), most points lie below zero, illustrating that many human–AI teams underperform relative to the better solo performer. In Panel B (augmentation), most points are above zero, confirming a consistent human performance boost when assisted by AI.

### Moderation analysis

Subgroup analyses tested the robustness of our main findings. Table 2 and Figure 3 explore why results vary. For example, synergy is less negative in creative tasks ($-0.18$) than in structured decision tasks ($-0.39$), suggesting more potential for complementarity in open-ended work. Human augmentation is strong across all contexts but especially high in creative tasks ($1.07$). AI sophistication also matters: deep-learning systems tend to yield better augmentation effects than shallow ones, though synergy still remains negative. Expertise plays a role too – synergy is closer to neutral with experts ($-0.25$) than non-experts ($-0.56$) (see Appendix 4). In addition, Appendix 5 presents scatterplots of effect sizes for accuracy-based decision tasks, showing human–AI synergy is more likely when humans outperform AI and rarer when AI is stronger.

## IV. Discussion and conclusion

Our meta-analysis shows that AI augmentation typically improves human performance, largely by reducing routine human error rather than by creating dependable human–AI ‘synergy’ (Binns et al. 2018). However, mixed teams often underperform the best solo agent – frequently the AI itself – and explanations rarely help because trust and reliance remain uncalibrated (Bansal et al. 2021). Effects are context-dependent, and task type matters: analytical, highly structured problems tend to favour AI dominance (Dietvorst, Simmons, and Massey 2018), whereas creative or ambiguous work leaves more scope for complementary strengths (Davenport and Harris 2005). User expertise also conditions gains; contrary to common assumptions, less experienced users do not automatically benefit more from AI support (Longoni, Bonezzi, and Morewedge 2019). These results emphasize the importance of design, not just adoption. Effective deployment of human–AI teams requires selecting tasks where error reduction yields

Table 1. Standardized effect sizes and heterogeneity test using random effects.
<table>
  <thead>
    <tr>
        <th>AI system</th>
        <th>Standardized effect size</th>
        <th>No. Effect size</th>
        <th colspan="2">95% CI</th>
        <th>t value</th>
        <th colspan="4">Heterogeneity test</th>
    </tr>
    <tr>
        <th></th>
        <th></th>
        <th></th>
        <th>lower limit</th>
        <th>upper limit</th>
        <th></th>
        <th>I²</th>
        <th>df</th>
        <th>Q value</th>
        <th>p value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Human-AI synergy</td>
        <td>-0.380***</td>
        <td>146</td>
        <td>-0.570</td>
        <td>-0.191</td>
        <td>-4.043</td>
        <td>96.4</td>
        <td>145</td>
        <td>2789</td>
        <td>0.000</td>
    </tr>
    <tr>
        <td>Human Augmentation</td>
        <td>0.622***</td>
        <td>146</td>
        <td>0.464</td>
        <td>0.780</td>
        <td>7.902</td>
        <td>92.7</td>
        <td>145</td>
        <td>1349</td>
        <td>0.000</td>
    </tr>
    <tr>
        <td>AI Augmentation</td>
        <td>-0.065</td>
        <td>146</td>
        <td>-0.336</td>
        <td>0.206</td>
        <td>-0.482</td>
        <td>98.4</td>
        <td>145</td>
        <td>4196</td>
        <td>0.000</td>
    </tr>
  </tbody>
</table>
Notes: *p < 0.1 **p < 0.05 ***p < 0.01.

4 V. M. NGO


### Panel A
#### Human-AI System versus max(Human, AI)

The forest plot in Panel A shows effect sizes (Hedge's g) for the Human-AI system compared to the best of either the human or AI alone.
- **The human-AI group underperforms either the human or AI alone (n = 88, 60.3%)**: Represented by the red shaded area where effect sizes are less than 0.
- **The human-AI group outperforms both the human and AI alone (n = 58, 39.7%)**: Represented by the green shaded area where effect sizes are greater than 0.

### Panel B
#### Human-AI System versus Human Alone

The forest plot in Panel B shows effect sizes (Hedge's g) for the Human-AI system compared to the human alone.
- **The human-AI group underperforms the human alone (n = 22, 15.1%)**: Represented by the red shaded area where effect sizes are less than 0.
- **The human-AI group outperforms the human alone (n = 124, 84.9%)**: Represented by the green shaded area where effect sizes are greater than 0.

Figure 2. Forest plots of all effect sizes (k = 146) included in the meta-analysis.

Table 2. Moderating test for different groups.

<table>
  <tbody>
    <tr>
        <td>Subgroup</td>
        <td>n</td>
        <td>Human-AI Synergy (Hedge's g)</td>
        <td>p-value</td>
        <td>AI Augmentation (Hedge's g)</td>
        <td>p-value</td>
        <td>Human Augmentation (Hedge's g)</td>
        <td>p-value</td>
    </tr>
    <tr>
        <td>*Type of Task</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Create</td>
        <td>8</td>
        <td>-0.18 [-0.3, -0.06]</td>
        <td>0.00</td>
        <td>1.07 [0.93, 1.21]</td>
        <td>0.00</td>
        <td>0.22 [0.19, 0.24]</td>
        <td>0.00</td>
    </tr>
    <tr>
        <td>Decide</td>
        <td>138</td>
        <td>-0.39 [-0.59, -0.19]</td>
        <td>0.00</td>
        <td>-0.12 [-0.39, 0.15]</td>
        <td>0.39</td>
        <td>0.64 [0.47, 0.8]</td>
        <td>0.00</td>
    </tr>
    <tr>
        <td>*AI Type</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Deep</td>
        <td>64</td>
        <td>-0.33 [-0.59, -0.07]</td>
        <td>0.02</td>
        <td>0.12 [-0.29, 0.54]</td>
        <td>0.56</td>
        <td>0.61 [0.44, 0.78]</td>
        <td>0.00</td>
    </tr>
    <tr>
        <td>Shallow</td>
        <td>46</td>
        <td>-0.39 [-0.61, -0.17]</td>
        <td>0.00</td>
        <td>-0.27 [-0.52, -0.02]</td>
        <td>0.03</td>
        <td>0.46 [0.17, 0.74]</td>
        <td>0.00</td>
    </tr>
    <tr>
        <td>Wizard of Oz</td>
        <td>36</td>
        <td>-0.5 [-1.11, 0.12]</td>
        <td>0.11</td>
        <td>-0.18 [-0.97, 0.62]</td>
        <td>0.66</td>
        <td>0.86 [0.42, 1.3]</td>
        <td>0.00</td>
    </tr>
    <tr>
        <td>*AI Explanation Included</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>No</td>
        <td>56</td>
        <td>-0.35 [-0.59, -0.1]</td>
        <td>0.01</td>
        <td>-0.06 [-0.42, 0.31]</td>
        <td>0.75</td>
        <td>0.6 [0.41, 0.79]</td>
        <td>0.00</td>
    </tr>
    <tr>
        <td>Yes</td>
        <td>90</td>
        <td>-0.4 [-0.62, -0.19]</td>
        <td>0.00</td>
        <td>-0.07 [-0.39, 0.25]</td>
        <td>0.67</td>
        <td>0.64 [0.46, 0.81]</td>
        <td>0.00</td>
    </tr>
    <tr>
        <td>*Expert Participants</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>No</td>
        <td>52</td>
        <td>-0.56 [-0.78, -0.34]</td>
        <td>0.00</td>
        <td>-0.33 [-0.68, 0.01]</td>
        <td>0.06</td>
        <td>0.6 [0.33, 0.87]</td>
        <td>0.00</td>
    </tr>
    <tr>
        <td>Yes</td>
        <td>94</td>
        <td>-0.25 [-0.52, 0.03]</td>
        <td>0.08</td>
        <td>0.12 [-0.25, 0.49]</td>
        <td>0.53</td>
        <td>0.64 [0.47, 0.81]</td>
        <td>0.00</td>
    </tr>
  </tbody>
</table>

measurable value, configuring interfaces that provide calibrated risk bands and disagreement alerts, and instituting procedures for escalation when AI predictions and human judgement diverge. Calibration training on base rates, controlled pilots, and ongoing monitoring are more promising than generic ‘explainability’ for fixing misuse and overreliance (Bansal et al. 2021; Wilson, Daugherty, and

APPLIED ECONOMICS LETTERS 5


<table>
  <thead>
    <tr>
        <th>*Type of Task</th>
        <th colspan="4"></th>
        <th colspan="3"></th>
    </tr>
    <tr>
        <th>*Task Output</th>
        <th colspan="4"></th>
        <th colspan="3"></th>
    </tr>
    <tr>
        <th>*Year</th>
        <th colspan="4"></th>
        <th colspan="3"></th>
    </tr>
    <tr>
        <th>*AI Type</th>
        <th colspan="4"></th>
        <th colspan="3"></th>
    </tr>
    <tr>
        <th>*AI Explanation Included</th>
        <th colspan="4"></th>
        <th colspan="3"></th>
    </tr>
    <tr>
        <th>*AI Confidence Included</th>
        <th colspan="4"></th>
        <th colspan="3"></th>
    </tr>
    <tr>
        <th>*Expert Participants</th>
        <th colspan="4"></th>
        <th colspan="3"></th>
    </tr>
    <tr>
        <th>*Crowdworker Participants</th>
        <th colspan="4"></th>
        <th colspan="3"></th>
    </tr>
    <tr>
        <th>*Experimental Design</th>
        <th colspan="4"></th>
        <th colspan="3"></th>
    </tr>
    <tr>
        <th>Scale</th>
        <th colspan="4"></th>
        <th>-1 -0.5 0 0.5 1</th>
        <th>-1 -0.5 0 0.5 1</th>
        <th>-1 -0.5 0 0.5 1</th>
    </tr>
    <tr>
        <th>Interpretation</th>
        <th colspan="4"></th>
        <th>No Synergy | Synergy</th>
        <th>No Synergy | Synergy</th>
        <th>No Synergy | Synergy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Sub.group</td>
        <td>n</td>
        <td>Strong Synergy<br/>HAI &gt; max(AI,H)</td>
        <td>Weak Synergy<br/>HAI &gt; A</td>
        <td>Weak Synergy<br/>HAI &gt; H</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>Create</td>
        <td>8</td>
        <td>-0.1</td>
        <td>1.1</td>
        <td>0.2</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>Decide</td>
        <td>138</td>
        <td>-0.4</td>
        <td>-0.1</td>
        <td>0.6</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>Binary</td>
        <td>61</td>
        <td>-0.4</td>
        <td>-0.2</td>
        <td>0.6</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>Categoric</td>
        <td>69</td>
        <td>-0.3</td>
        <td>0.0</td>
        <td>0.7</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>Numeric</td>
        <td>8</td>
        <td>-0.4</td>
        <td>-0.5</td>
        <td>0.8</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>Open Response</td>
        <td>8</td>
        <td>-0.2</td>
        <td>1.1</td>
        <td>0.2</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>2020</td>
        <td>25</td>
        <td>-0.6</td>
        <td>-0.5</td>
        <td>0.9</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>2021</td>
        <td>53</td>
        <td>-0.5</td>
        <td>-0.2</td>
        <td>0.4</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>2022</td>
        <td>24</td>
        <td>-0.3</td>
        <td>-0.1</td>
        <td>0.6</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>2023</td>
        <td>42</td>
        <td>0.1</td>
        <td>0.2</td>
        <td>0.9</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>2024</td>
        <td>2</td>
        <td>-0.7</td>
        <td>-0.7</td>
        <td>0.7</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>Deep</td>
        <td>64</td>
        <td>-0.3</td>
        <td>0.1</td>
        <td>0.6</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>Shallow</td>
        <td>46</td>
        <td>-0.4</td>
        <td>-0.3</td>
        <td>0.4</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>Wizard of Oz</td>
        <td>36</td>
        <td>-0.5</td>
        <td>-0.2</td>
        <td>0.9</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>No</td>
        <td>56</td>
        <td>-0.4</td>
        <td>-0.1</td>
        <td>0.6</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>Yes</td>
        <td>90</td>
        <td>-0.4</td>
        <td>-0.1</td>
        <td>0.7</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>No</td>
        <td>82</td>
        <td>-0.4</td>
        <td>-0.2</td>
        <td>0.7</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>Yes</td>
        <td>64</td>
        <td>-0.3</td>
        <td>0.1</td>
        <td>0.6</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>No</td>
        <td>52</td>
        <td>-0.5</td>
        <td>-0.3</td>
        <td>0.6</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>Yes</td>
        <td>94</td>
        <td>-0.2</td>
        <td>0.1</td>
        <td>0.7</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>No</td>
        <td>102</td>
        <td>-0.3</td>
        <td>0.0</td>
        <td>0.7</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>Yes</td>
        <td>44</td>
        <td>-0.5</td>
        <td>-0.3</td>
        <td>0.6</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>Dependent Samples</td>
        <td>107</td>
        <td>-0.3</td>
        <td>0.0</td>
        <td>0.6</td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td>Independent Samples</td>
        <td>39</td>
        <td>-0.4</td>
        <td>-0.3</td>
        <td>0.7</td>
        <td colspan="3"></td>
    </tr>
  </tbody>
</table>

Figure 3. Results from the meta-regression models for the moderator variables.

Davenport 2022). Accordingly, in healthcare and the public sector, it is prudent to automate high-precision, structured sub-tasks (e.g. triage prioritization and duplicate-record detection) while reserving ethically complex or ambiguous decisions for documented human review, where judgement, accountability, and stakeholder values are especially important (Binns et al. 2018; Wilson, Daugherty, and Davenport 2022).

We acknowledge limitations including high between-study heterogeneity, potential publication/selection bias (especially for augmentation), timeframe restrictions, reliance on reported summary statistics, the predominance of experimental settings, and the scarcity of open-ended studies (~5%), which limits generalizability beyond structured tasks and likely makes our pooled synergy a conservative lower bound for creative contexts. Because publication bias can inflate reported augmentation gains, agencies should mandate preregistered evaluations, routine reporting of null results, and independent audits, and researchers should use selection-model or p-curve sensitivity tests. Future studies should preregister field/simulation tests of creative, ambiguous high-stakes work; vary ambiguity and stakes; and assess appropriateness, novelty, justification quality, value

6 [logo] V. M. NGO


alignment, and downstream impact – not just accuracy.

### Author contributions

CRediT: **Vu Minh Ngo**: Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Resources, Software, Validation, Visualization, Writing – original draft.

### Disclosure statement

No potential conflict of interest was reported by the author(s).

### Funding

This study is funded by the University of Economics Ho Chi Minh City, Vietnam (UEH).

### ORCID

Vu Minh Ngo [orcid_logo] http://orcid.org/0000-0002-0997-4720

### References

Bansal, G., T. Wu, J. Zhou, R. Fok, B. Nushi, E. Kamar, and D. S. Weld. 2021. “Does the Whole Exceed Its Parts? The Effect of AI Explanations on Complementary Team Performance.” *ACM Transactions on Human-Computer Interaction* 28 (2): 1–24.

Binns, R., M. Veale, M. Van Kleek, and N. Shadbolt. 2018. “‘It’s Reducing a Human Being to a Percentage’: Perceptions of Justice in Algorithmic Decisions.” In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems (CHI ’18)*, edited by R. L. Mandryk, M. Hancock, M. Perry, and A. L. Cox, Article 377, 1–14. New York, NY, United States: Association for Computing Machinery.

Davenport, T. H., and J. G. Harris. 2005. “Automated decision making comes of age.” *MIT Sloan Management Review* 46 (4): 83.

Dietvorst, B. J., J. P. Simmons, and C. Massey. 2018. “Overcoming Algorithm Aversion: People Will Use Imperfect Algorithms If They Can (Even Slightly) Modify Them.” *Management Science* 64 (3): 1155–1170. https://doi.org/10.1287/mnsc.2016.2643.

Esteva, A., A. Robicquet, B. Ramsundar, V. Kuleshov, M. DePristo, K. Chou, C. Cui, G. Corrado, S. Thrun, and J. Dean. 2019. “A Guide to Deep Learning in Healthcare.” *Nature Medicine* 25 (1): 24–29. https://doi.org/10.1038/s41591-018-0316-z.

Freyer, O., I. C. Wiest, J. N. Kather, and S. Gilbert. 2024. “A Future Role for Health Applications of Large Language Models Depends on Regulators Enforcing Safety Standards.” *Lancet Digital Health* 6 (9): e662–e664. https://doi.org/10.1016/S2589-7500(24)00124-9.

Holzinger, A., G. Langs, H. Denk, K. Zatloukal, and H. Müller. 2019. “Causability and Explainability of Artificial Intelligence in Medicine.” *Wiley Interdisciplinary Reviews. Data Mining and Knowledge Discovery* 9 (4): e1312. https://doi.org/10.1002/widm.1312.

Longoni, C., A. Bonezzi, and C. K. Morewedge. 2019. “Resistance to Medical Artificial Intelligence.” *Journal of Consumer Research* 46 (4): 629–650. https://doi.org/10.1093/jcr/ucz013.

Margetts, H. 2022. “Rethinking AI for Good Governance.” *Daedalus* 151 (2): 360–371. https://doi.org/10.1162/daed_a_01922.

Vaccaro, M., A. Almaatouq, and T. Malone. 2024. “When Combinations of Humans and AI Are Useful: A Systematic Review and Meta-Analysis.” *Nature Human Behaviour* 8 (12): 2293–2303. https://doi.org/10.1038/s41562-024-02024-1.

Van Noordt, C., and G. Misuraca. 2022. “Artificial Intelligence for the Public Sector: Results of Landscaping the Use of AI in Government Across the European Union.” *Government Information Quarterly* 39 (3): 101714. https://doi.org/10.1016/j.giq.2022.101714.

Wilson, H. J., P. R. Daugherty, and T. H. Davenport. 2022. “The Future of AI Will Be About Less Data, Not More.” *Harvard Business Review* 100 (1): 114–123.

Zöller, N., J. Berger, I. Lin, N. Fu, J. Komarneni, G. Barabucci, K. Laskowski, V. Shia, B. Harack, E. A. Chu, and V. Trianni. 2025. “Human–AI Collectives Most Accurately Diagnose Clinical Vignettes.” *Proceedings of the National Academy of Sciences* 122 (24): e2426153122. https://doi.org/10.1073/pnas.2426153122.