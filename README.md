# otrec-dropsondes

This repository contains a modular Python package designed to generate publication-quality diagnostic plots of dropsonde analysis data collected during the OTREC (Organization of Tropical East Pacific Convection) field campaign.
The tool pairs 3DVAR-gridded dropsonde data with thermodynamic and kinematic fields, applies case-specific spatial and vertical bounds, and exports high-resolution PDFs optimized for scientific journals.

## 📊 Data Source & Processing

The dropsonde data used in this project originates from the OTREC field campaign.

* Raw Data Access: Datasets can be downloaded from the [UCAR Earth Observing Laboratory (EOL) OTREC portal](https://www.eol.ucar.edu/field_projects/otrec).
* Data Processing: The original dropsonde data is processed and gridded using the CANDIS software suite, developed by David J. Raymond, which produces the 3DVAR analysis files (merge-1.nc) used by this package. Information and downloads for CANDIS can be found [here](https://kestrel.nmt.edu/~raymond/software/candis/candis.html).

## 📁 Package Architecture & Directory Structure

To ensure the package runs smoothly and discovers the datasets automatically, organize your local project directory as follows:

```text
otrec-wband-radar/
│
├── data/                       # Place your converted NetCDF files here
│   ├── hcr0811.nc
│   ├── hcr_surf0811.nc
│   ├── hcr0816.nc
│   ├── hcr_surf0816.nc
│   └── ...                     # (Any other paired cases)
│
├── plots/                      # Package automatically creates this folder for PDF outputs
│
├── otrec_radar/                # CORE PYTHON PACKAGE
│   ├── __init__.py             # Exposes core package functions
│   ├── config.py               # Pre-defined case configurations (bounds, titles, colormaps)
│   ├── get_available_cases.py  # Automated data folder scanning via regular expressions
│   ├── setup_plot_aesthetics.py# Matplotlib publication-quality style configuration
│   ├── generate_case_plots.py  # Main 3-panel plotting routine (single-case)
│   └── process_all_cases.py    # Batch processing orchestration routine
│
└── example.ipynb          # Jupyter Notebook to run the analysis
