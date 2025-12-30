"""
identity() Function
===================
Creates a square identity matrix.
"""

import numpy as np

a = np.identity(3)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

a = np.identity(3, dtype=int)
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]

# a.ndim = 2
# a.shape = (3, 3)
# a.size = 9

# a * 5 =
# [[5 0 0]
#  [0 5 0]
#  [0 0 5]]

# a * 5.6 =
# [[5.6 0.  0. ]
#  [0.  5.6 0. ]
#  [0.  0.  5.6]]
