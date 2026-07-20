# otrec_dropsondes

Python library for visualising OTREC (Organisation of Tropical East Pacific Convection) dropsonde analysis data derived from the NCAR HCR W-band cloud radar campaign (August–October 2019).

## What is OTREC?

OTREC was a field campaign conducted in the tropical eastern Pacific and Caribbean during summer–autumn 2019. The campaign deployed dropsondes and the NCAR HCR W-band radar aboard the NSF/NCAR HIAPER Gulfstream V aircraft to study the organisation and thermodynamic environment of tropical convection. This library provides standardised plots for the 3DVAR-gridded dropsonde analysis (`merge-1.nc`) files produced for each research flight.

## Variables

Each `merge-1.nc` file contains the following key fields on a `(lon, lat, z)` grid:

| Variable | Description | Units |
|---|---|---|
| `u`, `v`, `w` | Wind components | m/s |
| `mflux` | Vertical mass flux | kg/m²/s |
| `mfluxlo`, `mfluxhi`, `mfluxvl`, `mfluxdif` | Mass flux layer integrals | kg/m²/s |
| `relvort`, `absvort` | Relative / absolute vorticity | ks⁻¹ |
| `ent`, `satent` | Entropy / saturated entropy | J/K/kg |
| `ii` | Instability index | J/K/kg |
| `dcin` | Downdraft convective inhibition | J/K/kg |
| `sfrac` | Saturation fraction | — |
| `sst` | Sea surface temperature | °C |
| `pres` | Pressure | hPa |
| `eflux`, `rtflux` | Surface energy fluxes | W/m² |
| `srcmr`, `srcent` | Moisture / entropy source terms | W/m² |

## Repository layout

```
otrec-dropsondes/
├── otrec_dropsondes/          # Python package
│   ├── __init__.py            # Public API
│   ├── plotting.py            # All plot functions
│   ├── _helpers.py            # Internal helpers (_squeeze_to_2d, _map_panel)
│   └── configs/               # One config file per case
│       ├── __init__.py
│       ├── config_0807.py     # RF01  — 2019-08-07
│       ├── config_0812.py     # RF03  — 2019-08-12
│       ├── config_0816.py     # RF04c — 2019-08-16
│       ├── config_0817.py     # RF05  — 2019-08-17
│       ├── config_0818.py     # RF06  — 2019-08-18
│       ├── config_0811.py     # RF02  — 2019-08-11
│       ├── config_0822.py     # RF07  — 2019-08-22
│       ├── config_0823.py     # RF08  — 2019-08-23
│       ├── config_0825.py     # RF09a — 2019-08-25
│       ├── config_0903.py     # RF10  — 2019-09-03
│       ├── config_0904.py     # RF11  — 2019-09-04
│       ├── config_0909.py     # RF12  — 2019-09-09
│       ├── config_0917.py     # RF13c — 2019-09-17
│       ├── config_0921.py     # RF14  — 2019-09-21
│       ├── config_0922.py     # RF15c — 2019-09-22
│       ├── config_0924.py     # RF16  — 2019-09-24
│       ├── config_0925.py     # RF17c — 2019-09-25
│       ├── config_0927.py     # RF18  — 2019-09-27
│       ├── config_0928.py     # RF19  — 2019-09-28
│       ├── config_0930.py     # RF20  — 2019-09-30
│       ├── config_1001.py     # RF21  — 2019-10-01
│       └── config_1002.py     # RF22  — 2019-10-02
├── notebooks/
│   └── example_1002.ipynb    # Example notebook for case 1002 (RF22)
├── data/                      # Place your merge-1.nc files here
│   └── 20191002/
│       └── box2/
│           └── merge-1.nc
├── README.md
└── requirements.txt
```

## Installation

```bash
git clone https://github.com/VALENTINAMOVILSANDOVAL/otrec-dropsondes.git
cd otrec-dropsondes
pip install -r requirements.txt
```

## Data

Place your `merge-1.nc` files under `data/` following the structure:

```
data/
└── yyyymmdd/
    └── boxN/
        └── merge-1.nc
```

## Usage

### From a Jupyter notebook

```python
import otrec_dropsondes

# Generate all plots for case 1002 (RF22, 2019-10-02)
otrec_dropsondes.generate_case_plots(
    case_id   = '1002',
    data_dir  = 'data',
    output_dir= 'plots'
)

# Generate plots for every available case
otrec_dropsondes.process_all_cases(
    data_dir  = 'data',
    output_dir= 'plots'
)
```

See `notebooks/example_1002.ipynb` for a full walkthrough.

## Cases

| case_id | Date | RF | Day |
|---|---|---|---|
| 0807 | 2019-08-07 | RF01 | 219 |
| 0811 | 2019-08-11 | RF02 | 223 |
| 0812 | 2019-08-12 | RF03 | 224 |
| 0816 | 2019-08-16 | RF04c | 228 |
| 0817 | 2019-08-17 | RF05 | 229 |
| 0818 | 2019-08-18 | RF06 | 230 |
| 0822 | 2019-08-22 | RF07 | — |
| 0823 | 2019-08-23 | RF08 | 235 |
| 0825 | 2019-08-25 | RF09a | 237 |
| 0903 | 2019-09-03 | RF10 | 246 |
| 0904 | 2019-09-04 | RF11 | 247 |
| 0909 | 2019-09-09 | RF12 | 252 |
| 0917 | 2019-09-17 | RF13c | 260 |
| 0921 | 2019-09-21 | RF14 | 264 |
| 0922 | 2019-09-22 | RF15c | 265 |
| 0924 | 2019-09-24 | RF16 | 267 |
| 0925 | 2019-09-25 | RF17c | 268 |
| 0927 | 2019-09-27 | RF18 | 270 |
| 0928 | 2019-09-28 | RF19 | 271 |
| 0930 | 2019-09-30 | RF20 | 273 |
| 1001 | 2019-10-01 | RF21 | 274 |
| 1002 | 2019-10-02 | RF22 | 275 |
