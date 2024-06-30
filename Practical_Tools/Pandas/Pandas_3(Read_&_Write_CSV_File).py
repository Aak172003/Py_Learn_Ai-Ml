import pandas as pd
import os as operating_system

# This give proper definition of read_csv function
# help(pd.read_csv)

# Read the 1d or 2d data
df = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv')
print(df)

# find where this file store when I open that file using read_csv function
print('find where this file store : ', operating_system.getcwd())

# By default, head and tail give only 5 rows,
# but we can modify no of rows head(n) , tail(n)

# Read only 5 data from top and bottom
print(df.head(10))
print(df.tail(10))

# How check data types
print(type(df))

