"""Case 0818 — RF06, day 230, box3"""
CASE = {
    "iisf": {
        "p_ii":    {"variable": "ii",    "title": "RF06, day 230, instab index (J/K/kg)", "x_axis": {"label": "longitude (deg)", "limits": [-95, -89]}, "y_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "color_bar": {"ticks": [5, 10, 15, 20, 25, 30, 35, 40]}},
        "p_sfrac": {"variable": "sfrac", "title": "RF06, day 230, satfrac",               "x_axis": {"label": "longitude (deg)", "limits": [-95, -89]}, "y_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "color_bar": {"ticks": [0.69, 0.72, 0.75, 0.78, 0.81, 0.84]}}
    },
    "ppiplot": {
        "p_srcmr": {"variable": "srcmr", "title": "RF06: moisture conv (W/m$^2$, r/b); Track (y)", "x_axis": {"label": "longitude (deg)", "limits": [-95, -89]}, "y_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "color_bar": {"ticks": [-1000, -500, 0, 500, 1000, 1500, 2000]}}
    },
    "latplot": {
        "p_mflux": {"variable": "mflux", "title": "mfluxhi / mfluxlo",   "x_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "y_axis": {"label": "mflux (kg/m$^2$/s)",   "limits": [-0.06, 0.12]}},
        "p_sst":   {"variable": "sst",   "title": "SST (C)",              "x_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "y_axis": {"label": "SST (C)",             "limits": [26, 30]}},
        "p_eflux": {"variable": "eflux", "title": "surf flux (W/m$^2$)", "x_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "y_axis": {"label": "surf flux (W/m$^2$)", "limits": [0, 600]}},
        "p_ii":    {"variable": "ii",    "title": "ii, dcin (J/K/kg)",   "x_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "y_axis": {"label": "ii, dcin (J/K/kg)",   "limits": [-20, 40]}},
        "p_srcmr": {"variable": "srcmr", "title": "sources (W/m$^2$)",   "x_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "y_axis": {"label": "sources (W/m$^2$)",   "limits": [-2000, 3000]}},
        "p_sfrac": {"variable": "sfrac", "title": "sat frac",            "x_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "y_axis": {"label": "sat frac",            "limits": [0.5, 1.0]}}
    },
    "zlatplot": {
        "p_mflux": {"variable": "mflux", "title": "L: mass flux (kg/m$^2$/s); R: zonal wind (m/s)", "x_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "y_axis": {"label": "height (km)", "limits": [0, 14]}, "color_bar_left": {"ticks": [-0.02, 0, 0.02, 0.04, 0.06, 0.08, 0.1]}, "color_bar_right": {"ticks": [-20, -16, -12, -8, -4, 0, 4, 8, 12]}}
    },
    "vort": {
        "p_relvort": {"variable": "relvort", "title": "RF06, day 230, relvort 1.5 km (ks$^{-1}$)",        "x_axis": {"label": "longitude (deg)", "limits": [-95, -89]}, "y_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "color_bar": {"ticks": [-0.05, -0.025, 0, 0.025, 0.05, 0.075, 0.1]}},
        "p_absvort": {"variable": "relvort", "title": "winds 20 m/s per deg, relvort 4.0 km (ks$^{-1}$)", "x_axis": {"label": "longitude (deg)", "limits": [-95, -89]}, "y_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "color_bar": {"ticks": [-0.05, -0.025, 0, 0.025, 0.05, 0.075, 0.1]}}
    },
    "surf": {
        "p_dcin":  {"variable": "dcin",  "title": "RF06, day 230, dcin, (J/K/kg)",  "x_axis": {"label": "longitude (deg)", "limits": [-95, -89]}, "y_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "color_bar": {"ticks": [-20, -10, 0, 10, 20, 30, 40, 50, 60]}},
        "p_eflux": {"variable": "eflux", "title": "RF06, day 230, eflux (W/m$^2$)", "x_axis": {"label": "longitude (deg)", "limits": [-95, -89]}, "y_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "color_bar": {"ticks": [0, 50, 100, 150, 200, 250, 300]}}
    },
    "sst_wind": {
        "p_sst":  {"variable": "sst",  "title": "RF06, day 230, SST (C)",                     "x_axis": {"label": "longitude (deg)", "limits": [-95, -89]}, "y_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "color_bar": {"ticks": [26, 26.5, 27, 27.5, 28, 28.5, 29, 29.5, 30]}},
        "p_pres": {"variable": "pres", "title": "BL winds 20 m/s per deg, surf pres (hPa)", "x_axis": {"label": "longitude (deg)", "limits": [-95, -89]}, "y_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "color_bar": {"ticks": [997.5, 998, 998.5, 999, 999.5, 1000, 1000.5, 1001]}}
    },
    "src": {
        "p_srcmr":  {"variable": "srcmr",  "title": "RF06, day 230, srcmr, (W/m$^2$)", "x_axis": {"label": "longitude (deg)", "limits": [-95, -89]}, "y_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "color_bar": {"ticks": [-2000, -1500, -1000, -500, 0, 500, 1000, 1500, 2000]}},
        "p_srcent": {"variable": "srcent", "title": "RF06, day 230, srcent (W/m$^2$)",  "x_axis": {"label": "longitude (deg)", "limits": [-95, -89]}, "y_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "color_bar": {"ticks": [-500, 0, 500, 1000, 1500, 2000]}}
    },
    "sndplot": {
        "p_ent": {"variable": "ent", "title": "RF06: 3DVAR (-93, 10) - entropy / sat ent", "x_axis": {"label": "entropy (J/K/kg)",  "limits": [200, 320], "ticks": [200, 240, 280, 320]}, "y_axis": {"label": "height (km)", "limits": [0, 14]}},
        "p_u":   {"variable": "u",   "title": "RF06: 3DVAR (-93, 10) - U wind / V wind",   "x_axis": {"label": "U, V wind (m/s)", "limits": [-12, 12], "ticks": [-12, -8, -4, 0, 4, 8, 12]}, "y_axis": {"label": "height (km)", "limits": [0, 14]}}
    },
    "profs": {
        "p_ent":   {"variable": "ent",   "title": "RF06, day 230 - entropy, sat entropy (J/K/kg)", "x_axis": {"label": "entropy, sat entropy (J/K/kg)", "limits": [180, 320], "ticks": [180, 200, 220, 240, 260, 280, 300, 320]}, "y_axis": {"label": "height (km)", "limits": [0, 16]}},
        "p_mflux": {"variable": "mflux", "title": "RF06, day 230 - mass flux (kg/m$^2$/s)",       "x_axis": {"label": "mass flux (kg/m$^2$/s)",        "limits": [-0.04, 0.08], "ticks": [-0.04, -0.02, 0, 0.02, 0.04, 0.06, 0.08]}, "y_axis": {"label": "height (km)", "limits": [0, 16]}}
    },
    "mfluxplot": {
        "p_mflux": {"variable": "mflux", "title": "RF06: 3DVAR (-93, 10) - mass flux (kg/m$^2$/s)",      "x_axis": {"label": "mass flux (kg/m$^2$/s)",      "limits": [-0.02, 0.06], "ticks": [-0.02, 0, 0.02, 0.04, 0.06]}, "y_axis": {"label": "height (km)", "limits": [0, 14]}},
        "p_w":     {"variable": "w",     "title": "RF06: 3DVAR (-93, 10) - HCR vertical velocity (m/s)", "x_axis": {"label": "HCR vertical velocity (m/s)", "limits": [-4, 1],     "ticks": [-4, -3, -2, -1, 0, 1]},     "y_axis": {"label": "height (km)", "limits": [0, 14]}}
    },
    "mflux": {
        "p_mfluxlo":  {"variable": "mfluxlo",  "title": "RF06, day 230, mfluxlo (kg/m$^2$/s)",  "x_axis": {"label": "longitude (deg)", "limits": [-95, -89]}, "y_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "color_bar": {"ticks": [-0.08, -0.06, -0.04, -0.02, 0, 0.02, 0.04, 0.06, 0.08]}},
        "p_mfluxhi":  {"variable": "mfluxhi",  "title": "RF06, day 230, mfluxhi (kg/m$^2$/s)",  "x_axis": {"label": "longitude (deg)", "limits": [-95, -89]}, "y_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "color_bar": {"ticks": [-0.08, -0.06, -0.04, -0.02, 0, 0.02, 0.04, 0.06, 0.08]}},
        "p_mfluxvl":  {"variable": "mfluxvl",  "title": "RF06, day 230, mfluxvl (kg/m$^2$/s)",  "x_axis": {"label": "longitude (deg)", "limits": [-95, -89]}, "y_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "color_bar": {"ticks": [-0.08, -0.06, -0.04, -0.02, 0, 0.02, 0.04, 0.06, 0.08]}},
        "p_mfluxdif": {"variable": "mfluxdif", "title": "RF06, day 230, mfluxdif (kg/m$^2$/s)", "x_axis": {"label": "longitude (deg)", "limits": [-95, -89]}, "y_axis": {"label": "latitude (deg)", "limits": [7, 13]}, "color_bar": {"ticks": [-0.08, -0.06, -0.04, -0.02, 0, 0.02, 0.04, 0.06, 0.08]}}
    }
}
