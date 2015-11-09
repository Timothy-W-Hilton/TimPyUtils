import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import from_levels_and_colors


def get_cmap_norm(vmin, vmax, midpoint, this_cmap=plt.get_cmap('PuOr')):

    bands_above_mdpt = 3
    bands_below_mdpt = 9

    x = np.concatenate([np.linspace(start=vmin,
                                    stop=midpoint,
                                    num=bands_below_mdpt),
                        np.linspace(start=midpoint,
                                    stop=vmax,
                                    num=bands_above_mdpt)[1:]])
    y = np.concatenate([np.linspace(start=0.0,
                                    stop=0.5,
                                    num=bands_below_mdpt),
                        np.linspace(start=0.5,
                                    stop=1.0,
                                    num=bands_above_mdpt)[1:]])

    mycmap, mynorm = from_levels_and_colors(x, this_cmap(y[1:]))
    return(mycmap, mynorm)


plt.close('all')
data = np.random.randint(-120, 20, [124, 124])
#[data, data2] = np.meshgrid(np.linspace(-100, 20), np.linspace(-100, 20))
fix, ax = plt.subplots(1, 2)
mycmap, mynorm = get_cmap_norm(vmin=-120, vmax=20, midpoint=0.0)
cm = ax[0].pcolormesh(data, norm=mynorm, cmap=mycmap)
plt.colorbar(cm, cax=ax[1])
plt.show()
