# Pandas is a powerful python data analysis toolkit
# Open Source
# A fast and efficient Data Frame Object for data manipulation
# Reading and writing data structure and different format: csv, tsv, txt, xml, json, zip, etc.

# Pandas Data Structure are classified into 3 parts
# Series
# Data Frame
# Panel

# Numpy array is used fot implementation of panda data objects

import pandas as pd

print(pd)
# Used to check a version of panda library
print(pd.__version__)

# ------------------------------- Series ----------------------

# Pandas work on only a list, tuple
list_s = [1, 2, 3, 4, 9, 7, 'data values']
print(list_s)

series1 = pd.Series(list_s)
print(series1)

# print(series1[0])
# print(series1[1])
# print(series1[5])

series2 = pd.Series([1, 2, 3, 4, 'Second_Series'])
print("series2 : ", series2)

# How create Empty List
empty_series = pd.Series([])
print("empty_series : ", empty_series)

# -------------------------------------------------------------------------

# We can define a type of index as well
series3 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'y', 'z'], dtype=float, name='Data values')
print(series3)
print(series3['y'])
print("series3.name : ", series3.name)

# ------------------------------ Create list with single values -----------------------------
scalar_s = pd.Series(5, index=[1, 2, 3, 4, 5])
print(scalar_s)

# ------------------------------ Create list with Dictionary values -----------------------------

dict_s = pd.Series({'a': 1, 'b': 2}, name='Dictionary Values')
print(dict_s)

# ------------------------------------------------------------------------------------------------

print("-------------------")
# Panda series is support python numpy array
s4 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("String slicing ")
print(s4[0:9:2])

# get min and max value
print(max(s4))
print(min(s4))

# S4 has only those values that are greater than 3
# This make in series form
print(s4[s4 > 3])

# Pandas are automatically handle missing value,
# those are missing this will out NULL that place
s5 = pd.Series([1, 2, 3, 4, 5])
print((s4 + s5))
