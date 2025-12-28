# Unary Operators Those operators which require one operand.

import numpy as np

A = np.array([12,34,50,90])
A.max() # 90
A.min() # 12
A.sum() # 184

##############

B = no.array([[20,25,70], [100,2,30]])
B.max() # 100
B.max(axis=1) # [70,100], max value at each row
B.max(axis=0) # [100,25,70], max value at each column
