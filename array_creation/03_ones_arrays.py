"""
Creating arrays filled with ones
"""

import numpy as np

# -----------------------
# 1D ones array
# -----------------------

o1 = np.ones(2)
print(o1)  # [1. 1.]

# Change data type
o1_int = np.ones(2, dtype=int)
print(o1_int)  # [1 1]

print(o1_int.ndim)  # 1


# -----------------------
# 2D ones array
# -----------------------

o2 = np.ones((2, 2))
print(o2)

print(o2.shape)  # (2, 2)
print(type(o2))  # numpy.ndarray


# -----------------------
# 3D ones array
# -----------------------

o3 = np.ones((2, 2, 2))
print(o3.size)  # 8
