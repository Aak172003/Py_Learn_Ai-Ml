import numpy as np

arr_1 = np.arange(1, 101).reshape((10, 10))

# arr_1 = np.arange(1, 101, dtype=float).reshape((10, 10))
print(arr_1)

# get 0,0 th value
print(arr_1[0, 0])

print('Dimension ', arr_1.ndim)
print('Size ', arr_1.size)

# get particular row
print(arr_1[0])

# get particular column
print((arr_1[:, 1]))

# if I want this column 1d array into 2d array
print('1d array into 2d array : ')

# print(array[start index: end index (exclusive) ])
print(arr_1[0:5, 0:5])
print((arr_1[:, 0:5]).ndim)

# get element 5 element from single row and multiple column
print(arr_1[1, 0:5])

# get element 5 element form every column
print(arr_1[0:5, :])

# get a slice of matrix
print(arr_1[1:4, 0:5])
print((arr_1[1:4, 0:5]).shape)

print(arr_1[:, 1:6])

# This show byte required storing every single byte
print(arr_1.itemsize)
print(arr_1.dtype)
