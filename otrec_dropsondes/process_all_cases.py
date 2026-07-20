# otrec_dropsondes/process_all_cases.py

from .generate_case_plots import generate_case_plots, _CASE_REGISTRY
import warnings

def process_all_cases(data_dir: str = './data', output_dir: str = './plots'):
    """Generate plots for every registered OTREC case."""
    for case_id in sorted(_CASE_REGISTRY.keys()):
        try:
            generate_case_plots(case_id, data_dir=data_dir, output_dir=output_dir)
        except FileNotFoundError as exc:
            warnings.warn(str(exc))
