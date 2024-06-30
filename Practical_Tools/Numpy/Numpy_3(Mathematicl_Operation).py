import numpy as np

arr_1 = np.arange(1, 10).reshape(3, 3)
arr_2 = np.arange(1, 10).reshape(3, 3)
print(arr_1)
print(arr_2)

# --------------------------- Add() ---------------------------------

add = arr_2 + arr_1
print('Addition \n', add)

# Addition Via Inbuilt Function
print(np.add(arr_2, arr_1))

# --------------------------- Substract() ---------------------------------

sub = arr_1 - arr_2
print('Subtraction \n', sub)

# Subtract Via Inbuilt Function
print(np.subtract(arr_2, arr_1))

# --------------------------- Multiply() ---------------------------------

mul = arr_1 * arr_2
print('Multiplication \n', mul)

# Multiply Via Inbuilt Function
print(np.multiply(arr_2, arr_1))

# --------------------------- Divide() ---------------------------------

divide = arr_1 / arr_2
print('Divide \n', divide)

# Divide Via Inbuilt Function
print(np.divide(arr_2, arr_1))

# --------------------------- Dot or Standard Product() ---------------------------------

# first row with 1st column, then first row with second column

# a(2,3) @ b(3,4) => c(2,4)

arr_3 = np.arange(1, 13, 2).reshape(2, 3)
arr_4 = np.arange(1, 13).reshape(3, 4)

print(arr_3)
print(arr_4)

# c_matrix = arr_3 @ arr_4

# or

c_matrix = arr_3.dot(arr_4)
print(c_matrix)

# --------------------------------- Maximum --------------------

max_Arr_1 = arr_1.max()
print(max_Arr_1)

# Find Index of maximum value
max_value_index = arr_1.argmax()
print(max_value_index)

# Find min value in every row or column
# where single 0 -> column, 1 -> row
get_max = arr_1.max(axis=1)
print(get_max)

# --------------------------------- Minimum --------------------

# Find min value
# Find index of min value
# Find min value in every row or column
# where single 0 -> column, 1 -> row

# --------------------------------- Functions --------------------

# Add all value in matrix and get single value

print(np.sum(arr_1))

# get a sum of all rows wise
print('Row wise ', np.sum(arr_1, axis=1))
# get a sum of all columns wise
print('Column wise ', np.sum(arr_1, axis=0))

# Fet Average of Matrix
print('Average', np.mean(arr_1))

# Square rooot of every element
print('Square root ', np.sqrt(arr_1))

# Get exponent of every element
print(np.exp(arr_1))

# get log of every element
print('log \n ', np.log(arr_1))
print('log2 \n ', np.log2(arr_1))
print('log10 \n ', np.log10(arr_1))
