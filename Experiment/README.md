# Experiment — Meta-Analysis: Human-AI Collaboration

Pipeline phân tích meta cho nghiên cứu cộng tác Người-AI.

## Cấu trúc

```
Experiment/
├── data/                     # Excel nguồn
├── src/
│   ├── experiment_meta/      # Shared package (effect sizes, meta-engine, bias, …)
│   ├── 01–06_*.py            # Analysis scripts
│   ├── 10–14_*.py            # Publication figure scripts
│   └── run_pipeline.py       # Orchestrator
├── outputs/
│   ├── figures/              # PNG + PDF (600 DPI)
│   ├── tables/               # CSV results
│   └── reports/              # Markdown insights
├── notebooks/                # Archived Jupyter notebooks
└── archive/                  # Old Python scripts
```

## Chạy pipeline

```bash
cd Experiment/src
python run_pipeline.py              # Chạy tất cả
python run_pipeline.py --analysis   # Chỉ analysis (01–06)
python run_pipeline.py --figures    # Chỉ figures (10–14)
```

## Yêu cầu

- Python 3.9+
- R với packages: `metafor`, `clubSandwich` (cho 3-level REML)
- Python packages: xem `requirements.txt`

```bash
pip install -r requirements.txt
```

## So sánh chính (3 comparisons)

| Comparison | Ký hiệu | Ý nghĩa |
|---|---|---|
| Strong Synergy | es_s | HAI vs max(Human, AI) |
| Human Augmentation | es_h | HAI vs Human alone |
| AI Augmentation | es_a | HAI vs AI alone |

## Outputs chính

- `02_meta_results.csv` — Pooled estimates (3-level REML)
- `03_bias_summary.csv` — Egger, Begg, trim-and-fill, fail-safe N
- `04_subgroup_results.csv` — Moderator analysis with Q-between
- `Figure1–4` — 4 publication figures (PNG + PDF, 600 DPI)
- `FigureS1–S3` — Supplementary figures
