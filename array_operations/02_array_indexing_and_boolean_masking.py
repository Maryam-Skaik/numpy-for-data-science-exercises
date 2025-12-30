"""
Array indexing and slicing
Boolean masking in NumPy
"""

import numpy as np

# -----------------------
# Indexing & slicing (1D array)
# -----------------------

a = np.array([1, 2, 3, 4])

# Access single element (0-based index)
print(a[2])  # 3

# Full slice (returns a copy)
print(a[:])  # [1 2 3 4]

# Slice from index 2 to end
print(a[2:])  # [3 4]

# Slice from index 1 to 2 (stop index is exclusive)
print(a[1:2])  # [2]


# -----------------------
# Boolean masking (2D array)
# -----------------------

b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Condition applied element-wise
masked_values = b[b < 5]
print(masked_values)
# [1 2 3 4]
