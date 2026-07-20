"""Case 0904 — RF11, day 247, box2"""
CASE = {
    "iisf": {
        "p_ii":    {"variable": "ii",    "title": "RF11, day 247, instab index (J/K/kg)", "x_axis": {"label": "longitude (deg)", "limits": [-89, -86]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "color_bar": {"ticks": [5, 10, 15, 20, 25, 30, 35, 40]}},
        "p_sfrac": {"variable": "sfrac", "title": "RF11, day 247, satfrac",               "x_axis": {"label": "longitude (deg)", "limits": [-89, -86]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "color_bar": {"ticks": [0.69, 0.72, 0.75, 0.78, 0.81, 0.84]}}
    },
    "ppiplot": {
        "p_srcmr": {"variable": "srcmr", "title": "RF11: moisture conv (W/m$^2$, r/b); Track (y)", "x_axis": {"label": "longitude (deg)", "limits": [-90, -85]}, "y_axis": {"label": "latitude (deg)", "limits": [2, 12]}, "color_bar": {"ticks": [-1000, -500, 0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000]}}
    },
    "latplot": {
        "p_mflux": {"variable": "mflux", "title": "mfluxhi / mfluxlo",   "x_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "y_axis": {"label": "mflux (kg/m$^2$/s)",   "limits": [-0.06, 0.12]}},
        "p_sst":   {"variable": "sst",   "title": "SST (C)",              "x_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "y_axis": {"label": "SST (C)",             "limits": [26, 30]}},
        "p_eflux": {"variable": "eflux", "title": "surf flux (W/m$^2$)", "x_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "y_axis": {"label": "surf flux (W/m$^2$)", "limits": [0, 600]}},
        "p_ii":    {"variable": "ii",    "title": "ii, dcin (J/K/kg)",   "x_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "y_axis": {"label": "ii, dcin (J/K/kg)",   "limits": [-20, 40]}},
        "p_srcmr": {"variable": "srcmr", "title": "sources (W/m$^2$)",   "x_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "y_axis": {"label": "sources (W/m$^2$)",   "limits": [-2000, 3000]}},
        "p_sfrac": {"variable": "sfrac", "title": "sat frac",            "x_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "y_axis": {"label": "sat frac",            "limits": [0.5, 1.0]}}
    },
    "zlatplot": {
        "p_mflux": {"variable": "mflux", "title": "L: mass flux (kg/m$^2$/s); R: zonal wind (m/s)", "x_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "y_axis": {"label": "height (km)", "limits": [0, 14]}, "color_bar_left": {"ticks": [-0.02, 0, 0.02, 0.04, 0.06, 0.08, 0.1]}, "color_bar_right": {"ticks": [-20, -16, -12, -8, -4, 0, 4, 8, 12]}}
    },
    "vort": {
        "p_relvort": {"variable": "relvort", "title": "RF11, day 247, relvort 1.5 km (ks$^{-1}$)",        "x_axis": {"label": "longitude (deg)", "limits": [-89, -86]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "color_bar": {"ticks": [-0.05, -0.025, 0, 0.025, 0.05, 0.075, 0.1]}},
        "p_absvort": {"variable": "relvort", "title": "winds 20 m/s per deg, relvort 4.0 km (ks$^{-1}$)", "x_axis": {"label": "longitude (deg)", "limits": [-89, -86]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "color_bar": {"ticks": [-0.05, -0.025, 0, 0.025, 0.05, 0.075, 0.1]}}
    },
    "surf": {
        "p_dcin":  {"variable": "dcin",  "title": "RF11, day 247, dcin, (J/K/kg)",  "x_axis": {"label": "longitude (deg)", "limits": [-89, -86]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "color_bar": {"ticks": [-20, -10, 0, 10, 20, 30, 40, 50, 60]}},
        "p_eflux": {"variable": "eflux", "title": "RF11, day 247, eflux (W/m$^2$)", "x_axis": {"label": "longitude (deg)", "limits": [-89, -86]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "color_bar": {"ticks": [0, 50, 100, 150, 200, 250, 300]}}
    },
    "sst_wind": {
        "p_sst":  {"variable": "sst",  "title": "RF11, day 247, SST (C)",                     "x_axis": {"label": "longitude (deg)", "limits": [-89, -86]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "color_bar": {"ticks": [26, 26.5, 27, 27.5, 28, 28.5, 29, 29.5, 30]}},
        "p_pres": {"variable": "pres", "title": "BL winds 20 m/s per deg, surf pres (hPa)", "x_axis": {"label": "longitude (deg)", "limits": [-89, -86]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "color_bar": {"ticks": [999, 999.5, 1000, 1000.5, 1001, 1001.5]}}
    },
    "src": {
        "p_srcmr":  {"variable": "srcmr",  "title": "RF11, day 247, srcmr, (W/m$^2$)", "x_axis": {"label": "longitude (deg)", "limits": [-89, -86]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "color_bar": {"ticks": [-2000, -1500, -1000, -500, 0, 500, 1000, 1500, 2000]}},
        "p_srcent": {"variable": "srcent", "title": "RF11, day 247, srcent (W/m$^2$)",  "x_axis": {"label": "longitude (deg)", "limits": [-89, -86]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "color_bar": {"ticks": [-500, 0, 500, 1000, 1500, 2000]}}
    },
    "sndplot": {
        "p_ent": {"variable": "ent", "title": "RF11: 3DVAR (-89.0, 6.0) - entropy / sat ent", "x_axis": {"label": "entropy (J/K/kg)",  "limits": [200, 320], "ticks": [200, 240, 280, 320]}, "y_axis": {"label": "height (km)", "limits": [0, 14]}},
        "p_u":   {"variable": "u",   "title": "RF11: 3DVAR (-89.0, 6.0) - U wind / V wind",   "x_axis": {"label": "U, V wind (m/s)", "limits": [-12, 8], "ticks": [-12, -8, -4, 0, 4, 8]}, "y_axis": {"label": "height (km)", "limits": [0, 14]}}
    },
    "profs": {
        "p_ent":   {"variable": "ent",   "title": "RF11, day 247 - entropy, sat entropy (J/K/kg)", "x_axis": {"label": "entropy, sat entropy (J/K/kg)", "limits": [180, 320], "ticks": [180, 200, 220, 240, 260, 280, 300, 320]}, "y_axis": {"label": "height (km)", "limits": [0, 16]}},
        "p_mflux": {"variable": "mflux", "title": "RF11, day 247 - mass flux (kg/m$^2$/s)",       "x_axis": {"label": "mass flux (kg/m$^2$/s)",        "limits": [-0.04, 0.08], "ticks": [-0.04, -0.02, 0, 0.02, 0.04, 0.06, 0.08]}, "y_axis": {"label": "height (km)", "limits": [0, 16]}}
    },
    "mfluxplot": {
        "p_mflux": {"variable": "mflux", "title": "RF11: 3DVAR (-89.0, 6.0) - mass flux (kg/m$^2$/s)",      "x_axis": {"label": "mass flux (kg/m$^2$/s)",      "limits": [-0.04, 0.16], "ticks": [-0.04, 0, 0.04, 0.08, 0.12, 0.16]}, "y_axis": {"label": "height (km)", "limits": [0, 14]}},
        "p_w":     {"variable": "w",     "title": "RF11: 3DVAR (-89.0, 6.0) - HCR vertical velocity (m/s)", "x_axis": {"label": "HCR vertical velocity (m/s)", "limits": [-6, 0],     "ticks": [-6, -5, -4, -3, -2, -1, 0]},     "y_axis": {"label": "height (km)", "limits": [0, 14]}}
    },
    "mflux": {
        "p_mfluxlo":  {"variable": "mfluxlo",  "title": "RF11, day 247, mfluxlo (kg/m$^2$/s)",  "x_axis": {"label": "longitude (deg)", "limits": [-89, -86]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "color_bar": {"ticks": [-0.08, -0.06, -0.04, -0.02, 0, 0.02, 0.04, 0.06, 0.08]}},
        "p_mfluxhi":  {"variable": "mfluxhi",  "title": "RF11, day 247, mfluxhi (kg/m$^2$/s)",  "x_axis": {"label": "longitude (deg)", "limits": [-89, -86]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "color_bar": {"ticks": [-0.08, -0.06, -0.04, -0.02, 0, 0.02, 0.04, 0.06, 0.08]}},
        "p_mfluxvl":  {"variable": "mfluxvl",  "title": "RF11, day 247, mfluxvl (kg/m$^2$/s)",  "x_axis": {"label": "longitude (deg)", "limits": [-89, -86]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "color_bar": {"ticks": [-0.08, -0.06, -0.04, -0.02, 0, 0.02, 0.04, 0.06, 0.08]}},
        "p_mfluxdif": {"variable": "mfluxdif", "title": "RF11, day 247, mfluxdif (kg/m$^2$/s)", "x_axis": {"label": "longitude (deg)", "limits": [-89, -86]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 11]}, "color_bar": {"ticks": [-0.08, -0.06, -0.04, -0.02, 0, 0.02, 0.04, 0.06, 0.08]}}
    }
}
