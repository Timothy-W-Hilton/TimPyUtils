import matplotlib.pylab as plt


def colorbar_from_cmap_norm(cmap, norm, cax, format, vals):
    """
    create a colorbar in a specified axis from a colormap instance, a
    norm instance, and an array of values.

    This is a workaround for a problem I'm having where calling
    plt.colorbar on different matplotlib.contour.QuadContourSet
    created from the same cmap and norm produces different colorbars,
    all of which are messed up in one way or another.  This function
    creates a dummy mappable and creates the colorbar from it.

    INPUTS
    cmap: A :class:`matplotlib.colors.Colormap` instance.
    norm: A :class:`matplotlib.colors.Normalize` instance
    cax: axes: an :class:`~matplotlib.axes.Axes` instance where the
        colorbar is to be drawn
    format: [ None | format string | Formatter object ]
        If None, the :class:`~matplotlib.ticker.ScalarFormatter` is
        used. If a format string is given, e.g., '%.3f', that is
        used. An alternative :class:`~matplotlib.ticker.Formatter`
        object may be given instead.
    vals: the data to be described by the colorbar
    """

    dummy_scm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    dummy_scm.set_array(vals)
    cb = plt.colorbar(dummy_scm, cax=cax, format=format)
    return(cb)
