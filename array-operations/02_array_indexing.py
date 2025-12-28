# array[srart index : stop index]

import numpy as np

A = np.array([1,2,3,4])
A[2] # 3
A[:] # [1,2,3,4], same as A[0:]
A[2:] # [3,4]
A[1:2] # [2]

################

B = np.array([[1,2,3], [4,5,6]])
B[B<5] # [1,2,3,4]
