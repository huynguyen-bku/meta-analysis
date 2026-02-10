"""Effect size computation — delegates to jabes_shared.

This module re-exports everything from jabes_shared.effect_sizes so that
existing ``from experiment_meta.effect_sizes import …`` statements keep working.
"""

from jabes_shared.effect_sizes import (  # noqa: F401
    compute_hedges_g,
    compute_all_effect_sizes,
    flag_edge_cases,
)
