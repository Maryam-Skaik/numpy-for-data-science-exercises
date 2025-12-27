import numpy as np

A1 = np.Array([1, 2, 3]) # 1-D array
print(A1) # [1 2 3]

type(A1) # numpy.ndarray

A1.shape # (3,)

A1.size # 3

######################

A2 = np,array([[1,2,3], [4,5,6]])
print(A2) #[[1 2 3]
          # [4 5 6]]

A2.ndim # 2, to check dimensions(rank) of the array

A2.shape # (2, 3), 2 rows, 3 cols

A2.size # 6, no. of elements

#######################

A3 = np.array([[[1,2,3], [4,5,6], [7,8,9]]])

print(A3) # [[[1 2 3]
          #   [4 5 6]
          #   [7 8 9]]]

A3.shape # (1, 3, 3)

A3.size # 9
