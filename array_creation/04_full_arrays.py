"""
Creating full arrays (constant value arrays)
"""

import numpy as np

# -----------------------
# 1D full array
# -----------------------

f1 = np.full(3, 21)
print(f1)  # [21 21 21]

# Change dtype to float
f1_float = np.full(3, 21, dtype=float)
print(f1_float)  # [21. 21. 21.]

print(f1.ndim)  # 1


# -----------------------
# 2D full array
# -----------------------

f2 = np.full((2, 2), 11.5)
print(f2)

# String dtype
f2_str = np.full((2, 2), 11.5, dtype=str)
print(f2_str)

# Integer dtype (value is truncated)
f2_int = np.full((2, 2), 11.5, dtype=int)
print(f2_int)

print(f2.shape)  # (2, 2)


# -----------------------
# 3D full array
# -----------------------

f3 = np.full((2, 5, 2), "maryam")

print(f3.ndim)  # 3
print(f3.size)  # 20
