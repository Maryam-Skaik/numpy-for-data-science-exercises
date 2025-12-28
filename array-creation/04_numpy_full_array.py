# Full Array - an array in which all values are the same (constant).

# F = np.full(shape, fill_value)
# default data type is integer, but can change it to float and string 

import numpy as np

f1 = np.full(3, 21)
f1 # [21,21,21]

# change data type to float 
f1 = np.full(3, 21, dtype=float)
f1 # [21.0,21.0,21.0]

type(f1) # numpy.ndarray

f1.ndim # same as np.ndim(f1) # 1

##################

f2 = np.full((2,2), 11.5)
f2 # [[11.5,11.5]
   #  [11.5,11.5]]

# change data type to string
f2 = np.full((2,2), 11.5, dtype=str)
f2 # [['11','11']
   #  [11,'11']]

# change data type to int
f2 = np.full((2,2), 11.5, dtype=int)
f2 # [[11,11]
   #  [11,11]]

f2.shape # (2,2)

################

f3 = no.full([2,5,2], 'maryam')

f3.ndim # 3

f3.size # 20
