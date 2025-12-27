# An array in which all values are 0.
# ZA = np.zeros(shape, dtype)

import numpy as np

z1 = np.zeros(3)
z1 # [0.0,0.0,0.0], float is the default data type, but we can change it.

z1 = np.zeros(3, dtype = int)
z1 # [0,0,0]

type(z1) # numpy.ndarray

np.ndim(z1) # 1

################

z2 = np.zeros((3,3)) # no. of rows, cols
z2 # [[0.0,0.0,0.0],
   #  [0.0,0.0,0.0],
   #  [0.0,0.0,0.0]]

z2 = no.zeros((3,3), dtype=int)

z2.shape # (3,3)

##################

z3 = np.zeros((2,2,2))

z3.ndim # 3

z3.size # 8
