"""
Using *_like functions:
- ones_like
- zeros_like
- full_like
"""

import numpy as np

# -----------------------
# ones_like
# -----------------------

a = np.array([5, 21, 70])

ones_from_a = np.ones_like(a)
print(ones_from_a)  # [1 1 1]

random_matrix = np.random.random((2, 2))
print(random_matrix)

ones_from_random = np.ones_like(random_matrix)
print(ones_from_random)

ones_int = np.ones_like(random_matrix, dtype=int)
print(ones_int)


# -----------------------
# zeros_like
# -----------------------

zeros_from_a = np.zeros_like(a)
print(zeros_from_a)  # [0 0 0]

zeros_from_random = np.zeros_like(random_matrix)
print(zeros_from_random)

zeros_int = np.zeros_like(random_matrix, dtype=int)
print(zeros_int)


# -----------------------
# full_like
# -----------------------

full_from_a = np.full_like(a, 5)
print(full_from_a)

full_from_random = np.full_like(random_matrix, 40)
print(full_from_random)

full_int = np.full_like(random_matrix, -40, dtype=int)
print(full_int)
