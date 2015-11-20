"""Provides class mpl_fig_joiner to join list of
matplotlib.figure.Figure objects together into a single SVG file using
svgutils (https://github.com/btel/svg_utils).  The SVG file may be
converted to other formats using e.g. inkscape.
"""

import svgutils.transform as sg
from svgutils.templates import VerticalLayout
import matplotlib.pyplot as plt


class FigJoiner(object):
    """Joins a list of matplotlib.figure.Figure objects together into
    a single SVG file, and saves the file to disk.
    """

    def __init__(self, figs, fname_svg):
        """class constructor for FigJoiner

        :param figs: list of matplotlib.figure.Figure objects to be joined
        :param fname_svg: full path of the SVG file to be written to disk
        """
        self.figs = figs
        self.fname_svg = fname_svg

    def join(self, verbose=True):
        """
        join matplotlib.figure.Figure objects contained in the object.

        for now assumes that all figures are the same size.
        """

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
        """close all figures contained self
        """
        for f in self.figs:
            plt.close(f)
