"""
eye() Function
==============
Creates a 2D array with ones on a specified diagonal.
"""

import numpy as np

a = np.eye(3)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

a = np.eye(3, k=1)
# [[0. 1. 0.]
#  [0. 0. 1.]
#  [0. 0. 0.]]

a = np.eye(3, k=-1)
# [[0. 0. 0.]
#  [1. 0. 0.]
#  [0. 1. 0.]]

a = np.eye(3, dtype=int)
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]

a = np.eye(3, 2)
# [[1. 0.]
#  [0. 1.]
#  [0. 0.]]

# a.ndim = 2
