import matplotlib.pyplot as plt
from timutils import midpt_norm
import numpy as np
from matplotlib.colors import from_levels_and_colors
import matplotlib.colors as mcolors


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


def test_offset_norm_img():
    x = np.linspace(-2, 7)
    y = np.linspace(-1*np.pi, np.pi)
    X, Y = np.meshgrid(x, y)
    Z = x * np.sin(Y)**2

    fig, (ax1, ax2) = plt.subplots(ncols=2)
    cmap = plt.cm.coolwarm
    norm = midpt_norm.PiecewiseLinearNorm(vmin=-2, vcenter=0, vmax=7)

    img1 = ax1.imshow(Z, cmap=cmap, norm=None)
    cbar1 = fig.colorbar(img1, ax=ax1)

    img2 = ax2.imshow(Z, cmap=cmap, norm=norm)
    cbar2 = fig.colorbar(img2, ax=ax2)

data = np.random.randint(-120, 20, [5, 5])
# [data, data2] = np.meshgrid(np.linspace(-100, 20), np.linspace(-100, 20))
n = midpt_norm.PiecewiseLinearNorm(vmin=-120, vmax=20, vcenter=0.0)
fix, ax = plt.subplots(1, 2)
cm = ax[0].pcolormesh(data, norm=n, cmap=plt.get_cmap('PuOr', 10))
# plt.colorbar(cm, norm=n, cmap=plt.get_cmap('PuOr', 10))
cb = colorbar_from_cmap_norm(plt.get_cmap('PuOr', 10), n, ax[1], '%0d', data)
plt.show()
