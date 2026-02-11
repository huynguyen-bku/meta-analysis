"""Meta-analytic engines — delegates to jabes_shared.

This module re-exports everything from jabes_shared.meta_engine so that
existing ``from experiment_meta.meta_engine import …`` statements keep working.
"""

from jabes_shared.meta_engine import (  # noqa: F401
    MetaResult,
    random_effects_dl,
    fit_threelevel_reml,
)
