"""
Creating 1D, 2D, and 3D NumPy arrays
Understanding shape, size, and dimensions
"""

import numpy as np

# -----------------------
# 1D Array
# -----------------------

a1 = np.array([1, 2, 3])
print(a1)  # [1 2 3]

# Type of NumPy array
print(type(a1))  # <class 'numpy.ndarray'>

# Shape: (number of elements,)
print(a1.shape)  # (3,)

# Total number of elements
print(a1.size)   # 3


# -----------------------
# 2D Array (Matrix)
# -----------------------

a2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a2)
# [[1 2 3]
#  [4 5 6]]

# Number of dimensions (rank)
print(a2.ndim)   # 2

# Shape: (rows, columns)
print(a2.shape)  # (2, 3)

# Total elements = rows * columns
print(a2.size)   # 6


# -----------------------
# 3D Array (Tensor)
# -----------------------

a3 = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
])

print(a3)
# [[[1 2 3]
#   [4 5 6]
#   [7 8 9]]]

# Shape: (depth, rows, columns)
print(a3.shape)  # (1, 3, 3)

# Total number of elements
print(a3.size)   # 9
