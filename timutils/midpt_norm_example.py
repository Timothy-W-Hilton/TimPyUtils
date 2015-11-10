import matplotlib.pyplot as plt
import numpy as np
from timutils import midpt_norm


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
    cb = plt.colorbar(dummy_scm, cax=cax, format=format, extend='both')
    return(cb)


plt.close('all')
data = np.random.randint(-140, 30, [124, 124])
#[data, data2] = np.meshgrid(np.linspace(-100, 20), np.linspace(-100, 20))
fix, ax = plt.subplots(1, 2)
mycmap, mynorm = midpt_norm.get_discrete_midpt_cmap_norm(
    vmin=-120, vmax=20,
    midpoint=0.0,
    bands_above_mdpt=3,
    bands_below_mdpt=6,
    extend='both')
cm = ax[0].pcolormesh(data, norm=mynorm, cmap=mycmap)
cb = colorbar_from_cmap_norm(mycmap, mynorm, ax[1], '%d', data)
# plt.colorbar(cm, cax=ax[1], norm=mynorm, extend='both')
plt.show()
