# The random module contains functions which are used for generating random numbers.

import numpy as np
from numpy import random

# Random Function: it return random numbers between 0 and 1.

x = np.random.random() # first random is random module, second is random function
x # 0.57412......

x = np.random.random(2)
x # [0.745631, 0.6974120]

x = np.random.rondom((2,2))
x # [[0.745631, 0.6974120],
  #  [0.951235, 0.5713698]]

x = np.random.random((2,3,2))

#######################

# Randint Function: generate random integer number(s) between given range.
# default range start from 0.
# numbers can repeat

x = np.random.randint(2,70)
x # 69

x = np.random.randint(2,70, 3)
x # [4,19,8]

x = np.random.randint(5)
x # 4

#######################

# Rand Function: it return random float numbers between 0 and 1.

x = np.random.rand()
x # 0.58712...

x = np.random.rand(2)
x # [0.745631, 0.6974120]

x = np.random.rand(2,2)
x # [[0.745631, 0.6974120],
  #  [0.951235, 0.5713698]]

x = np.random.rand(2,3,2)

# difference between np.random.rondom((2,2)) and np.random.rand(2,2), random need more () to return an array, while rand didn't

#######################

# Randn Function: it return random float numbers (positive and nigative both) in form of array.

x = np.rando.randn()
x # -0.51478...

x = np.random.randn(2)
x # [0.745631, -0.6974120]

x = np.random.randn(2,2)
x # [[-0.745631, -0.6974120],
  #  [-0.951235, 0.5713698]]

x = np.random.randn(2,3,2)

#######################

# Uniform Function: it return random float numbers between given range of values.
# random numbers can't repeat.
# by default, range start from 0.
# if nothing passed in (), it will return float number between 0 and 1.

x = np.random.uniform(4, 20)
x # 15.8745632

x = np.random.uniform(4, 20, 3)
x # [4.74125, 8.789632, 17.7896321]

x = np.random.uniform(6)
x # 4.984126

x = np.random.uniform()
x # 0.984126

#######################

# Choice Function: it returns random integer number(s) from the given sequence.
# range start from 0 by default.
# if only 1 element passed, then it will return a number between 0 and that number.
# by default, replace = true, mean numbers can repeat.

x = np.random.choice([2,4,8,19,90,7,20])
x # 90

x = np.random.choice([2,4,8,19,90,7,20], 3)
x # [90,2,90]

x = np.random.choice(40,5)
x # [19,20,7,3,10]

x = np.random.choice(7)
x # 6

x = np.random.choice([2,4,8,19,90,7,20], size=3)
x # [90,2,90]

x = np.random.choice([2,4,8,19,90,7,20], size=3, replace=False)
x # [90,2,8]

x = np.random.choice([2,4,8,19,90,7,20], size=40, replace=False)
x # error

x = np.random.choice([2,4,8,19,90,7,20], size=40, replace=True)
# worked

