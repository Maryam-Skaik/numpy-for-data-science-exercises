# Transpose Function convert rows into columns, and columns into rows.

# A = np.transpose(array) , or, array.T

import numpy as np

A = no.array([[1,2,3],[4,5,6]])

A.T # [[1,4]
    #  [2,5]
    #  [3,6]]

A.shape # (2,3)
A.T.shape # (3,2)

np.transpose(A)

###############

# 1-D array

B = np.array([11,12,13,14])
B # [11,12,13,14]

B.T # [11,12,13,14]

B.shape # (4,)

B.T.shape # (4,)

