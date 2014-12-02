from nose.tools import *
import timutils
from timutils import colormap_nlevs

import numpy as np
import matplotlib.pyplot as plt

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def plot_fig(mycmap, mynorm):
    """
    helper function for 
    """
    data = np.random.rand(100, 100)  * 1000
    fig, ax = plt.subplots()
    cm = ax.pcolormesh(data, cmap=mycmap, norm=mynorm)
    plt.colorbar(cm)
    plt.close(fig)

def test_setup_colors_extend():
    """
    make sure number of colors calculated correctly for all values of
    'extend' keyword
    """
    mycmap, mynorm = colormap_nlevs.setup_colormap(
        vmin=200.0, vmax=800.0, extend='max')
    plot_fig(mycmap, mynorm)
    mycmap, mynorm = colormap_nlevs.setup_colormap(
        vmin=200.0, vmax=800.0, extend='min')
    plot_fig(mycmap, mynorm)
    mycmap, mynorm = colormap_nlevs.setup_colormap(
        vmin=200.0, vmax=800.0, extend='both')
    plot_fig(mycmap, mynorm)
    mycmap, mynorm = colormap_nlevs.setup_colormap(
        vmin=200.0, vmax=800.0, extend='neither')
    plot_fig(mycmap, mynorm)

    mycmap, mynorm = colormap_nlevs.setup_colormap_with_zeroval(
        vmin=0.0, vmax=1000.0, nlevs=7, extend='max')
    plot_fig(mycmap, mynorm)
    mycmap, mynorm = colormap_nlevs.setup_colormap_with_zeroval(
        vmin=0.0, vmax=1000.0, nlevs=7, extend='min')
    plot_fig(mycmap, mynorm)
    mycmap, mynorm = colormap_nlevs.setup_colormap_with_zeroval(
        vmin=0.0, vmax=1000.0, nlevs=7, extend='both')
    plot_fig(mycmap, mynorm)
    mycmap, mynorm = colormap_nlevs.setup_colormap_with_zeroval(
        vmin=0.0, vmax=1000.0, nlevs=7, extend='neither')
    plot_fig(mycmap, mynorm)

def test_setup_colormap():
    data = np.random.rand(100, 100)  * 1000
    mycmap, mynorm = colormap_nlevs.setup_colormap(
        vmin=200.0, vmax=800.0, extend='max')
    fig, ax = plt.subplots()
    cm = ax.pcolormesh(data, cmap=mycmap, norm=mynorm)
    plt.colorbar(cm)
    plt.title('setup_colormap example\n'
              'data values 0 to 1000; nlevs=5, vmin=200, vmax=800')
    plt.show()

def setup_colormap_with_zeroval_nlevs(nlevs=7):
    data = np.random.rand(100, 100)  * 1000
    mycmap, mynorm = colormap_nlevs.setup_colormap_with_zeroval(
        vmin=data.min(), 
        vmax=data.max(), 
        nlevs=nlevs,
        extend='neither')
    fig, ax = plt.subplots()
    cm = ax.pcolormesh(data, cmap=mycmap, norm=mynorm)
    plt.colorbar(cm)
    plt.title('setup_colormap_with_zeroval example\n'
              'data values 0 to 1000; nlevs={}'.format(nlevs))
    plt.show()

def test_setup_colormap_with_zeroval_nlevs7():
    setup_colormap_with_zeroval_nlevs(nlevs=5)

def test_setup_colormap_with_zeroval_nlevs5():
    setup_colormap_with_zeroval_nlevs(nlevs=10)
