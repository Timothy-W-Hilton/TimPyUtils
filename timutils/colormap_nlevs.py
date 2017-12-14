"""create colormaps with user-specified number of intervals.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import from_levels_and_colors


def setup_colormap(vmin, vmax, nlevs=5,
                   cmap=plt.get_cmap('Greens'),
                   extend='both'):
    """
    create a discrete colormap from a continuous colormap

    Returns the N-level colormap and a normalizer to plot arbitrary
    data using the colormap.  The normalizing places the N levels at
    constant intervals between the vmin and vmax.

    ARGS:
        vmin (float): value to map to the lowest color level
        vmax (float): value to map to the highest color level
        nlevs (integer): number of levels for the colormap (default is 5)
        cmap (:class:`matplotlib.colors.Colormap` instance): colormap to use for the N-level colormap
        extend (string): ({'both'} | 'min' | 'max' | 'neither'}) should the top or bottom of the colormap use an arrow to indicate "and larger" or "and smaller"

    RETURNS:
        tuple (cmap, norm) containing a
        :class:`matplotlib.colors.Colormap` object and a
        :class:`matplotlib.colors.Normalize` object.

    EXAMPLES:
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> from timutils.colormap_nlevs import setup_colormap
    >>> data = np.random.rand(100, 100)  * 1000
    >>> mycmap, mynorm = setup_colormap(vmin=200.0, vmax=800.0, extend='max')
    >>> fig, ax = plt.subplots()
    >>> cm = ax.pcolormesh(data, cmap=mycmap, norm=mynorm)
    >>> plt.colorbar(cm)
    >>> plt.title(('setup_colormap example\\n data values 0 to 1000; nlevs=5, vmin=200, vmax=800'))
    >>> plt.show()

    """
    print('setting up colormaps')
    # Pick some of the nicer colors from the palette...
    if extend is "neither":
        ncolors = nlevs - 1
    elif (extend is "min") or (extend is "max"):
        ncolors = nlevs
    elif extend is "both":
        ncolors = nlevs + 1
    levels = np.linspace(start=vmin, stop=vmax, num=nlevs)
    colors = cmap(np.linspace(start=0.0, stop=1.0, num=ncolors))
    cmap, norm = from_levels_and_colors(levels, colors, extend=extend)
    return((cmap, norm))


def setup_colormap_with_zeroval(vmin, vmax, nlevs=5,
                                cmap=plt.get_cmap('Greens'),
                                extend='both'):
    """create a discrete colormap with reserved level for small values

    setup a colormap based on a existing colormap with a specified
    number N of levels reserving the lowest colormap level for
    extremely small values.

    Extremely small are currently defined as [0.0, 1e-8].

    Returns the N-level colormap and a normalizer to plot arbitrary
    data using the colormap.  The normalizing places the N levels at
    constant intervals between the vmin and vmax.

    ARGS:
        vmin (float): value to map to the lowest color level
        vmax (float): value to map to the highest color level
        nlevs (integer): number of levels for the colormap (default is 5)
        cmap (:class:`matplotlib.colors.Colormap` instance): colormap to use for the N-level colormap
        extend (string): ({'both'} | 'min' | 'max' | 'neither') should the top or bottom of the colormap use an arrow to indicate "and larger" or "and smaller"

    RETURNS:
        tuple (cmap, norm) containing a
        :class:`matplotlib.colors.Colormap` object and a
        :class:`matplotlib.colors.Normalize object`.

    EXAMPLE:
        >>> import matplotlib.pyplot as plt
        >>> import numpy as np
        >>> from timutils.colormap_nlevs import setup_colormap_with_zeroval
        >>> data = np.random.rand(100, 100)
        >>> mycmap, mynorm = setup_colormap_with_zeroval(vmin=data.min(), vmax=data.max(), nlevs=7, extend='neither')
        >>> fig, ax = plt.subplots()
        >>> cm = ax.pcolormesh(data, cmap=mycmap, norm=mynorm)
        >>> plt.colorbar(cm)
        >>> plt.title(('setup_colormap_with_zeroval example\\n data values 0 to 1; nlevs=5'))
        >>> plt.show()

    """

    # Pick some of the nicer colors from the palette...
    if extend is "neither":
        ncolors = nlevs
    elif (extend is "min") or (extend is "max"):
        ncolors = nlevs + 1
    elif extend is "both":
        ncolors = nlevs + 2
    levels = np.concatenate((np.array([0.0, 1e-8]),
                             np.linspace(start=vmin,
                                         stop=vmax,
                                         num=nlevs)[1:]))
    colors = cmap(np.linspace(start=0.0, stop=1.0, num=ncolors))
    cmap, norm = from_levels_and_colors(levels, colors, extend=extend)
    return((cmap, norm))
