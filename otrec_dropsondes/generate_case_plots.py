# otrec_dropsondes/generate_case_plots.py

import os
import re
import importlib
import warnings

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import xarray as xr

from .helpers import _squeeze_to_2d, _map_panel
from .setup_plot_aesthetics import setup_plot_aesthetics

_CASE_REGISTRY = {
    '0807': ('20190807', 'box2'),
    '0811': ('20190811', 'box1'),
    '0812': ('20190812', 'box2'),
    '0816': ('20190816', 'box1'),
    '0817': ('20190817', 'box2'),
    '0818': ('20190818', 'box3'),
    '0822': ('20190822', 'box1'),
    '0823': ('20190823', 'box2'),
    '0825': ('20190825', 'box1'),
    '0903': ('20190903', 'box1'),
    '0904': ('20190904', 'box2'),
    '0909': ('20190909', 'box1'),
    '0917': ('20190917', 'box1'),
    '0921': ('20190921', 'box2'),
    '0922': ('20190922', 'box1'),
    '0924': ('20190924', 'box2'),
    '0925': ('20190925', 'box1'),
    '0927': ('20190927', 'box2'),
    '0928': ('20190928', 'box2'),
    '0930': ('20190930', 'box2'),
    '1001': ('20191001', 'box2'),
    '1002': ('20191002', 'box2'),
}

# ── Plot functions ────────────────────────────────────────────────────────────

def plot_iisf(case, ds, output_dir):
    cfg = case.get('iisf')
    if not cfg:
        warnings.warn('iisf: not defined for this case — skipping.'); return
    items = list(cfg.items())
    n = len(items)
    fig, axes = plt.subplots(1, n, figsize=(7.16, 3.5))
    if n == 1: axes = [axes]
    lon = ds['lon'].values
    lat = ds['lat'].values
    for i, (ax, (key, params)) in enumerate(zip(axes, items)):
        _map_panel(ax, _squeeze_to_2d(ds[params['variable']]), lon, lat, params, show_ylabel=(i == 0))
    plt.subplots_adjust(wspace=0.45, bottom=0.18, top=0.88)
    plt.suptitle('iisf', y=0.98, fontsize=9, color='grey')
    plt.savefig(os.path.join(output_dir, 'iisf.pdf'), bbox_inches='tight')
    plt.close()

def plot_ppiplot(case, ds, output_dir):
    cfg = case.get('ppiplot')
    if not cfg:
        warnings.warn('ppiplot: not defined for this case — skipping.'); return
    params = list(cfg.values())[0]
    fig, ax = plt.subplots(figsize=(4.5, 4.0))
    _map_panel(ax, _squeeze_to_2d(ds[params['variable']]), ds['lon'].values, ds['lat'].values, params)
    plt.tight_layout()
    plt.suptitle('ppiplot', y=1.01, fontsize=9, color='grey')
    plt.savefig(os.path.join(output_dir, 'ppiplot.pdf'), bbox_inches='tight')
    plt.close()

def plot_mflux(case, ds, output_dir):
    cfg = case.get('mflux')
    if not cfg:
        warnings.warn('mflux: not defined for this case — skipping.'); return
    items = list(cfg.items())
    fig, axes = plt.subplots(2, 2, figsize=(7.16, 5.5))
    axes = axes.flatten()
    lon = ds['lon'].values
    lat = ds['lat'].values
    for i, (ax, (key, params)) in enumerate(zip(axes, items)):
        _map_panel(ax, _squeeze_to_2d(ds[params['variable']]), lon, lat, params, show_ylabel=(i % 2 == 0))
    plt.subplots_adjust(wspace=0.45, hspace=0.55, bottom=0.08, top=0.93)
    plt.suptitle('mflux', y=0.97, fontsize=9, color='grey')
    plt.savefig(os.path.join(output_dir, 'mflux.pdf'), bbox_inches='tight')
    plt.close()

