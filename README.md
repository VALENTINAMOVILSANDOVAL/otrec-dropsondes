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
otrec-dropsondes/
│
├── data/                         # Place your converted NetCDF files here
│   └── yyyymmdd/                 # One folder per case date (e.g. 20191002)
│       └── boxN/                 # Box subdirectory (e.g. box1, box2, box3)
│           └── merge-1.nc        # 3DVAR gridded dropsonde analysis file
│
├── otrec_dropsondes/             # CORE PYTHON PACKAGE
│   ├── __init__.py               # Exposes core package functions
│   ├── _helpers.py               # Internal helpers (_squeeze_to_2d, _map_panel, rcParams)
│   ├── plotting.py               # All diagnostic plot functions + batch processing
│   ├── README.md                 # This file
│   └── configs/                  # Pre-defined case configurations (bounds, titles, colormaps)
│       ├── __init__.py
│       ├── config_0807.py        # RF01 — 2019-08-07
│       ├── config_0811.py        # RF02 — 2019-08-11
│       ├── config_0812.py        # RF03 — 2019-08-12
│       ├── config_0816.py        # RF04c — 2019-08-16
│       ├── config_0817.py        # RF05 — 2019-08-17
│       ├── config_0818.py        # RF06 — 2019-08-18
│       ├── config_0822.py        # RF07 — 2019-08-22
│       ├── config_0823.py        # RF08 — 2019-08-23
│       ├── config_0825.py        # RF09a — 2019-08-25
│       ├── config_0903.py        # RF10 — 2019-09-03
│       ├── config_0904.py        # RF11 — 2019-09-04
│       ├── config_0909.py        # RF12 — 2019-09-09
│       ├── config_0917.py        # RF13c — 2019-09-17
│       ├── config_0921.py        # RF14 — 2019-09-21
│       ├── config_0922.py        # RF15c — 2019-09-22
│       ├── config_0924.py        # RF16 — 2019-09-24
│       ├── config_0925.py        # RF17c — 2019-09-25
│       ├── config_0927.py        # RF18 — 2019-09-27
│       ├── config_0928.py        # RF19 — 2019-09-28
│       ├── config_0930.py        # RF20 — 2019-09-30
│       ├── config_1001.py        # RF21 — 2019-10-01
│       └── config_1002.py        # RF22 — 2019-10-02
