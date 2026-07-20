"""
otrec_dropsondes
================
Visualisation library for OTREC dropsonde 3DVAR analysis data.

Public API
----------
generate_case_plots(case_id, data_dir, output_dir)
    Generate all available PDF plots for a single case.

process_all_cases(data_dir, output_dir)
    Generate plots for every registered case.
"""

from .plotting import generate_case_plots, process_all_cases

__all__ = ["generate_case_plots", "process_all_cases"]
__version__ = "0.1.0"
