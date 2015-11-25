import numpy as np


def scinot_format(x):
    """format a numeric parameter x into scientific notation for use
    in plot labels.

    Formats the parameter using :math:`123 \\times 10^{{-456}}`
    notation, not :math:`123\\mathrm{e}-456` notation.

    ARGS:
        x (real): the value to be formatted

    YIELDS:
        a string containing x, formatted for use in matplotlib plot
            labels

    EXAMPLE:
        >>> from timutils.scinot_format import scinot_format
        >>> print scinot_format(1.234e-5)

        >>> import matplotlib.pyplot as plt
        >>> import numpy as np
        >>> from matplotlib.ticker import FuncFormatter
        >>> from timutils.scinot_format import scinot_format
        >>> def formatter(val, tickpos):
                return(scinot_format(val))
        >>> y = np.linspace(0.,2.,10)
        >>> x = y * 1e18
        >>> fig = plt.figure()
        >>> ax = fig.add_subplot(111)
        >>> ax.plot(x,y)
        >>> ax.xaxis.set_major_formatter(FuncFormatter(formatter))
        >>> plt.show()

        >>> import matplotlib.pyplot as plt
        >>> import numpy as np
        >>> from matplotlib.ticker import FuncFormatter
        >>> from timutils.scinot_format import scinot_format
        >>> def formatter(val, tickpos):
                return(scinot_format(val))
        >>> data = np.random.random((100, 100)) * 1e-12
        >>> fig, ax = plt.subplots()
        >>> cm = ax.pcolormesh(data)
        >>> plt.colorbar(cm, format=FuncFormatter(formatter))
        >>> plt.show()


    Code posted 19 Oct 2010 by Jonathan Slavin to the `matplotlib -
    users listserve
    <http://matplotlib.1069221.n5.nabble.com/scientific-notation-in-ticklabels-for-linear-plot-td25338.html>`_

    """
    if x == 0:
        s = '0'
    else:
        xp = int(np.floor(np.log10(np.abs(x))))
        mn = x/10.**xp
        # Here we truncate to 2 significant digits -- may not be enough
        # in all cases
        s = '$'+str('%.1f'%mn) +'\\times 10^{'+str(xp)+'}$'
    return s
