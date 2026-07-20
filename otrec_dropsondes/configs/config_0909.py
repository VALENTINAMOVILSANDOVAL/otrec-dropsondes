"""Case 0909 — RF12, 2019-09-09, box1 (partial — ppiplot + sndplot + mfluxplot only)"""
CASE = {
    "ppiplot": {
        "p_srcmr": {"variable": "srcmr", "title": "RF12: moisture conv (W/m$^2$, r/b); Track (y)", "x_axis": {"label": "longitude (deg)", "limits": [-84, -77]}, "y_axis": {"label": "latitude (deg)", "limits": [3, 14]}, "color_bar": {"ticks": [-1000, -500, 0, 500, 1000, 1500, 2000]}}
    },
    "sndplot": {
        "p_ent": {"variable": "ent", "title": "RF12: 3DVAR (-78.5, 5.5) - entropy / sat ent", "x_axis": {"label": "entropy (J/K/kg)",  "limits": [200, 320], "ticks": [200, 240, 280, 320]}, "y_axis": {"label": "height (km)", "limits": [0, 14]}},
        "p_u":   {"variable": "u",   "title": "RF12: 3DVAR (-78.5, 5.5) - U wind / V wind",   "x_axis": {"label": "U, V wind (m/s)", "limits": [-12, 8], "ticks": [-12, -8, -4, 0, 4, 8]}, "y_axis": {"label": "height (km)", "limits": [0, 14]}}
    },
    "mfluxplot": {
        "p_mflux": {"variable": "mflux", "title": "RF12: 3DVAR (-78.5, 5.5) - mass flux (kg/m$^2$/s)",      "x_axis": {"label": "mass flux (kg/m$^2$/s)",      "limits": [-0.04, 0.06], "ticks": [-0.04, -0.02, 0, 0.02, 0.04, 0.06]}, "y_axis": {"label": "height (km)", "limits": [0, 14]}},
        "p_w":     {"variable": "w",     "title": "RF12: 3DVAR (-78.5, 5.5) - HCR vertical velocity (m/s)", "x_axis": {"label": "HCR vertical velocity (m/s)", "limits": [-6, 0],     "ticks": [-6, -5, -4, -3, -2, -1, 0]},     "y_axis": {"label": "height (km)", "limits": [0, 14]}}
    }
}
