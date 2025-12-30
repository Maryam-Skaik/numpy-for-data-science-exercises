"""
Creating arrays filled with zeros
"""

import numpy as np

# -----------------------
# 1D zeros array
# -----------------------

z1 = np.zeros(3)
print(z1)  # [0. 0. 0.]

# Default dtype is float
print(z1.dtype)  # float64

# Change dtype to int
z1_int = np.zeros(3, dtype=int)
print(z1_int)  # [0 0 0]

print(z1_int.ndim)  # 1


# -----------------------
# 2D zeros array
# -----------------------

z2 = np.zeros((3, 3), dtype=int)
print(z2)

print(z2.shape)  # (3, 3)


# -----------------------
# 3D zeros array
# -----------------------

z3 = np.zeros((2, 2, 2))

print(z3.ndim)  # 3
print(z3.size)  # 8
