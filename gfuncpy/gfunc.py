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
    
    def __add__(self, other):
        f = GridFunction(x=self.x, y=np.copy(self.y))
        if isinstance(other, GridFunction):
            if id(self.x) != id(other.x):
                raise ValueError("The two functions for operation '+' must share the same x grid instance. ")
            f.y += other.y
        else:
            # other is a number
            f.y += other
        return f

    def __sub__(self, other):
        f = GridFunction(x=self.x, y=np.copy(self.y))
        if isinstance(other, GridFunction):
            if id(self.x) != id(other.x):
                raise ValueError("The two functions for operation '-' must share the same x grid instance. ")
            f.y -= other.y
        else:
            # other is a number
            f.y -= other
        return f
    
    def __mul__(self, other):
        f = GridFunction(x=self.x, y=np.copy(self.y))
        if isinstance(other, GridFunction):
            if id(self.x) != id(other.x):
                raise ValueError("The two functions for operation '*' must share the same x grid instance. ")
            f.y *= other.y
        else:
            # other is a number
            f.y *= other
        return f

    def __truediv__(self, other):
        f = GridFunction(x=self.x, y=np.copy(self.y))
        if isinstance(other, GridFunction):
            if id(self.x) != id(other.x):
                raise ValueError("The two functions for operation '/' must share the same x grid instance. ")
            f.y /= other.y
        else:
            # other is a number
            f.y /= other
        return f
        
    def __radd__(self, other):
        '''
        for 2 + cos(x), same for rsub, rmul and rdiv
        '''
        return self.__add__(other)

    def __rsub__(self, other):
        return -self + other
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __rtruediv__(self, other):
        f = GridFunction(x=self.x, y=np.copy(self.y))
        if isinstance(other, GridFunction):
            if id(self.x) != id(other.x):
                raise ValueError("The two functions for operation '/' must share the same x grid instance. ")
            f.y = other.y/f.y
        else:
            # other is a number
            f.y = other/f.y
        return f

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

