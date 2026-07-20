# otrec_dropsondes/helpers.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def _squeeze_to_2d(da):
    """
    Return a 2-D (lat, lon) numpy array regardless of whether the
    DataArray has an extra z dimension. Takes the first z level (index 0).
    """
    if 'z' in da.dims:
        da = da.isel(z=0)
    da = da.squeeze()
    if set(da.dims) == {'lat', 'lon'}:
        return da.transpose('lat', 'lon').values
    return da.values

def _map_panel(ax, data2d, lon, lat, params, show_ylabel=True):
    """Render one filled-contour map panel driven by a params dict block."""
    ticks  = params['color_bar']['ticks']
    levels = np.linspace(ticks[0], ticks[-1], 100)

    cf = ax.contourf(lon, lat, data2d,
                     levels=levels, cmap='RdBu_r', extend='both')
    ax.contour(lon, lat, data2d,
               levels=np.linspace(ticks[0], ticks[-1], len(ticks)),
               colors='k', linewidths=0.5)
    if 0 in ticks:
        ax.contour(lon, lat, data2d, levels=[0],
                   colors='k', linewidths=1.5)

    ax.set_title(params['title'], pad=6, fontsize=10)
    ax.set_xlabel(params['x_axis']['label'])
    if show_ylabel:
        ax.set_ylabel(params['y_axis']['label'])
    ax.set_xlim(params['x_axis']['limits'])
    ax.set_ylim(params['y_axis']['limits'])
    ax.xaxis.set_major_locator(MaxNLocator(nbins=5))
    ax.yaxis.set_major_locator(MaxNLocator(nbins=7))

    cbar = ax.get_figure().colorbar(
        cf, ax=ax, orientation='horizontal', pad=0.22, aspect=20)
    cbar.set_ticks(ticks)
    return cf
