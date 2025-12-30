"""
empty() Function
================
Creates arrays without initializing values.
Used when performance is critical.
"""

import numpy as np

# 1D arrays
e = np.empty(3)
print(e)

e = np.empty(3, dtype=int)
print(e)

e = np.empty(3, dtype=object)
print(e)

# 2D arrays
e = np.empty((2, 2))
print(e)

e = np.empty((2, 2), dtype=int)
print(e)

e = np.empty((2, 2), dtype=object)
print(e)

# 3D array
e = np.empty((2, 2, 2))
print(e)
