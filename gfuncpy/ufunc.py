'''
Must create new instance or otherwise the following will not return 1 as it's supposed to

from math import pi

f = sin(x) + cos(x)
f(pi/2)
'''

import numpy as np
from .gfunc import GridFunction

def sin(fnc):   
    return GridFunction(fnc.x, np.sin(fnc.y))

def cos(fnc):   
    return GridFunction(fnc.x, np.cos(fnc.y))
