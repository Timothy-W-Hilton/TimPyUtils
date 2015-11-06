import numpy as np
import numpy.ma as ma
from matplotlib.colors import Normalize


class MidpointNormalize(Normalize):
    """
    adapted by Timothy W. Hilton from code posted by Joe Kington to
    http://stackoverflow.com/questions/20144529/shifted-colorbar-matplotlib
    accessed 19 January 2015
    """

    def __init__(self, vmin=None, vmax=None, midpoint=None,
                 clip=False, nlevs=9):
        self.midpoint = midpoint
        self.nlevs = nlevs
        Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        # I'm ignoring masked values and all kinds of edge cases to make a
        # simple example...

        x = np.concatenate([np.linspace(start=self.vmin,
                                        stop=self.midpoint,
                                        num=7),
                            np.linspace(start=self.midpoint,
                                        stop=self.vmax,
                                        num=4)[1:]])
        y = np.concatenate([np.linspace(start=0.0,
                                        stop=0.5,
                                        num=7),
                            np.linspace(start=0.5,
                                        stop=1.0,
                                        num=4)[1:]])
        print 'x, y:', np.dstack([x, y])
        # x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]  #
        return np.ma.masked_array(np.interp(value, x, y))


class PiecewiseLinearNorm(Normalize):
    """
    A subclass of matplotlib.colors.Normalize.

    Normalizes data into the ``[0.0, 1.0]`` interval.
    """
    def __init__(self, vmin=None, vcenter=None, vmax=None):
        """Normalize data with an offset midpoint

        Useful when mapping data unequally centered around a conceptual
        center, e.g., data that range from -2 to 4, with 0 as the midpoint.

        Parameters
        ----------
        vmin : float, optional
            The data value that defines ``0.0`` in the normalized data.
            Defaults to the min value of the dataset.

        vcenter : float, optional
            The data value that defines ``0.5`` in the normalized data.
            Defaults to halfway between *vmin* and *vmax*.

        vmax : float, optional
            The data value that defines ``1.0`` in the normalized data.
            Defaults to the the max value of the dataset.

        Examples
        --------
        >>> import matplotlib.colors as mcolors
        >>> offset = mcolors.PiecewiseLinearNorm(vmin=-2., vcenter=0., vmax=4.)
        >>> data = [-2., -1., 0., 1., 2., 3., 4.]
        >>> offset(data)
        array([0., 0.25, 0.5, 0.625, 0.75, 0.875, 1.0])

        """

        self.vmin = vmin
        self.vcenter = vcenter
        self.vmax = vmax

    def __call__(self, value, clip=None):
        """Map value to the interval [0, 1]. The clip argument is unused."""

        result, is_scalar = self.process_value(value)

        self.autoscale_None(result)
        vmin, vcenter, vmax = self.vmin, self.vcenter, self.vmax
        if vmin == vmax == vcenter:
            result.fill(0)
        elif not vmin <= vcenter <= vmax:
            raise ValueError("minvalue must be less than or equal to "
                             "centervalue which must be less than or "
                             "equal to maxvalue")
        else:
            vmin = float(vmin)
            vcenter = float(vcenter)
            vmax = float(vmax)
            # in degenerate cases, prefer the center value to the extremes
            degen = (result == vcenter) if vcenter == vmax else None

            x, y = [vmin, vcenter, vmax], [0, 0.5, 1]
            result = ma.masked_array(np.interp(result, x, y),
                                     mask=ma.getmask(result))
            if degen is not None:
                result[degen] = 0.5

        if is_scalar:
            result = np.atleast_1d(result)[0]
        return result

    def autoscale_None(self, A):
        ' autoscale only None-valued vmin or vmax'
        if self.vmin is None and np.size(A) > 0:
            self.vmin = ma.min(A)

        if self.vmax is None and np.size(A) > 0:
            self.vmax = ma.max(A)

        if self.vcenter is None:
            self.vcenter = (self.vmax + self.vmin) * 0.5
