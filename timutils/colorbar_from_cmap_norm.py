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

    ARGS:
        cmap (:class:`matplotlib.colors.Colormap` instance): The colormap
            to use in the colorbar
        norm (:class:`matplotlib.colors.Normalize` instance): normalizer
            to use for the colorbar
        cax (:class:`matplotlib.axes.Axes` instance): Axes where the
            colorbar is to be drawn
        format (string): [None | format string | Formatter object]
            If None, the :class:`matplotlib.ticker.ScalarFormatter` is
            used. If a format string is given, e.g., '%.3f', that is
            used. An alternative :class:`matplotlib.ticker.Formatter`
            object may be given instead.
        vals (:class:`numpy.array`-like): the data to be described by the
            colorbar

    RETURNS:
        a
        :class:`matplotlib.colorbar.Colorbar` object.

    EXAMPLE:
        >>> import matplotlib.pyplot as plt
        >>> import numpy as np
        >>> data = np.random.random([100, 100])
        >>> my_cmap, my_norm = colormap_nlevs.setup_colormap(
            data.min(), data.max(),
            nlevs=6,
            cmap=plt.get_cmap('Greens'),
            extend='max')
        >>> fig, ax = plt.subplots(nrows=1, ncols=2)
        >>> ax[0].pcolormesh(data, cmap=my_cmap, norm=my_norm)
        >>> cb = colorbar_from_cmap_norm(my_cmap,
                                     my_norm,
                                     ax[1],
                                     '%0.2f',
                                     data)
        >>> plt.show()

    """

    dummy_scm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    dummy_scm.set_array(vals)
    cb = plt.colorbar(dummy_scm, cax=cax, format=format)
    return(cb)
