.. GFuncPy documentation master file, created by
   sphinx-quickstart on Fri Jul 18 21:05:30 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

GFuncPy documentation
=====================

GFuncPy is a powerful numerical and plotting library tailored for research and educational applications. It represents functions in discrete form using $x$ and $y$ values, allowing for straightforward arithmetic operations and numerical analysis. This intuitive approach greatly simplifies complex computations, making quantitative research more accessible and productive.

Here's an example showcasing the simplicity and expressiveness of GFuncPy:

```python
from gfuncpy import Identity

x = Identity.uniform_grid(0, 2, 1000)

(x**2 - 2).root()
```

This example calculates the root of $x^2 - 2$ within the range $[0, 2]$, yielding $\sqrt{2} \approx 1.4142135\ldots$. Dive into the Quick Start guide for more examples and detailed instructions.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quick_start
