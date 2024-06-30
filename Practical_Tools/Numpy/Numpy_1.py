import numpy as np

# create 1d Array
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)

# check a type
print(type(arr_1d))

# Check dimension of an array
print(arr_1d.ndim)

# create 2d Array
arr_2d = np.array([[8, 2, 0, 1], [7, 8, 9, 4], [1, 2, 3, 4]])
print(arr_2d)

# find dimension of an array
print(arr_2d.ndim)

# find the size of an array (no of an element)
array_size = arr_2d.size
print("array size :", array_size)

# find shape and dta type of array
print(arr_2d.shape)
print(arr_2d.dtype)

# --------------------------------------------------------------------------

# make a row of ones
print("Ones : ", np.ones(5))  # 5 column

# Create a 5x5 matrix filled with ones, but all values are of float type
ones_matrix = np.ones((5, 5))  # Row 5 and 5 col

# Print the created matrix
print(ones_matrix)
print(ones_matrix.dtype)

# ------------------------------------------------------------------------

# make a row of eros
print(np.zeros(5))
# Create a 5x5 matrix filled with zeros, but all value is of float type
zeros_matrix = np.zeros((5, 5))

# Print the created matrix
print(zeros_matrix)
print(zeros_matrix.dtype)


# This is an int type matrix,
# by default ones and zeros function creates a float type of matrix means 0. or 1.


int_matrix = np.ones((3, 4), dtype=int)
print(int_matrix)

# Create a multi-dimension array with random value

# empty this function creates random values, this will give float value
empty_matrix = np.empty((3, 4))
print(empty_matrix)

# But if i want ki i get only integer type value
empty_matrix = np.empty((3, 4), dtype=int)
print(empty_matrix)
