import copy
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

class GridFunction:
    def __init__(self, x=None, y=None):
        if x is not None and y is not None and not (hasattr(x, '__len__') and hasattr(y, '__len__') and len(x)==len(y)):
            raise ValueError('x and y must be array-like object with the same length')
        self.x = x
        self.y = y
    
    def __call__(self, x):
        '''
        x can be a list
        '''
        intp = interpolate.interp1d(self.x, self.y)
        return intp(x)
    
    def __add__(self, other):

        f = copy.deepcopy(self)
        
        if isinstance(other, GridFunction):
            if id(self.x) != id(other.x):
                raise ValueError("The two functions for the operation must share the same x grid instance. ")
            f.y += other.y
        else:
            # other is a number
            f.y += other

        return f

    def plot(self, style='-'):
        plt.plot(self.x, self.y, style)
        
class Identity(GridFunction):
    @classmethod
    def uniform_grid(cls, a, b, n):  
        # this is how multiple constructors can be defined in python
        # https://stackoverflow.com/questions/2164258/is-it-not-possible-to-define-multiple-constructors-in-python
        f = cls()
        f.x = np.linspace(a, b, n+1)
        f.y = np.linspace(a, b, n+1)
        return f
