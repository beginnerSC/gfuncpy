# %%

from gfuncs import Identity
from ufuncs import *

if __name__ == '__main__':
    from math import pi

    # expecting ValueError
    # z = Identity(0, 2*pi, 100)
    # sin(x) + cos(z)

    # can't find a way for this to work: h = 2 + cos(x)
    # but there is a way: 2*np.arange(5) works

    x = Identity.uniform_grid(0, 2*pi, 100)
    f = sin(x) + cos(x)
    g = sin(x) + sin(x) + cos(x)
    h = cos(x) + 2
    
    print(f(pi/2), g(pi/2), h(pi/2))
    f.plot()
    g.plot()


# %%
