# %%

import sys, os, unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gfuncpy import *


if __name__ == '__main__':
    from math import pi
    import numpy as np

    # expecting ValueError
    # z = Identity(0, 2*pi, 100)
    # sin(x) + cos(z)

    x = Identity.uniform_grid(0, 2*pi, 100)

    f1 = sin(x) + cos(x)
    f2 = sin(x) + sin(x) + cos(x)
    f3 = sin(x) + 2
    f4 = 2 + sin(x)
    f5 = sin(x) - 2
    f6 = 2 - sin(x)
    f7 = -sin(x)
    f8 = (sin(x) + cos(x))/2
        
    # print((3*x+5).root()) # expecting ArithmeticError

    print(f1(pi/2), f2(pi/2), f3(pi/2), f4(pi/2), f5(pi/2), f6(pi/2), f7(pi/2), f8(pi/2), (3*x-5).root())

    f1.plot()
    f2.plot()
    f3.plot()
    f4.plot()
    f5.plot()
    f6.plot()
    f7.plot()




# %%
