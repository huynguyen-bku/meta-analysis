"""Shared plotting style and save helpers — publication ready.

Both Analysis/ and Experiment/ import from here.

Font strategy:
  - Serif body text: Noto Serif (full Vietnamese + Latin support)
  - Fallbacks: Liberation Serif (TNR-metric clone), DejaVu Serif
  - Panel labels (A, B, C): Noto Sans Bold (clean sans-serif)
  - Math: STIX (standard academic math font)
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Iterable

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from .colors import COLORS

logger = logging.getLogger(__name__)


# ── Font availability check ──────────────────────────────────────────

def _best_serif() -> list[str]:
    """Return ordered serif font list, verified against system fonts."""
    available = {f.name for f in fm.fontManager.ttflist}
    preferred = [
        "Noto Serif",           # Google serif, full Vietnamese
        "Liberation Serif",     # Times New Roman metric-compatible
        "DejaVu Serif",         # Wide Unicode, always available in mpl
    ]
    found = [f for f in preferred if f in available]
    if found:
        logger.debug("Serif font chain: %s", found)
    return found or ["DejaVu Serif"]


def _best_sans() -> list[str]:
    """Return ordered sans font list for panel labels."""
    available = {f.name for f in fm.fontManager.ttflist}
    preferred = [
        "Noto Sans",
        "Liberation Sans",
        "DejaVu Sans",
    ]
    return [f for f in preferred if f in available] or ["DejaVu Sans"]


# ── Plot style ─────────────────────────────────────────────────────────

def apply_plot_style(mode: str = "publication") -> None:
    """Apply a consistent plotting style.

    Parameters
    ----------
    mode : str
        ``"publication"`` — Noto Serif, 600 DPI, STIX math (papers).
        ``"eda"`` — sans-serif, 350 DPI (exploratory notebooks).
    """
    # Clear font cache to avoid stale entries
    matplotlib.rcdefaults()

    if mode == "eda":
        sans = _best_sans()
        plt.rcParams.update({
            "font.family": "sans-serif",
            "font.sans-serif": sans,
            "font.size": 9,
            "axes.labelsize": 10,
            "axes.titlesize": 11,
            "axes.titleweight": "bold",
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "figure.dpi": 350,
            "savefig.dpi": 350,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.08,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.25,
            "grid.linestyle": "-",
            "grid.linewidth": 0.5,
            "grid.color": "#CFCFCF",
        })
        return

    # ── Publication mode ──
    serif = _best_serif()
    plt.rcParams.update({
        # Typography
        "font.family": "serif",
        "font.serif": serif,
        "font.size": 11,
        "mathtext.fontset": "stix",

        # Axes labels & titles
        "axes.labelsize": 12,
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "axes.titlepad": 10,

        # Tick labels
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.major.size": 4,
        "ytick.major.size": 4,
        "xtick.minor.size": 2,
        "ytick.minor.size": 2,
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,

        # Legend
        "legend.fontsize": 9,
        "legend.title_fontsize": 10,
        "legend.frameon": True,
        "legend.framealpha": 0.9,
        "legend.edgecolor": "#CCCCCC",
        "legend.fancybox": False,
        "legend.borderpad": 0.5,

        # Figure
        "figure.titlesize": 14,
        "figure.titleweight": "bold",
        "figure.dpi": 150,
        "figure.facecolor": "white",
        "figure.edgecolor": "none",
        "figure.constrained_layout.use": False,

        # Save
        "savefig.dpi": 600,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.15,
        "savefig.facecolor": "white",
        "savefig.edgecolor": "none",

        # Axes frame
        "axes.linewidth": 0.7,
        "axes.edgecolor": "#333333",
        "axes.labelcolor": "#1a1a1a",
        "axes.facecolor": "white",
        "axes.spines.top": False,
        "axes.spines.right": False,

        # Grid
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.alpha": 0.15,
        "grid.linestyle": "-",
        "grid.linewidth": 0.4,
        "grid.color": "#D9D9D9",

        # Colours
        "xtick.color": "#333333",
        "ytick.color": "#333333",
        "text.color": "#1a1a1a",

        # Lines
        "lines.linewidth": 1.5,
        "lines.markersize": 5,
        "patch.linewidth": 0.5,

        # Unicode: use ASCII hyphen-minus instead of U+2212 MINUS SIGN
        "axes.unicode_minus": False,

        # Hatch (for bar patterns)
        "hatch.linewidth": 0.5,
    })


# ── Save helper ────────────────────────────────────────────────────────

def save_figure(fig, base_path: Path, formats: Iterable[str] = ("png", "pdf"),
                facecolor: str = "white") -> None:
    """Save figure as PNG + PDF at 600 DPI."""
    base_path = Path(base_path)
    base_path.parent.mkdir(parents=True, exist_ok=True)
    stem = base_path.with_suffix("")
    for ext in formats:
        fig.savefig(stem.with_suffix(f".{ext}"),
                    dpi=600, bbox_inches="tight",
                    facecolor=facecolor, edgecolor="none")
    plt.close(fig)
    names = ", ".join(f"{stem.name}.{e}" for e in formats)
    print(f"  Saved: {names}")


# ── Annotation helpers ────────────────────────────────────────────────

def add_panel_label(ax, label: str, x: float = -0.08, y: float = 1.03,
                    fontsize: int = 16) -> None:
    """Add bold panel label (A, B, C, …) in sans-serif."""
    sans = _best_sans()
    ax.text(x, y, label, transform=ax.transAxes,
            fontsize=fontsize, fontweight="bold", va="top", ha="left",
            fontfamily=sans[0])


def add_zero_line(ax, orientation: str = "v") -> None:
    """Add zero reference line."""
    kw = dict(color=COLORS["zero"], linewidth=0.8, linestyle="-", alpha=0.5, zorder=0)
    if orientation == "v":
        ax.axvline(0, **kw)
    else:
        ax.axhline(0, **kw)


def sig_stars(p) -> str:
    """Return significance stars for a p-value."""
    if p < 0.001:
        return "***"
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    return "ns"
