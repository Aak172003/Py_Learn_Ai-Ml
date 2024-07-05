import pandas as pd
import numpy as np

df_1 = pd.read_csv('D:\\Python_Things\\Py_Learn-main\\Practical_Tools\\Csv_Files\\customers-1000.csv')
print(df_1)

# ------------------------  Na_Values  --------------------------------

# df_2 = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv',
#                    na_values=["not available", 'no values'])
# print(df_2)

# print(df_2.head(10))

# We use dictionary for any specific column in a database

# df_2 = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv',
#                    na_values={'Website': 'no values', 'First Name': "not available"})
#
# print(df_2.head(10))

# ------------------------  Keep Default Na   --------------------------------

# Keep Default na -> if I want ki pandas library does not consider any nan of missing value, keep as default
# keep_default_na = true, so this default property will go to execute

# df_3 = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv', keep_default_na=False)
#
# print(df_3.head(10))


# ------------------------  Na_filter  --------------------------------

# Na_filter -> this is used for parsing over the datasets. This find missing values, so we can handle that missing values,
# from this my model performance automatically boast

# If I put na_filter as true, so this put NaN at place of missing value,
# but if I make as False, so this will show as it is whatever I put in datasets.

# df_4 = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv', na_filter=False)
#
# print(df_4.head(10))

# ------------------------  isnull()  --------------------------------

# df_5 = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv')

# print(df_5.head(10))

# This return all null values via true or false -> true means null , false means not null
# print(df_5.isnull())

# This return no of null vales in column wise
# print(df_5.isnull().sum())

# Give an idea about no of total null values in datasets
# print(df_5.isnull().sum().sum())

# ------------------------  notnull()  --------------------------------

# This is just opposite to null values
# here true means not null, and false means null
# print(df_5.notnull())

# This return no of not vales in column wise
# print(df_5.notnull().sum())

# Give an idea about no of total notnull values in datasets
# print(df_5.notnull().sum().sum())

# ------------------------  with series
# pandas handling method--------------------------------

# sr = pd.Series([1, 2, 3, np.nan, 4, np.NAN])
# print(sr)

# ------------------------  dropna()  --------------------------------

# First traverse on dataset and found any null value, so this removes that particular row and column and creates not null datasets for better processing

df_6 = pd.read_csv('D:\\Python_Things\\Py_Learn-main\\Practical_Tools\\Csv_Files\\customers-1000.csv')

print(df_6.head(10))
# Remove that particular row and column from datasets who have null value
print(df_6.dropna())
# by default, axis 0 (means row)


print(df_6.dropna(axis=1))  # delete column who has null value

# by default, follow any parameter

# any -> remove that row and column if dataset has any single null value
# all -> remove that row and column if only is all row or column has missing null value
print(df_6.dropna(how='all'))

# thresh parameter -> print those columns or row which has n no of not-null values otherwise drop that row

print(df_6.dropna(thresh=1))  # at least 1 not-null value

# inplecae -> if I true that inplace value, so this will update that dataframe, not create new dataframe
print(df_6.dropna(axis=1, inplace=True))

# update in own Excel own csv file
print(df_6)
