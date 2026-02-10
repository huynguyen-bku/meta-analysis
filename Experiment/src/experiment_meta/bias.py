"""Publication bias assessment — delegates to jabes_shared.

This module re-exports everything from jabes_shared.bias so that
existing ``from experiment_meta.bias import …`` statements keep working.
"""

from jabes_shared.bias import (  # noqa: F401
    eggers_test,
    begg_test,
    trim_and_fill,
    failsafe_n,
    run_all_bias_tests,
)
