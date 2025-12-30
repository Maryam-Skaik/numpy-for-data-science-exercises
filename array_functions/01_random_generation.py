"""
Random number generation in NumPy
"""

import numpy as np

# -----------------------
# random()
# -----------------------
# Generates random floats in the range [0, 1)

x = np.random.random()
print(x)

x = np.random.random(2)
print(x)

x = np.random.random((2, 2))
print(x)

x = np.random.random((2, 3, 2))
print(x)


# -----------------------
# randint()
# -----------------------
# Generates random integers
# High value is exclusive

x = np.random.randint(2, 70)
print(x)

x = np.random.randint(2, 70, size=3)
print(x)

x = np.random.randint(5)
print(x)


# -----------------------
# rand()
# -----------------------
# Similar to random(), but shape is passed as separate arguments

x = np.random.rand()
print(x)

x = np.random.rand(2)
print(x)

x = np.random.rand(2, 2)
print(x)

x = np.random.rand(2, 3, 2)
print(x)

# Difference:
# random((2,2)) → tuple
# rand(2,2)     → separate arguments


# -----------------------
# randn()
# -----------------------
# Generates values from standard normal distribution (mean=0, std=1)

x = np.random.randn()
print(x)

x = np.random.randn(2)
print(x)

x = np.random.randn(2, 2)
print(x)

x = np.random.randn(2, 3, 2)
print(x)


# -----------------------
# uniform()
# -----------------------
# Generates random floats in a given range [low, high)

x = np.random.uniform(4, 20)
print(x)

x = np.random.uniform(4, 20, size=3)
print(x)

x = np.random.uniform(6)
print(x)

x = np.random.uniform()
print(x)


# -----------------------
# choice()
# -----------------------
# Randomly selects elements from a sequence

x = np.random.choice([2, 4, 8, 19, 90, 7, 20])
print(x)

x = np.random.choice([2, 4, 8, 19, 90, 7, 20], size=3)
print(x)

x = np.random.choice(40, size=5)
print(x)

x = np.random.choice(7)
print(x)

x = np.random.choice([2, 4, 8, 19, 90, 7, 20], size=3, replace=False)
print(x)
