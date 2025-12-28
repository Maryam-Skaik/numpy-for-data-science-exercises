# Linespace Function returns evenly(linearly) spaced values within a given interval.

# np.linespace(start_value, stop_value, num=50, endpoint=False, retstep=True, dtype=None)
# by default it shows 50 values.

import numpy as np

A = np.linespace(2, 20, num=10)
A # [2. 4. 6. 8. 10. 12. 14. 16. 18. 20.]

A = np.linespace(2, 20, num=10, endpoint=False)
A # [2. 3.8 6.4 9.1 11. 12.8 14.6 16.4 17.5 18.]

A = np.linespace(2, 20, num=10, endpoint=True)
A # [2. 4. 6. 8. 10. 12. 14. 16. 18. 20.]

A = np.linespace(2, 20, num=10, endpoint=True, retstep=True)
A # ([2. 4. 6. 8. 10. 12. 14. 16. 18. 20.], 2.0)

A = np.linespace(2, 20, num=10, endpoint=True, retstep=False)
A # [2. 4. 6. 8. 10. 12. 14. 16. 18. 20.]

A = np.linespace(2, 20, num=10, endpoint=True, retstep=False, dtype=int)
A # [2 4 6 8 10 12 14 16 18 20]

A = np.linespace(2, 20)
# print 50 values between 2 and 20

