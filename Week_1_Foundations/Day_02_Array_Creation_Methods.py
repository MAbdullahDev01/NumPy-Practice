# Problems: Generate arrays using zeros, ones, ranges.
# Learning Objective: np.zeros, np.ones, np.arange, np.linspace.

import numpy as np

# np.zeros can be used to make an array of 0s

zeros_1D = np.zeros(1)
zeros_2D = np.zeros((2, 3))
zeros_3D = np.zeros((2, 2, 2))

print(zeros_1D)
print(zeros_2D)
print(zeros_3D)

# np.ones can be used to make an array of 1s

ones_1D = np.ones(1)
ones_2D = np.ones((2, 5))
ones_3D = np.ones((7, 1, 3))

print(ones_1D)
print(ones_2D)
print(ones_3D)

# np.arange can be used to create an array with a range of elements
# np.arange(start, stop, jump)

range_1D = np.arange(0, 10, 2)

print(range_1D)

# np.linspace can be used to create an array with values that are spaced linearly in a specified interval

temperature_range = np.linspace(-20, 10, 7)

print(temperature_range)