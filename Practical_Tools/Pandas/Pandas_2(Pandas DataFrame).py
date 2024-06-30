# Pandas DataFrame -> Pandas DataFrame is two-dimensional, size-mutable, potentially heterogeneous tabular data
# structure with labeled axes (rows and column)


# How Create Python Pandas DataFrame
import pandas as pd

# --------------------- empty dataFrame ----------------
empty_df = pd.DataFrame()
print("empty_df : ", empty_df)  # with empty column and empty index

# --------------------- create dataFrame with list ----------------
# Make sure all lists have same no of an element

list_01 = [1, 2, 3, 4, 5, 6, 7]
print(list_01)
df1_list = pd.DataFrame(list_01)
print(df1_list)

# --------------------- create dataFrame with list of list ( multiple column )  ----------------

ls_of_ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7, 8]]
df2_ls_of_ls = pd.DataFrame(ls_of_ls)

print(df2_ls_of_ls)

# --------------------- create dataFrame with dictionary of list  ----------------

# Here key becomes label
dict1 = {'id': [11, 22, 33, 44, 55, 66]}

df_01_dict = pd.DataFrame(dict1)
print(df_01_dict)

# --------------------- create dataFrame with dictionary of dictionary list  ----------------

dict2 = {'id1': [1, 2, 3, 4, 5, 6], 'id2': [1, 7, 8, 9, 6, 5], 'id3': [8, 9, 6, 5, 4, 7]}
df_01_dict_of_dict = pd.DataFrame(dict2)
print(df_01_dict_of_dict)

# --------------------- create dataFrame with a list of dictionary  ----------------

ls_dict = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6, 'c': 7}]
df_ls_of_dict = pd.DataFrame(ls_dict)

print(df_ls_of_dict)

# --------------------- create dataFrame with a list of dictionary{Series} ----------------

dict_sr = {'Id': pd.Series([1, 2, 3, 4]), 'Sn': pd.Series([5, 6, 7, 8])}

data_frame = pd.DataFrame(dict_sr)
print(data_frame)
