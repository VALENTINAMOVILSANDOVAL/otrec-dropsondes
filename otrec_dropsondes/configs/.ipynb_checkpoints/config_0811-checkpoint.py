"""Case 0811 — RF02, 2019-08-11, box1 (partial — ppiplot + sndplot + mfluxplot only)"""
CASE = {
    "ppiplot": {
        "p_srcmr": {"variable": "srcmr", "title": "RF02: rain (mm/d, r/b); mfdif (kg/m$^2$/s, k); Track (y)", "x_axis": {"label": "longitude (deg)", "limits": [-84, -77]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 14]}, "color_bar": {"ticks": [-50, -25, 0, 25, 50, 75, 100, 125, 150]}}
    },
    "sndplot": {
        "p_ent": {"variable": "ent", "title": "RF02: 3DVAR (-78, 5) - entropy / sat ent", "x_axis": {"label": "entropy (J/K/kg)",  "limits": [200, 320], "ticks": [200, 240, 280, 320]}, "y_axis": {"label": "height (km)", "limits": [0, 14]}},
        "p_u":   {"variable": "u",   "title": "RF02: 3DVAR (-78, 5) - U wind / V wind",   "x_axis": {"label": "U, V wind (m/s)", "limits": [-16, 12], "ticks": [-16, -12, -8, -4, 0, 4, 8, 12]}, "y_axis": {"label": "height (km)", "limits": [0, 14]}}
    },
    "mfluxplot": {
        "p_mflux": {"variable": "mflux", "title": "RF02: 3DVAR (-78, 5) - mass flux (kg/m$^2$/s)",      "x_axis": {"label": "mass flux (kg/m$^2$/s)",      "limits": [-0.08, 0.08], "ticks": [-0.08, -0.04, 0, 0.04, 0.08]}, "y_axis": {"label": "height (km)", "limits": [0, 14]}},
        "p_w":     {"variable": "w",     "title": "RF02: 3DVAR (-78, 5) - HCR vertical velocity (m/s)", "x_axis": {"label": "HCR vertical velocity (m/s)", "limits": [-6, 0],     "ticks": [-6, -5, -4, -3, -2, -1, 0]},     "y_axis": {"label": "height (km)", "limits": [0, 14]}}
    }
}
