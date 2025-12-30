"""
Aggregation (reduction) operations in NumPy

These operations reduce an array to a single value
or reduce along a specific axis.
"""

import numpy as np

# -----------------------
# Aggregation on 1D array
# -----------------------

a = np.array([12, 34, 50, 90])

# Maximum value in the array
print(a.max())  # 90

# Minimum value in the array
print(a.min())  # 12

# Sum of all elements
print(a.sum())  # 186


# -----------------------
# Aggregation on 2D array
# -----------------------

b = np.array([
    [20, 25, 70],
    [100, 2, 30]
])

# Maximum value in the entire array
print(b.max())  # 100

# Axis explanation:
# axis=0 → operate column-wise
# axis=1 → operate row-wise

# Maximum value in each row
print(b.max(axis=1))  # [70 100]

# Maximum value in each column
print(b.max(axis=0))  # [100 25 70]
