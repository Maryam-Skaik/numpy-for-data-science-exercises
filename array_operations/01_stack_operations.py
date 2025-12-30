"""
Stacking NumPy arrays:
- vstack  → vertical stacking (row-wise)
- hstack  → horizontal stacking (column-wise / concatenation)
"""

import numpy as np

# -----------------------
# Stacking 1D arrays
# -----------------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Vertical stacking:
# Converts 1D arrays into rows of a 2D array
v_stacked_1d = np.vstack((a, b))
print(v_stacked_1d)
# [[1 2 3]
#  [4 5 6]]

# Horizontal stacking:
# Concatenates arrays along the same row
h_stacked_1d = np.hstack((a, b))
print(h_stacked_1d)
# [1 2 3 4 5 6]


# -----------------------
# Stacking 2D arrays
# -----------------------

c = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

d = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

# Vertical stacking (adds rows)
v_stacked_2d = np.vstack((c, d))
print(v_stacked_2d)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# Horizontal stacking (adds columns)
h_stacked_2d = np.hstack((c, d))
print(h_stacked_2d)
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]
