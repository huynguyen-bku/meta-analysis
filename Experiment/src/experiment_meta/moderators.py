"""Subgroup + moderator analysis — delegates to jabes_shared.

This module re-exports everything from jabes_shared.moderators so that
existing ``from experiment_meta.moderators import …`` statements keep working.
"""

from jabes_shared.moderators import (  # noqa: F401
    subgroup_analysis,
    run_all_moderators,
)
