# Problems: Analyze dataset shape and size
# Learning Objectives: shape, size, itemsize, nbytes

import numpy as np

# Creating arrays
test_case_1 = np.array([(4, 5, 9, 1)])
test_case_2 = np.array([(4, 5, 1), (7, 2,  0)])
test_case_3 = np.array([(4.2, 5.0, 9.1, 1.5, 5.7), (7.6, 2.5, 3.1, 0.4, 9.3), (5.0, 4.1, 3.5, 2.3, 7.0)])

# ndarray.shape is used to check the size of the array in each dimension.
print(test_case_1.shape)
print(test_case_2.shape)
print(test_case_3.shape)

# ndarray.size is used to check the total number of items in the array
print(test_case_1.size)
print(test_case_2.size)
print(test_case_3.size)

# ndarray.itemsize is used to check the size of the item
print(test_case_1.itemsize)
print(test_case_2.itemsize)
print(test_case_3.itemsize)

# ndarray.nbytes is use to check the total number of bytes used by the elements of the array 
print(test_case_1.nbytes)
print(test_case_2.nbytes)
print(test_case_3.nbytes)