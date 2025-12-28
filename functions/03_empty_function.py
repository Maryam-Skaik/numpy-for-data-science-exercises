# Empty Function: used to create an array of arbitrary values, of given shape and datatype, wthout initializinf the entire.

# E = np.empty(shape, dtype)
# shape can given in list or truple form.
# default datatype is float

import numpy as np

e = np.empty(3)
e # [2.5874563e-308, 9.745632e-307, 7.56985e-317]

e = np.empty(3, dtype=int)
e # [49842, 789521, 789632]

e = np.empty(3, dtype=object)
e # [None, None, None]

########################

e = np.empty((2,2))
e # [[0.0, 0.0],
  #  [0.0, 0.0]]

e = np.empty((2,2), dtype=int)
e # [[0, 145],
  #  [0, 0]]

e = np.empty((2,2), dtype=object)
e # [[None, None],
  #  [None, None]]

########################

e = np.empty([2,2,2])

e = np.empty([2,2,2], dtype=int)

e = np.empty([2,2,2], dtype=object)
