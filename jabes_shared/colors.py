"""Canonical colour palette shared across Analysis and Experiment pipelines."""

COLORS = {
    # Comparison colours
    "synergy": "#C0392B",
    "human_aug": "#27AE60",
    "ai_aug": "#2980B9",
    # Significance / direction
    "sig": "#E67E22",
    "nonsig": "#95A5A6",
    "positive": "#27AE60",
    "negative": "#C0392B",
    "neutral": "#7F8C8D",
    # Structure
    "zero": "#555555",
    "grid": "#DDDDDD",
    "accent": "#2C3E50",
}

COMPARISON_COLORS = {
    "Strong Synergy": COLORS["synergy"],
    "Human Augmentation": COLORS["human_aug"],
    "AI Augmentation": COLORS["ai_aug"],
}
