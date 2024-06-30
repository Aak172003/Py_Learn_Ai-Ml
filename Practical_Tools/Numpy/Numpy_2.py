# Numpy Functions
import numpy as np

# arange() -> behave like python range function

# np.arrange(start,end,gap)
arr_1d = np.arange(1, 16, 2)
print(arr_1d)

# --------------------------- linspace() ---------------------------------

# This give random value which in between start and stop
# and num means I want 4 values which could be in my start and stop range

print(np.linspace(1, 5, 4))

# --------------------------- reshape() ---------------------------------

# This is used to change the dimension of 1d array to 2d array
reshaped_arr_1d = arr_1d.reshape(4, 2)
print(reshaped_arr_1d)

# Apply two methods (like chaining rule)
arr = np.arange(1, 13).reshape(2, 6)
print(arr)

# --------------------------- ravel() ---------------------------------
# This function convert multi-dimensional into 1d array

after_ravel = arr.ravel()
print(after_ravel)

# --------------------------- flatten() ---------------------------------

# This function convert multidimensional into 1d array,
# but element arrange in 1d on some order basis

# order{‘C’, ‘F’, ‘A’, ‘K’}, optional

# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html

# --------------------------- transpose() ---------------------------------
# This convert the matrix dimension from row to column and column to row

transpose_arr_1d = reshaped_arr_1d.transpose()
print(transpose_arr_1d)

# or
# Another way
print(transpose_arr_1d.T)
