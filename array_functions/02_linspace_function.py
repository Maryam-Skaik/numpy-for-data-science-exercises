"""
linspace() Function
===================
Returns evenly spaced numbers over a specified interval.
Commonly used in plotting and numerical analysis.
"""

import numpy as np

# Basic usage
a = np.linspace(2, 20, num=10)
print(a)

# endpoint=False excludes the stop value
a = np.linspace(2, 20, num=10, endpoint=False)
print(a)

# retstep returns the step size
a, step = np.linspace(2, 20, num=10, retstep=True)
print(a)
print("Step size:", step)

# dtype=int truncates values
a = np.linspace(2, 20, dtype=int)
print(a)

# Default behavior → 50 values
a = np.linspace(2, 20)
print(len(a))
