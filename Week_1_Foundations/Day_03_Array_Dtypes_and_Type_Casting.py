# Problems: Convert integer arrays to float and boolean.
# Learning Objectives: dtype, astype, type casting.

import numpy as np

# ndarray.dtype is used to check the data type of an array

# Integer
arr_int = np.array([4, 6, 0, 1], dtype=int)
print(arr_int.dtype)

# Float
arr_float = np.array([4.5, 6.1, 0, 1.3], dtype=float)
print(arr_float.dtype)

# String
arr_string = np.array(["hi", "bye", "world"], dtype=str)
print(arr_string.dtype)

# Boolean
arr_boolean = np.array([True, False], dtype=bool)
print(arr_boolean.dtype)

# ndarray.astype is used to cast one data type to another 
print(arr_float.astype("int"))  # Output: [4, 6, 0, 1] (Note: it truncates, doesn't round)
print(arr_float.astype("int").dtype)
