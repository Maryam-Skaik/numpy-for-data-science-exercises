"""
NumPy Random Number Generation
=============================

This file demonstrates the most commonly used random functions in NumPy.
All results are written as comments for learning and revision purposes.
"""

import numpy as np

# ============================================================
# np.random.random()
# ============================================================

x = np.random.random()
# Example output: 0.5488135

x = np.random.random(2)
# Example output: [0.71518937 0.60276338]

x = np.random.random((2, 2))
# Example output:
# [[0.54488318 0.4236548 ]
#  [0.64589411 0.43758721]]

x = np.random.random((2, 3, 2))
# Example output:
# [[[0.891773   0.96366276]
#   [0.38344152 0.79172504]
#   [0.52889492 0.56804456]]
#
#  [[0.92559664 0.07103606]
#   [0.0871293  0.0202184 ]
#   [0.83261985 0.77815675]]]


# ============================================================
# np.random.randint()
# ============================================================

x = np.random.randint(2, 70)
# Example output: 45

x = np.random.randint(2, 70, size=3)
# Example output: [12 56 33]

x = np.random.randint(5)
# Example output: 3


# ============================================================
# np.random.rand()
# ============================================================

x = np.random.rand()
# Example output: 0.417022

x = np.random.rand(2)
# Example output: [0.72032449 0.00011437]

x = np.random.rand(2, 2)
# Example output:
# [[0.30233257 0.14675589]
#  [0.09233859 0.18626021]]

x = np.random.rand(2, 3, 2)
# Example output: 3D array of floats


# ============================================================
# np.random.randn()
# ============================================================

x = np.random.randn()
# Example output: -0.52817175

x = np.random.randn(2)
# Example output: [ 0.86540763 -2.3015387 ]

x = np.random.randn(2, 2)
# Example output:
# [[ 1.74481176 -0.7612069 ]
#  [ 0.3190391  -0.24937038]]


# ============================================================
# np.random.uniform()
# ============================================================

x = np.random.uniform(4, 20)
# Example output: 14.239

x = np.random.uniform(4, 20, size=3)
# Example output: [ 6.3 18.9 10.4 ]

x = np.random.uniform(6)
# Example output: 3.27

x = np.random.uniform()
# Example output: 0.92


# ============================================================
# np.random.choice()
# ============================================================

x = np.random.choice([2, 4, 8, 19, 90, 7, 20])
# Example output: 19

x = np.random.choice([2, 4, 8, 19, 90, 7, 20], size=3)
# Example output: [ 7 90  4]

x = np.random.choice(40, size=5)
# Example output: [12  3 27 18  5]

x = np.random.choice(
    [2, 4, 8, 19, 90, 7, 20],
    size=3,
    replace=False
)
# Example output: [19  7  4]
