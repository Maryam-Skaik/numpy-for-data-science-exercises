# Eye Function: returns a 2-D array, with 1 diagonal and 0 elsewhere.

# E = np.eye(shape, k, dtype)
# if only no. of rows passed, then no. of cols. = no. of rows
# K is index of diagonal, k=0, mean main diagonal; when k=positive, mean upper diagonal; when k=nigative, mean lower diagonal
# default dtype is float

import numpy as np

a = np.eye(3)
a # [[1.0, 0.0, 0.0],
  #  [0.0, 1.0, 0.0],
  #  [0.0, 0.0, 1.0]]

a = np.eye(3, k=0)
a # [[1.0, 0.0, 0.0],
  #  [0.0, 1.0, 0.0],
  #  [0.0, 0.0, 1.0]]

a = np.eye(3, k=1)
a # [[0.0, 1.0, 0.0],
  #  [0.0, 0.0, 1.0],
  #  [0.0, 0.0, 0.0]]

a = np.eye(3, k=-1)
a # [[0.0, 0.0, 0.0],
  #  [1.0, 0.0, 0.0],
  #  [0.0, 1.0, 0.0]]

a = np.eye(3, dtype=int)
a # [[1, 0, 0],
  #  [0, 1, 0],
  #  [0, 0, 1]]

a = np.eye(3, 2)
a # [[1.0, 0.0],
  #  [0.0, 1.0],
  #  [0.0, 0.0]]

###################

a = np.ey(1)
a # [[1.0]]

np.ndim(a) # 2
