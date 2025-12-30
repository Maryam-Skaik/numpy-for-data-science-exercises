"""
NumPy Random Module
------------------
This file demonstrates the most common random number generation
functions used in NumPy for data science and simulations.

Important note:
Random numbers are NOT truly random — they are pseudo-random,
generated using algorithms.
"""

import numpy as np


# ============================================================
# 1. np.random.random()
# ============================================================
# Generates random floating-point numbers in the range:
#   0.0 <= number < 1.0
#
# If no shape is given → returns a single float
# If shape is given → returns a NumPy array

x = np.random.random()
print(x)  # single random float between 0 and 1

x = np.random.random(2)
print(x)  # 1D array with 2 random floats

x = np.random.random((2, 2))
print(x)  # 2D array (2 rows, 2 columns)

x = np.random.random((2, 3, 2))
print(x)  # 3D array


# ============================================================
# 2. np.random.randint()
# ============================================================
# Generates random integers
#
# Syntax:
# np.random.randint(low, high, size)
#
# - low is inclusive
# - high is exclusive
# - numbers CAN repeat

x = np.random.randint(2, 70)
print(x)  # one integer between 2 and 69

x = np.random.randint(2, 70, size=3)
print(x)  # array of 3 integers

x = np.random.randint(5)
print(x)  # integer between 0 and 4


# ============================================================
# 3. np.random.rand()
# ============================================================
# Similar to np.random.random()
# Difference:
# - rand() takes shape as separate arguments
# - random() takes shape as a tuple

x = np.random.rand()
print(x)

x = np.random.rand(2)
print(x)

x = np.random.rand(2, 2)
print(x)

x = np.random.rand(2, 3, 2)
print(x)

# Comparison:
# np.random.random((2,2))  ✅ tuple
# np.random.rand(2,2)      ✅ separate arguments


# ============================================================
# 4. np.random.randn()
# ============================================================
# Generates numbers from the STANDARD NORMAL DISTRIBUTION:
# - Mean = 0
# - Standard deviation = 1
#
# Values can be positive or negative

x = np.random.randn()
print(x)

x = np.random.randn(2)
print(x)

x = np.random.randn(2, 2)
print(x)

x = np.random.randn(2, 3, 2)
print(x)


# ============================================================
# 5. np.random.uniform()
# ============================================================
# Generates random floating-point numbers from a given range
#
# Syntax:
# np.random.uniform(low, high, size)
#
# - low is inclusive
# - high is exclusive
# - values MAY repeat (important correction)

x = np.random.uniform(4, 20)
print(x)

x = np.random.uniform(4, 20, size=3)
print(x)

x = np.random.uniform(6)
print(x)  # between 0 and 6

x = np.random.uniform()
print(x)  # between 0 and 1


# ============================================================
# 6. np.random.choice()
# ============================================================
# Randomly selects elements from a sequence or range
#
# By default:
# - replace=True  → values can repeat
# - range starts from 0 if an integer is given

x = np.random.choice([2, 4, 8, 19, 90, 7, 20])
print(x)

x = np.random.choice([2, 4, 8, 19, 90, 7, 20], size=3)
print(x)

x = np.random.choice(40, size=5)
print(x)  # values from 0 to 39

x = np.random.choice(
    [2, 4, 8, 19, 90, 7, 20],
    size=3,
    replace=False
)
print(x)  # no repetition allowed
