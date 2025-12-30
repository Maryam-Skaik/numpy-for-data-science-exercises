"""
empty() Function
================
Creates arrays without initializing values.
"""

import numpy as np

e = np.empty(3)
# Result: random garbage values

e = np.empty(3, dtype=int)
# Result: random integers

e = np.empty(3, dtype=object)
# Result: [None None None]

e = np.empty((2, 2))
# Result: uninitialized 2D array

e = np.empty((2, 2), dtype=int)
# Result: random integers

e = np.empty((2, 2), dtype=object)
# Result:
# [[None None]
#  [None None]]

e = np.empty((2, 2, 2))
# Result: uninitialized 3D array
