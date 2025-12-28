# VStack combines the array vertically 
# HStack combines the array Horizontally 

import numpy as np

A = np.array([1,2,3])
B = no.array([4,5,6])

np.vstack((A,B))
# [[1,2,3],
# [4,5,6]]

np.hstack((A,B))
# [1,2,3,4,5,6]

############

C = np.array([[1,2,3],[4,5,6]])
D = np.array([[7,8,9],[10,11,12]])

np.vstack((C,D))
#  [[1,2,3],
#   [4,5,6],
#   [7,8,9]
#   [10,11,12]]

np.hstack((C,D))
# [[1,2,3,4,5,6],
#  [7,8,9,10,11,12]]
