"""
transpose() Function
====================
"""

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
a.T
# [[1 4]
#  [2 5]
#  [3 6]]

# a.shape = (2, 3)
# a.T.shape = (3, 2)

b = np.array([11, 12, 13, 14])
b.T
# Result: [11 12 13 14]
# Shape unchanged
