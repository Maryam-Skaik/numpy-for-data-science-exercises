# Diagonal Function it's used to extract the diagonal elements of an array, or used to construct a new diagonal array.

# A = np.diag(a, k)
# if a is a 2-D array,it extract the diagonal elements.
# if a is a 1-D array, it construct a 2-D array with elements of a in diagonal.
# by default k=0

import numpy as np


A = np.array([1,2], [3,4])
A.ndim # 2

# extract the diagonal elements
np.diag(A) # [1,4]

#############

B = np.array([1,2,3])

np.diag(B) # [[1,0,0],
           #  [0,2,0],
           #  [0,0,3]]

