# otrec-dropsondes

This repository contains a modular Python package designed to generate publication-quality, 3D-Var dropsonde data collected during the **OTREC (Organization of Tropical East Pacific Convection)** field campaign. 

## 📊 Data Source & Processing

The radar data used in this project originates from the OTREC field campaign. 
* **Raw Data Access:** Datasets can be downloaded from the [UCAR Earth Observing Laboratory (EOL) OTREC portal](https://www.eol.ucar.edu/field_projects/otrec).
* **Data Conversion:** The original data is provided in `.cdf` format. Before using this package, the files must be converted to standard NetCDF (`.nc`) format utilizing the **CANDIS** software suite, developed by David J. Raymond. Information and downloads for CANDIS can be found [here](https://kestrel.nmt.edu/~raymond/software/candis/candis.html).

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
