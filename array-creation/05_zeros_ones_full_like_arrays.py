import numpy as np
from numpy import random

# One Likes Array: return an array of Ones, with the same shape & type as the given array

# A = np.ones_like(array, dtype)

A = np.array([5,21,70])

# creating ones array from A
B = np.ones_like(A)
B # [1, 1, 1], same shape and datatype as A

C = np.random.random((2,2))
C # [[0.7852, 0.96518],
  #  [0.4562, 0.6523]]

D = np.ones_like(C)
D # [[1.0, 1.0],
  #  [1.0, 1.0]]

D = np.ones_like(C, dtype=int)
D # [[1, 1],
  #  [1, 1]]

#########################

# Zero Likes array: returns an array of zeros, with same shape & type as the given array

# A = np.zeros_like(array, dtype)

A = np.array([5,21,70])

# creating zeros array from A
B = np.zeros_like(A)
B # [0, 0, 0]

C = np.random.random((2,2))
C # [[0.7852, 0.96518],
  #  [0.4562, 0.6523]]

D = np.zeros_like(C)
D # [[0.0, 0.0],
  #  [0.0, 0.0]]

D = np.zeros_like(C, dtype=int)
D # [[0, 0],
  #  [0, 0]]

###########################

# Full Likes array: returns an array of constant element, with same shape & type as the given array

# A = np.full_like(array, fill_value, dtype)

A = np.array([5,21,70])

# creating full array from A
B = np.full_like(A, 5)
B # [5, 5, 5]

C = np.random.random((2,2))
C # [[0.7852, 0.96518],
  #  [0.4562, 0.6523]]

D = np.full_like(C, 40)
D # [[40.0, 40.0],
  #  [40.0, 40.0]]

D = np.full_like(C, -40, dtype=int)
D # [[-40, -40],
  #  [-40, -40]]
