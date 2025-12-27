# Ones Array - an array in which all values are 1.

import numpy as np

o1 = np.ones(2)
o1 # [1.0,1.0]

# change data type 
o1 = np.ones(2, dtype=int)
o1 # [1,1]

o1.ndim # 1

###############

o2 = np.ones((2, 2))

o2.shape # (2,2)

type(o2) # numpy.ndarray

##############

o3 = np.ones((2,2,2))

o3.size # 8
