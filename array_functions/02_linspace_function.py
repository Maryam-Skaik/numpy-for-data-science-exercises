"""
linspace(): returns evenly spaced values over a specified interval
"""

import numpy as np

a = np.linspace(2, 20, num=10)
print(a)

a = np.linspace(2, 20, num=10, endpoint=False)
print(a)

a = np.linspace(2, 20, num=10, endpoint=True)
print(a)

a, step = np.linspace(2, 20, num=10, retstep=True)
print(a)
print(step)

a = np.linspace(2, 20, dtype=int)
print(a)

a = np.linspace(2, 20)
print(len(a))  # default is 50 values