def plot_src(case, ds, output_dir):
    cfg = case.get('src')
    if not cfg:
        warnings.warn('src: not defined for this case — skipping.'); return
    items = list(cfg.items())
    fig, axes = plt.subplots(1, 2, figsize=(7.16, 3.5))
    lon = ds['lon'].values
    lat = ds['lat'].values
    for i, (ax, (key, params)) in enumerate(zip(axes, items)):
        _map_panel(ax, _squeeze_to_2d(ds[params['variable']]), lon, lat, params, show_ylabel=(i == 0))
    plt.subplots_adjust(wspace=0.45, bottom=0.18, top=0.88)
    plt.suptitle('src', y=0.98, fontsize=9, color='grey')
    plt.savefig(os.path.join(output_dir, 'src.pdf'), bbox_inches='tight')
    plt.close()

def plot_surf(case, ds, output_dir):
    cfg = case.get('surf')
    if not cfg:
        warnings.warn('surf: not defined for this case — skipping.'); return
    items = list(cfg.items())
    fig, axes = plt.subplots(1, 2, figsize=(7.16, 3.5))
    lon = ds['lon'].values
    lat = ds['lat'].values
    for i, (ax, (key, params)) in enumerate(zip(axes, items)):
        _map_panel(ax, _squeeze_to_2d(ds[params['variable']]), lon, lat, params, show_ylabel=(i == 0))
    plt.subplots_adjust(wspace=0.45, bottom=0.18, top=0.88)
    plt.suptitle('surf', y=0.98, fontsize=9, color='grey')
    plt.savefig(os.path.join(output_dir, 'surf.pdf'), bbox_inches='tight')
    plt.close()

def plot_sst_wind(case, ds, output_dir):
    cfg = case.get('sst_wind')
    if not cfg:
        warnings.warn('sst_wind: not defined for this case — skipping.'); return
    items = list(cfg.items())
    fig, axes = plt.subplots(1, 2, figsize=(7.16, 3.5))
    lon = ds['lon'].values
    lat = ds['lat'].values
    for i, (ax, (key, params)) in enumerate(zip(axes, items)):
        if key == 'p_pres':
            data = ds['pres'].isel(z=0).squeeze().transpose('lat', 'lon').values
        else:
            data = _squeeze_to_2d(ds[params['variable']])
        ticks = params['color_bar']['ticks']
        dmin, dmax = np.nanmin(data), np.nanmax(data)
        if ticks[0] > dmax or ticks[-1] < dmin:
            ticks  = list(np.round(np.linspace(dmin, dmax, len(ticks)), 1))
            params = {**params, 'color_bar': {'ticks': ticks}}
        _map_panel(ax, data, lon, lat, params, show_ylabel=(i == 0))
        if key == 'p_pres' and 'u' in ds and 'v' in ds:
            u0 = ds['u'].isel(z=0).squeeze().transpose('lat', 'lon').values
            v0 = ds['v'].isel(z=0).squeeze().transpose('lat', 'lon').values
            ax.streamplot(lon, lat, u0, v0, color='k', linewidth=0.6, density=1.2, arrowsize=0.9)
    plt.subplots_adjust(wspace=0.45, bottom=0.18, top=0.88)
    plt.suptitle('sst_wind', y=0.98, fontsize=9, color='grey')
    plt.savefig(os.path.join(output_dir, 'sst_wind.pdf'), bbox_inches='tight')
    plt.close()

def plot_vort(case, ds, output_dir):
    cfg = case.get('vort')
    if not cfg:
        warnings.warn('vort: not defined for this case — skipping.'); return
    items = list(cfg.items())
    z_levels = [1.5, 4.0]
    fig, axes = plt.subplots(1, 2, figsize=(7.16, 3.5))
    lon = ds['lon'].values
    lat = ds['lat'].values
    for i, (ax, (key, params)) in enumerate(zip(axes, items)):
        sl = ds.sel(z=z_levels[i], method='nearest')
        _map_panel(ax, sl[params['variable']].squeeze().transpose('lat', 'lon').values, lon, lat, params, show_ylabel=(i == 0))
        if 'u' in ds and 'v' in ds:
            ax.streamplot(lon, lat,
                          sl['u'].squeeze().transpose('lat', 'lon').values,
                          sl['v'].squeeze().transpose('lat', 'lon').values,
                          color='k', linewidth=0.6, density=1.2, arrowsize=0.9)
    plt.subplots_adjust(wspace=0.45, bottom=0.18, top=0.88)
    plt.suptitle('vort', y=0.98, fontsize=9, color='grey')
    plt.savefig(os.path.join(output_dir, 'vort.pdf'), bbox_inches='tight')
    plt.close()

