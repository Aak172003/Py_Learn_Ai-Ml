# Pandas are maily used for data pre-processing and data cleaning
# Data Pre-Processing means cleaning of data and find some useful data with this row data

import pandas as pd

# So i can read 1d data and 2d data
df = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv')
print(df)

print((type(df)))

print(df.columns)

# Read data for specific rows and columns
print(" --------------- Read csv files for specific rows and columns ----------------------")

df = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv', nrows=5,
                 usecols=[0, 2, 3, 5])
print(df)

# ----------------------- Important Functions ----------------------------

# skip-rows


df = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv', skiprows=5)
# This will skip 5 rows
print("df : ", df)

df_new = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv', skiprows=[5,1,2])
# This will skip only row 5 (means specify row no)
print("df_new : ", df_new)


# --------------------------------------------------------------------------------------------------------------

# We can replace any other column with index
df = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv', index_col='Customer Id')
print(df)

