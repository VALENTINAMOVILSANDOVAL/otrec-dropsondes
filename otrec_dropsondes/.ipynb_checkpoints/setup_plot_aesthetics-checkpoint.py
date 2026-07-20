# otrec_dropsondes/setup_plot_aesthetics.py

import matplotlib.pyplot as plt

def setup_plot_aesthetics():
    """Configures global matplotlib aesthetics for journal publication."""
    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': 10,
        'axes.linewidth': 1,
        'xtick.direction': 'in',
        'ytick.direction': 'in',
        'xtick.top': True,
        'ytick.right': True,
        'xtick.major.size': 4,
        'ytick.major.size': 4,
        'axes.labelsize': 11,
        'axes.titlesize': 11,
    })