def plot_zlatplot(case, ds, output_dir):
    cfg = case.get('zlatplot')
    if not cfg:
        warnings.warn('zlatplot: not defined for this case — skipping.'); return
    params = list(cfg.values())[0]
    mflux_zl = ds['mflux'].mean(dim='lon').transpose('z', 'lat')
    u_zl     = ds['u'].mean(dim='lon').transpose('z', 'lat')
    lat = ds['lat'].values
    z   = ds['z'].values
    mflux_vals = mflux_zl.values
    ref = 0.1
    lat_span = lat.max() - lat.min()
    z_span   = z.max()  - z.min()
    U = mflux_vals / ref
    V = mflux_vals / ref * (lat_span / z_span)
    tL = params['color_bar_left']['ticks']
    tR = params['color_bar_right']['ticks']
    fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(7.16, 4.0))
    cfL = ax_l.contourf(lat, z, mflux_vals, levels=np.linspace(tL[0], tL[-1], 100), cmap='RdBu_r', extend='both')
    ax_l.contour(lat, z, mflux_vals, levels=np.linspace(tL[0], tL[-1], len(tL)), colors='k', linewidths=0.5)
    if 0 in tL: ax_l.contour(lat, z, mflux_vals, levels=[0], colors='k', linewidths=1.5)
    cbarL = fig.colorbar(cfL, ax=ax_l, orientation='horizontal', pad=0.22, aspect=20)
    cbarL.set_ticks(tL)
    cbarL.ax.set_xticklabels([f'{t:g}' for t in tL], rotation=45, ha='right', fontsize=7)
    cbarL.ax.tick_params(labelsize=7, pad=1)
    cfR = ax_r.contourf(lat, z, u_zl.values, levels=np.linspace(tR[0], tR[-1], 100), cmap='RdBu_r', extend='both')
    ax_r.contour(lat, z, u_zl.values, levels=np.linspace(tR[0], tR[-1], len(tR)), colors='k', linewidths=0.5)
    if 0 in tR: ax_r.contour(lat, z, u_zl.values, levels=[0], colors='k', linewidths=1.5)
    cbarR = fig.colorbar(cfR, ax=ax_r, orientation='horizontal', pad=0.22, aspect=20)
    cbarR.set_ticks(tR)
    cbarR.ax.set_xticklabels([f'{t:g}' for t in tR], rotation=45, ha='right', fontsize=7)
    cbarR.ax.tick_params(labelsize=7, pad=1)
    skip_lat, skip_z = 3, 8
    for ax in [ax_l, ax_r]:
        ax.quiver(lat[::skip_lat], z[::skip_z], U[::skip_z, ::skip_lat], V[::skip_z, ::skip_lat],
                  angles='xy', scale_units='xy', scale=0.1, color='k',
                  width=0.008, headwidth=5, headlength=6, headaxislength=5, alpha=0.9)
    xlim = params['x_axis']['limits']
    ylim = params['y_axis']['limits']
    for ax, label in zip([ax_l, ax_r], ['mass flux (kg/m$^2$/s)', 'zonal wind (m/s)']):
        ax.set_xlabel(params['x_axis']['label']); ax.set_ylabel(params['y_axis']['label'])
        ax.set_xlim(xlim); ax.set_ylim(ylim); ax.set_title(label, fontsize=9, pad=6)
        ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
        ax.yaxis.set_major_locator(MaxNLocator(nbins=7))
    fig.suptitle(params['title'], fontsize=10, y=0.98)
    plt.subplots_adjust(wspace=0.45, bottom=0.18, top=0.88)
    plt.savefig(os.path.join(output_dir, 'zlatplot.pdf'), bbox_inches='tight')
    plt.close()

