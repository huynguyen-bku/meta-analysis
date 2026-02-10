"""Paths, constants, and moderator list.

Colour palette and comparison colours are imported from jabes_shared.
"""

import sys
from pathlib import Path

# ── Make jabes_shared importable ────────────────────────────────────
_META_ROOT = Path(__file__).resolve().parent.parent.parent.parent  # meta-analysis/
if str(_META_ROOT) not in sys.path:
    sys.path.insert(0, str(_META_ROOT))

# ── Re-export shared palette ────────────────────────────────────────
from jabes_shared.colors import COLORS, COMPARISON_COLORS  # noqa: E402, F401

# ── Paths ────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # Experiment/
DATA_DIR = PROJECT_ROOT / "data"
DATA_PATH = DATA_DIR / "Data_Extraction_communication_public.xlsx"

OUTPUT_DIR = PROJECT_ROOT / "outputs"
FIGURE_DIR = OUTPUT_DIR / "figures"
TABLE_DIR = OUTPUT_DIR / "tables"
REPORT_DIR = OUTPUT_DIR / "reports"

for _d in (FIGURE_DIR, TABLE_DIR, REPORT_DIR):
    _d.mkdir(parents=True, exist_ok=True)

# ── Effect-size column mapping ───────────────────────────────────────
# {comparison_key: (es_col, var_col)}
ES_COLS = {
    "synergy": ("es_s", "var_es_s"),
    "human_aug": ("es_h", "var_es_h"),
    "ai_aug": ("es_a", "var_es_a"),
}

COMPARISON_NAMES = {
    "synergy": "Strong Synergy",
    "human_aug": "Human Augmentation",
    "ai_aug": "AI Augmentation",
}

# ── Moderators ───────────────────────────────────────────────────────
MODERATORS = [
    "Industry",
    "Task_Type",
    "AI_Type_Cleaned",
    "Participant_Expert",
    "AI_Expl_Incl",
    "Year",
]
