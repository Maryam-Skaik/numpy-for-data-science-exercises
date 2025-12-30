"""
eye() Function
==============
Creates a 2D array with ones on a specified diagonal.
"""

import numpy as np

# Main diagonal
a = np.eye(3)
print(a)

# Upper diagonal
a = np.eye(3, k=1)
print(a)

# Lower diagonal
a = np.eye(3, k=-1)
print(a)

# Integer dtype
a = np.eye(3, dtype=int)
print(a)

# Rectangular matrix
a = np.eye(3, 2)
print(a)

# Dimension check
print(a.ndim)
