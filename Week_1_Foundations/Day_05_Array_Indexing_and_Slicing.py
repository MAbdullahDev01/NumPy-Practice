# Problems: Extract rows/columns from a student score matrix.
# Learning Objective: Basic indexing, row/column access.

import numpy as np

# Created 1D and 2D arrays
arr_1D = np.array([1, 3, 4, 3, 1, 0, 9, 8, 5, 7])
print(arr_1D)

arr_2D = np.array([(1, 3, 4, 3, 1, 0, 9, 8, 5, 7), (7, 4, 4, 3, 2, 0, 9, 8, 5, 7)])
print(arr_2D)

# Extracting element at a specific index of a 1D array:
print(arr_1D[2]) 

# Extracting element at a specific index of a 2D array:
print(arr_2D[1, 7])

# Slicing a 1D array:
print(arr_1D[1:7:2])

# Row extraction from a 2D array:
print(arr_2D[1])

# Column extraction from a 2D array:
print(arr_2D[:, 2])