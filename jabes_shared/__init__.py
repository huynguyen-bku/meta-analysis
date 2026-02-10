"""JABES shared utilities for meta-analysis pipelines (Analysis + Experiment).

Provides:
  - colors: canonical colour palette
  - visuals: plotting style, save helpers, annotation
  - insights: manuscript insight logging
  - meta_engine: DL random-effects + 3-level REML
  - effect_sizes: Hedges' g computation
  - bias: Egger, Begg, trim-and-fill, fail-safe N
  - moderators: subgroup analysis + Q-between
  - sensitivity: leave-one-out, cumulative, influence, outliers
"""

__all__ = ["__version__"]
__version__ = "0.3.0"