def plot_pv_xz(case, ds, output_dir):
    """
    pv_xz.pdf -- longitude-height cross-sections at two latitude bands,
    using the 'vort' config block's variables/titles/ticks.

    Filled RdBu_r contours; black contour lines at the same tick levels;
    a heavier black zero-contour; horizontal colorbar per panel. Panel
    latitudes are chosen automatically at 1/3 and 2/3 of the lat range.
    """
    cfg = case.get('vort')
    if not cfg:
        warnings.warn('pv_xz: vort config not defined for this case — skipping.'); return

    lon = ds['lon'].values
    z = ds['z'].values

    lon_min, lon_max = ds['lonx'].min().item(), ds['lonx'].max().item()
    z_min, z_max = z.min(), z.max()

    fig, axes = plt.subplots(1, 2, figsize=(7.16, 4.0))
    axes = axes.flatten()

    items = list(cfg.items())
    lat_levels = [ds['lat'].values[len(ds['lat'])//3], ds['lat'].values[2*len(ds['lat'])//3]]

    for i, (ax, (key, params)) in enumerate(zip(axes, items)):
        var = params['variable']
        data_level = ds.sel(lat=lat_levels[i], method='nearest')
        data = data_level[var].transpose('z', 'lon').values

        ticks = params['color_bar']['ticks']
        cf_levels = np.linspace(ticks[0], ticks[-1], 100)
        thin_contours = np.linspace(ticks[0], ticks[-1], len(ticks))

        cf = ax.contourf(lon, z, data, levels=cf_levels, cmap='RdBu_r', extend='both')
        ax.contour(lon, z, data, levels=thin_contours, colors='black', linewidths=0.5)
        ax.contour(lon, z, data, levels=[0], colors='black', linewidths=1.5)

        ax.set_title(f"{params['title']} (lat={lat_levels[i]:.2f})", pad=10, fontsize=10)
        ax.set_xlabel('longitude (deg)')
        if i == 0:
            ax.set_ylabel('height (km)')

        ax.set_xlim(lon_min, lon_max)
        ax.set_ylim(z_min, z_max)

        ax.xaxis.set_major_locator(MaxNLocator(nbins=5))
        ax.yaxis.set_major_locator(MaxNLocator(nbins=7))

        cbar = fig.colorbar(cf, ax=ax, orientation='horizontal', pad=0.25, aspect=20)
        cbar.set_ticks(ticks)
        cbar.ax.set_xticklabels([f'{t:g}' for t in ticks], rotation=45, ha='right', fontsize=7)
        cbar.ax.tick_params(labelsize=7, pad=1)

    plt.subplots_adjust(wspace=0.45, bottom=0.15, top=0.85, left=0.1, right=0.95)
    plt.suptitle('pv_xz', y=0.98, fontsize=9, color='grey')
    plt.savefig(os.path.join(output_dir, 'pv_xz.pdf'), bbox_inches='tight')
    plt.close()

_LATPLOT_VAR_MAP = {
    'mflux':  [('mfluxhi', 'red', 'mfluxhi'), ('mfluxlo', 'blue', 'mfluxlo')],
    'sst':    [('sst',     'blue', 'SST')],
    'eflux':  [('eflux',  'red',  'moisture'), ('rtflux', 'blue', 'entropy')],
    'ii':     [('ii',     'red',  'instab index'), ('dcin', 'blue', 'dcin')],
    'srcmr':  [('srcmrh', 'blue', 'moisture convergence'), ('srcenth', 'red', 'entropy divergence')],
    'sfrac':  [('sfrac',  'blue', 'sat frac')],
}

def plot_latplot(case, ds, output_dir):
    cfg = case.get('latplot')
    if not cfg:
        warnings.warn('latplot: not defined for this case — skipping.'); return
    items = list(cfg.items())
    n = len(items)
    ncols = 2
    nrows = (n + 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(10, 3.5 * nrows), sharex=True)
    axes_flat = axes.flatten() if n > 1 else [axes]
    lat = ds['lat'].values
    for i, (ax, (key, params)) in enumerate(zip(axes_flat, items)):
        for vname, color, label in _LATPLOT_VAR_MAP.get(params['variable'], [(params['variable'], 'k', params['variable'])]):
            if vname in ds:
                ax.plot(lat, ds[vname].mean(dim='lon').values, color=color, lw=1.5, label=label)
        ax.set_xlim(params['x_axis']['limits']); ax.set_ylim(params['y_axis']['limits'])
        ax.set_ylabel(params['y_axis']['label']); ax.set_title(params.get('title', ''), fontsize=9)
        ax.legend(frameon=False, fontsize=7); ax.grid(True, linestyle='--', alpha=0.3)
        if i >= n - ncols: ax.set_xlabel(params['x_axis']['label'])
    for ax in axes_flat[n:]: ax.set_visible(False)
    plt.subplots_adjust(hspace=0.35, wspace=0.35)
    plt.suptitle('latplot', y=1.01, fontsize=9, color='grey')
    plt.savefig(os.path.join(output_dir, 'latplot.pdf'), bbox_inches='tight')
    plt.close()

def plot_profs(case, ds, output_dir):
    cfg = case.get('profs')
    if not cfg:
        warnings.warn('profs: not defined for this case — skipping.'); return
    z = ds['z'].values
    cold_mask = ds['sst'] < 27.5
    warm_mask = ds['sst'] >= 27.5
    def _mean(vname, mask):
        return ds[vname].where(mask).mean(dim=['lon', 'lat']).values if vname in ds else None
    _PROFS_VAR_MAP = {
        'ent':   [('ent', 'entropy'), ('satent', 'sat entropy')],
        'mflux': [('mflux', 'mass flux')],
    }
    items = list(cfg.items())
    fig, axes = plt.subplots(1, len(items), figsize=(7.16, 4.0))
    if len(items) == 1: axes = [axes]
    for i, (ax, (key, params)) in enumerate(zip(axes, items)):
        for vname, label in _PROFS_VAR_MAP.get(params['variable'], [(params['variable'], params['variable'])]):
            cold = _mean(vname, cold_mask)
            warm = _mean(vname, warm_mask)
            if cold is not None: ax.plot(cold, z, 'b-', lw=1.5)
            if warm is not None: ax.plot(warm, z, 'r-', lw=1.5)
        ax.set_title(params['title'], fontsize=9, pad=6)
        ax.set_xlim(params['x_axis']['limits']); ax.set_xticks(params['x_axis']['ticks'])
        ax.set_xlabel(params['x_axis']['label']); ax.set_ylim(params['y_axis']['limits'])
        if i == 0: ax.set_ylabel(params['y_axis']['label'])
        ax.grid(True, linestyle='--', alpha=0.3)
    plt.subplots_adjust(wspace=0.3)
    plt.suptitle('profs', y=1.01, fontsize=9, color='grey')
    plt.savefig(os.path.join(output_dir, 'profs.pdf'), bbox_inches='tight')
    plt.close()

def plot_sndplot(case, ds, output_dir):
    cfg = case.get('sndplot')
    if not cfg:
        warnings.warn('sndplot: not defined for this case — skipping.'); return
    _SNDPLOT_VAR_MAP = {
        'ent': [('ent', 'b-', 'entropy'), ('satent', 'r-', 'sat ent')],
        'u':   [('u',   'b-', 'U wind'),  ('v',      'r-', 'V wind')],
    }
    items = list(cfg.items())
    fig, axes = plt.subplots(1, len(items), figsize=(7.16, 4.0))
    if len(items) == 1: axes = [axes]
    first_title = items[0][1]['title']
    match = re.search(r'\(([\-\d.]+),\s*([\-\d.]+)\)', first_title)
    snd_lon = float(match.group(1)) if match else float(ds['lon'].mean())
    snd_lat = float(match.group(2)) if match else float(ds['lat'].mean())
    prof = ds.sel(lon=snd_lon, lat=snd_lat, method='nearest')
    z = ds['z'].values
    for i, (ax, (key, params)) in enumerate(zip(axes, items)):
        for vname, style, label in _SNDPLOT_VAR_MAP.get(params['variable'], [(params['variable'], 'b-', params['variable'])]):
            if vname in prof: ax.plot(prof[vname].values, z, style, lw=1.5, label=label)
        ax.set_title(params['title'], fontsize=9, pad=6)
        ax.set_xlim(params['x_axis']['limits']); ax.set_xticks(params['x_axis']['ticks'])
        ax.set_xlabel(params['x_axis']['label']); ax.set_ylim(params['y_axis']['limits'])
        if i == 0: ax.set_ylabel(params['y_axis']['label'])
        ax.legend(frameon=False, fontsize=7); ax.grid(True, linestyle='--', alpha=0.3)
    plt.subplots_adjust(wspace=0.3)
    plt.suptitle('sndplot', y=1.01, fontsize=9, color='grey')
    plt.savefig(os.path.join(output_dir, 'sndplot.pdf'), bbox_inches='tight')
    plt.close()

def plot_mfluxplot(case, ds, output_dir):
    cfg = case.get('mfluxplot')
    if not cfg:
        warnings.warn('mfluxplot: not defined for this case — skipping.'); return
    items = list(cfg.items())
    fig, axes = plt.subplots(1, len(items), figsize=(7.16, 4.0))
    if len(items) == 1: axes = [axes]
    first_title = items[0][1]['title']
    match = re.search(r'\(([\-\d.]+),\s*([\-\d.]+)\)', first_title)
    snd_lon = float(match.group(1)) if match else float(ds['lon'].mean())
    snd_lat = float(match.group(2)) if match else float(ds['lat'].mean())
    prof = ds.sel(lon=snd_lon, lat=snd_lat, method='nearest')
    z = ds['z'].values
    for i, (ax, (key, params)) in enumerate(zip(axes, items)):
        if params['variable'] in prof:
            ax.plot(prof[params['variable']].values, z, 'b-', lw=1.5)
        ax.set_title(params['title'], fontsize=9, pad=6)
        ax.set_xlim(params['x_axis']['limits']); ax.set_xticks(params['x_axis']['ticks'])
        ax.set_xlabel(params['x_axis']['label']); ax.set_ylim(params['y_axis']['limits'])
        if i == 0: ax.set_ylabel(params['y_axis']['label'])
        ax.axvline(0, color='k', lw=0.8, ls='--'); ax.grid(True, linestyle='--', alpha=0.3)
    plt.subplots_adjust(wspace=0.3)
    plt.suptitle('mfluxplot', y=1.01, fontsize=9, color='grey')
    plt.savefig(os.path.join(output_dir, 'mfluxplot.pdf'), bbox_inches='tight')
    plt.close()

_ALL_PLOT_FUNCTIONS = [
    plot_iisf, plot_ppiplot, plot_mflux, plot_src, plot_surf,
    plot_sst_wind, plot_vort, plot_zlatplot, plot_pv_xz, plot_latplot,
    plot_profs, plot_sndplot, plot_mfluxplot,
]

def generate_case_plots(case_id: str, data_dir: str = './data', output_dir: str = './plots'):
    """Generate all available PDF plots for a single OTREC case."""
    if case_id not in _CASE_REGISTRY:
        raise ValueError(f"Unknown case_id '{case_id}'. Valid options: {sorted(_CASE_REGISTRY.keys())}")

    yyyymmdd, box = _CASE_REGISTRY[case_id]
    mod  = importlib.import_module(f'.configs.config_{case_id}', package='otrec_dropsondes')
    case = mod.CASE

    nc_file = os.path.join(data_dir, yyyymmdd, box, 'merge-1.nc')
    if not os.path.exists(nc_file):
        raise FileNotFoundError(f"NetCDF not found: {nc_file}")

    case_out = os.path.join(output_dir, case_id)
    os.makedirs(case_out, exist_ok=True)

    setup_plot_aesthetics()
    ds = xr.open_dataset(nc_file).isel(record=0)
    print(f"=== Generating plots for case {case_id} ({yyyymmdd}/{box}) ===")

    for fn in _ALL_PLOT_FUNCTIONS:
        try:
            fn(case, ds, case_out)
            print(f"  ✅  {fn.__name__.replace('plot_', '')}.pdf")
        except Exception as exc:
            warnings.warn(f"  ⚠️  {fn.__name__} failed: {exc}")

    ds.close()
    print(f"  → Saved to {case_out}/\n")
