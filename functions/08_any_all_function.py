 # Any Function returns true if any element satisfying the given condition as OR 
# np any(condition)

# All Function returns true if all elements satisfied the given condition as AND 
# np.all(condition)

import numpy as np
from numpy import random 

x = np.random.randint(10, 1000, 5)
x # [123, 589,24,652,359]

np.any(x==500) # false 

np.any(x<100) # true

#############

np.all(x==500) # false 

np.all(x<100) # false

np.all(x>50) # true
