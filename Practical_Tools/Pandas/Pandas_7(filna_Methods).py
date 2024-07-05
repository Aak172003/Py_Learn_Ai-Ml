import pandas as pd

# So i can read 1d data and 2d data
df = pd.read_csv('D:\\Python_Things\\Py_Learn-main\\Practical_Tools\\Csv_Files\\fillna_data.csv')
print(df)

print(df.fillna(5))

# This is how i set the specific value if null value found in associated with column name 
print(df.fillna({'First Name': "Aakash", 'City': 'Ghaziabad', 'Country': 'India'}))

