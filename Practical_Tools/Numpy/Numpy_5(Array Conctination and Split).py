import numpy as np

arr1 = np.arange(1, 17).reshape(4, 4)
arr2 = np.arange(17, 33).reshape((4, 4))

print(arr1)
print(arr2)

# ------------------------------- Concatenate -----------------------
# Concat two 2d matrix

# list1 = [2,4,6,8]
# list2 = [10,12,14,16]

# This method is not work in concatenation, if I write arr1+arr2
# this will add the matrix element by element

# print(list1+list2)  this will work in list case

# ----------------------------------------------------------------

# single 0 -> column, 1 -> row

# concatenation in row wise
# new_concat_arr_row = np.concatenate((arr1, arr2), axis=1)

# Or we can use hstack function
new_concat_arr_row = np.hstack((arr1, arr2))
print('Row wise \n ', new_concat_arr_row)

# concatenation in column wise
# new_concat_arr_col = np.concatenate((arr1, arr2), axis=0)

# Or we can use vstack function
new_concat_arr_col = np.vstack((arr1, arr2))
print('Column wise \n ', new_concat_arr_col)

# ------------------------------- split with 2d array -----------------------

# This is list of list (2d array)
split_new_concat_arr_row = np.split(new_concat_arr_row, 2)
print(split_new_concat_arr_row)

# This is list of list  -> perform all operation which i have perform with list data type
print(type(split_new_concat_arr_row))

# Access first index value
print(split_new_concat_arr_row[1])

# --------------------------------------------------------------------------------
# This is list of list

split_new_concat_arr_col = np.split(new_concat_arr_col, 2)
print(split_new_concat_arr_col)

# This is list of list -> perform all operations that I have performed with a list data type
print(type(split_new_concat_arr_col))

# ----------------------------------------------------------------

arr_1d = np.arange(1, 6)
print("Original Array:", arr_1d)

# Split the array into sub_arrays at indices 1 and 3

result = np.split(arr_1d, [1, 3])
print("Result of split:", result)
