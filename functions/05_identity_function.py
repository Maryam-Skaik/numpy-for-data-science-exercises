# Identity Function: returns an identity array as a square array with 1 on the main diagonal and all other elements are 0.

# IA = np.identity(shape, dtype)
# takes single integer value only as shape.
# The no. of rows and no. of cols. will be equal to the given integer value.
# the default datatype is default

import numpy as np

A = np.identity(3)
A # [[1.0, 0.0, 0.0],
  #  [0.0, 1.0, 0.0],
  #  [0.0, 0.0, 1.0]]

A = np.identity(3, dtype=int)
A # [[1, 0, 0],
  #  [0, 1, 0],
  #  [0, 0, 1]]

np.ndim(A) # 2

A.shape (3, 3)

A.size # 9

A * 5
A # [[5, 0, 0],
  #  [0, 5, 0],
  #  [0, 0, 5]]

A * 5.6
A # [[5.6, 0, 0],
  #  [0, 5.6, 0],
  #  [0, 0, 5.6]]
