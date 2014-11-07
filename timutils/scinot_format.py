import numpy as np

def scinot_format(x,pos=None):
    """
    format its argument x into scientific notation, using "mn x 10^ex"
    notation, not "mn e ex" notation.

    Code provided 19 Oct 2010 by Jonathan Slavin to the matplotlib -
    users listserve.
    http://matplotlib.1069221.n5.nabble.com/scientific-notation-in-ticklabels-for-linear-plot-td25338.html

    USAGE EXAMPLE:
    import matplotlib.pyplot as plt 
    import numpy as np 
    from matplotlib.ticker import FuncFormatter 

    x = np.linspace(0.,2.,10)*1.E18 
    y = 2.*(x/1.E18) - 1. 
    fig = plt.figure() 
    ax = fig.add_subplot(111) 
    ax.plot(x,y) 
    ax.xaxis.set_major_formatter(FuncFormatter(sci_not_format_func)) 
    plt.show() 
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
