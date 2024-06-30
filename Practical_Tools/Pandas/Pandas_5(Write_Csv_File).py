import pandas as pd

df_1 = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv')
print(df_1)

# ---------------------- Header ------------------------------------
# This is used to make header of any row

# df_2 = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv', header=6)
# print(df_2)

# if we don't have any header, so we use header = none

# ---------------------- Prefix ------------------------------------
# This is used if I don't have a header,
# so we can use prefix with header none, so this gives valid column name ( column0, column1 , ........ column n)

# df_2 = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv', header=None,
# prefix='Akash ') print(df_2)

# ---------------------- names ------------------------------------

# # This is ued to give custom name of any column in csv file
# df_2 = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv',
#                    names=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])
#
# print(df_2)

# ---------------------- Prefix ------------------------------------

print(df_1.head(10))
print(df_1.tail(10))

# ---------------------- dType ------------------------------------
# This is used to convert datatype of any particular column

df_2 = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv',
                   dtype={'Index': 'float64'})
print(df_2)

df_3 = pd.read_csv('D:\\Python_Things\\Py_Learn\\Practical_Tools\\Csv_Files\\customers-1000.csv', true_values=['Yes'],
                   false_values=['No'])
print(df_3)
