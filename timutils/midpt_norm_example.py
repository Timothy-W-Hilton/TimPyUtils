import matplotlib.pyplot as plt
from timutils import midpt_norm
import numpy as np
from matplotlib.colors import from_levels_and_colors


def colorbar_from_cmap_norm(cmap, norm, cax, format, vals):
    """
    create a colorbar in a specified axis from a colormap instance, a
    norm instance, and an array of values.

    This is a workaround for a problem I'm having where calling
    plt.colorbar on different matplotlib.contour.QuadContourSet
    created from the same cmap and norm produces different colorbars,
    all of which are messed up in one way or another.  This function
    creates a dummy mappable and creates the colorbar from it.
    """
    dummy_scm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    dummy_scm.set_array(vals)
    cb = plt.colorbar(dummy_scm, cax=cax, format=format)
    return(cb)

data = np.random.randint(-120, 20, [124, 124])
[data, data2] = np.meshgrid(np.linspace(-100, 20), np.linspace(-100, 20))
n = midpt_norm.MidpointNormalize(vmin=-120, vmax=20, midpoint=0.0, nlevs=12)
fix, ax = plt.subplots(1, 2)
cm = ax[0].pcolormesh(data, norm=n, cmap=plt.get_cmap('PuOr', 10))
plt.colorbar(cm, cax=ax[1])
# cb = colorbar_from_cmap_norm(plt.get_cmap('PuOr', 10), n, ax[1], '%0d', data)
plt.show()
