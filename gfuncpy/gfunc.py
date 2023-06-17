import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

class GridFunction:
    '''
    Assuming x is sorted and y is in the corresponding order
    '''
    def __init__(self, x=None, y=None):
        if x is not None and y is not None and not (hasattr(x, '__len__') and hasattr(y, '__len__') and len(x)==len(y)):
            raise ValueError('x and y must be array-like object with the same length')
        self.x = x
        self.y = y
    
    @classmethod
    def from_dataframe(cls, df, y, x=None):
        '''
        must specify y (a column name)
        if x is not specified will use index of the DataFrame
        '''
        f = cls()
        f.y = df[y].values
        
        if x is None:
            f.x = df.index.values
        else:
            f.x = df[x].values
        return f
        
    @classmethod
    def from_series(cls, ss):
        f = cls()
        f.x = ss.index.values
        f.y = ss.values
        return f
        
    def root(self):
        '''
        Linear search from the left until the first root is found, slow but convenient API. 
        '''
        if self.y[0]==0:
            return self.x[0]
        elif self.y[0] < 0:
            idx = np.argmax(self.y > 0)
        elif self.y[0] > 0:
            idx = np.argmax(self.y < 0)

        if idx==0:
            raise ArithmeticError("It appears there is no root in the range of this function's x grid. ")

        x0, x1, y0, y1 = self.x[idx-1], self.x[idx], self.y[idx-1], self.y[idx]
        return x0 + (x1-x0)*abs(y0/(y1-y0))
        
    def __call__(self, x):
        '''
        x can be a list
        '''
        intp = interpolate.interp1d(self.x, self.y)
        return intp(x)
        
    def _apply_operator(self, other, operator, reverse=False):
        f = GridFunction(x=self.x, y=np.copy(self.y))
        if isinstance(other, GridFunction):
            if id(self.x) != id(other.x):
                raise ValueError(f"The two functions for operation '{operator}' must share the same x grid instance.")
            if reverse:
                f.y = operator(other.y, f.y)
            else:
                f.y = operator(f.y, other.y)
        else:
            if reverse:
                f.y = operator(other, f.y)
            else:
                f.y = operator(f.y, other)
        return f

    
    def __add__(self, other):
        return self._apply_operator(other, np.add)
    
    def __sub__(self, other):
        return self._apply_operator(other, np.subtract)
    
    def __mul__(self, other):
        return self._apply_operator(other, np.multiply)
    
    def __truediv__(self, other):
        return self._apply_operator(other, np.divide)

    def __pow__(self, other):
        return self._apply_operator(other, np.power)                

    def __radd__(self, other):
        return self._apply_operator(other, np.add, reverse=True)

    def __rsub__(self, other):
        return self._apply_operator(other, np.subtract, reverse=True)

    def __rmul__(self, other):
        return self._apply_operator(other, np.multiply, reverse=True)

    def __rtruediv__(self, other):
        return self._apply_operator(other, np.divide, reverse=True)

    def __rpow__(self, other):
        return self._apply_operator(other, np.power, reverse=True)


    def __neg__(self):
        return GridFunction(self.x, -np.copy(self.y))

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