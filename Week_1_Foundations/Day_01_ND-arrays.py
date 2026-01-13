# Problem: Create 1D, 2D arrays representing daily temperatures.
# Learning: Objective np.array, ndarray vs lists, ndim, shape.

# What is an ndarray?: ndarray (n-dimensional array) is a container for the same type of data type.
# ndarray.ndim is used to check the number of dimensions of the array.
# ndarray.shape is used to check the size of the array in each dimension.

# Importing the numpy package
import numpy as np

# Creating a 1D array
daily_temps_1D = np.array([28.5, 30.2, 29.8, 31.0])
print(daily_temps_1D)

# Checking the number of dimensions
print(np.ndim(daily_temps_1D))

# Checking the shape
print(np.shape(daily_temps_1D))

# Creating a 2D array
daily_temps_2D = np.array([(26.5, 32.2, 31.8, 33.0), (25.5, 30.8, 31.2, 31.7)])
print(daily_temps_2D)

# Checking the number of dimensions
print(np.ndim(daily_temps_2D))

# Checking the shape
print(np.shape(daily_temps_2D))