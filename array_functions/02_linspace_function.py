"""
linspace() Function
===================
Returns evenly spaced numbers over a specified interval.
"""

import numpy as np

a = np.linspace(2, 20, num=10)
# Result:
# [ 2.  4.  6.  8. 10. 12. 14. 16. 18. 20.]

a = np.linspace(2, 20, num=10, endpoint=False)
# Result:
# [ 2.   3.8  5.6  7.4  9.2 11.  12.8 14.6 16.4 18.2]

a, step = np.linspace(2, 20, num=10, retstep=True)
# a:
# [ 2.  4.  6.  8. 10. 12. 14. 16. 18. 20.]
# step:
# 2.0

a = np.linspace(2, 20, dtype=int)
# Result:
# [ 2  2  4  6  8 10 12 14 16 18]

a = np.linspace(2, 20)
# len(a) = 50
