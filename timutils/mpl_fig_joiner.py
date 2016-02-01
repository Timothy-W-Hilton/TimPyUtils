"""Provides class mpl_fig_joiner to join list of
:class:`matplotlib.figure.Figure` objects together into a single SVG
file using `svgutils <https://github.com/btel/svg_utils>`_.  The SVG
file may be converted to other formats using
e.g. `inkscape <https://inkscape.org/en/>`_.

.. note::
    requires `svgutils <https://github.com/btel/svg_utils>`_
    module to be installed
"""

import svgutils.transform as sg
from svgutils.templates import VerticalLayout
import matplotlib.pyplot as plt


class FigJoiner(object):
    """Joins a list of :class:`matplotlib.figure.Figure` objects together
    into a single SVG file, and saves the file to disk.
    """

    def __init__(self, figs, fname_svg):
        """
        ARGS:
            figs (list): list of :class:`matplotlib.figure.Figure` objects
                to be joined
            fname_svg (string): full path of the SVG file to be written to
                disk

        EXAMPLE:
            >>> import matplotlib.pyplot as plt
            >>> import numpy as np
            >>> figs = []
            >>> for i in range(4):
                figs.append(plt.figure())
                plt.plot(np.random.random(100))
            >>> fj = FigJoiner(figs,
                os.path.join(os.getenv('HOME'), 'plots', 'FJ_test.svg'))
            >>> fj.join()
            >>> fj.close_figs()

        To convert the SVG file to a differeng format, use e.g.\n
            ``inkscape --export-pdf=$HOME/plots/FJ_test.pdf $HOME/plots/FJ_test.svg``

        """
        self.figs = figs
        self.fname_svg = fname_svg

    def join(self, verbose=True):
        """
        join :class:`matplotlib.figure.Figure` objects contained in
        the object.  Currently supports only joining into a single
        horizontal row.

        ARGS:
            verbose (boolean): if True, print a message to stdout as
            each figure is added to the SVG file.

        .. warning::
            for now assumes that all figures are the same size.
        """

        # TODO (thilton@ucmerced.edu): sniff out the figure sizes and
        # size the SVG figure to accommodate all the figures.

        # TODO (thilton@ucmerced.edu): allow user to specify rows,
        # columns of combined SVG figures.

        layout = VerticalLayout()
        sz = map(int, sg.from_mpl(self.figs[0]).get_size())
        sz[1] *= len(self.figs)
        sz = map(str, sz)
        layout.set_size(sz)
        for f in self.figs:
            layout.add_figure(sg.from_mpl(f))

        if verbose:
            print('saving {}'.format(self.fname_svg))
        layout.save(self.fname_svg)

    def close_figs(self):
        """close all figures contained in self.
        """
        for f in self.figs:
            plt.close(f)
