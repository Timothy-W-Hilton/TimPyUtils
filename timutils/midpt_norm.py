import numpy as np
from matplotlib.colors import Normalize


class MidpointNormalize(Normalize):
    """
    posted by Joe Kington to
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

        x = np.sort(np.concatenate([np.linspace(start=self.vmin,
                                                stop=self.vmax,
                                                num=self.nlevs-1),
                                    [self.midpoint]]))
        y = np.sort(np.concatenate([np.linspace(start=0.0,
                                                stop=1.0,
                                                num=self.nlevs-1),
                                    [0.5]]))
        print 'x, y:', np.dstack([x, y])
        # x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]  #
        return np.ma.masked_array(np.interp(value, x, y))
