# ****************************** Tuple ***********************************

# Tuples are collection of ordered and un-mutable data
# For Tuple no brackets are mandatory . By Choice on can use parenthesis .
# The value inside a Tuple is separated by comma( , )

# Once created , Tuples can't be changed .
# Multiple datatype cam be written inside a tuple


# a = "apple", "mango", 1, "two ", 3, "four"
# # or
# b = ("apple", "mango", 1, "two ", 3, "four")
# print(a)
# print(type(a))
#
# print(b)
# print(type(b))

# b = "kiwi",   # ( "kiwi" , )
# print(b)
# print(type(b))

# ****************************** Slicing in Tuple  ***********************************

# a = ("apple", "mango", 1, "two ", 3, "four")
# print(a[0:3])  # 3 - 1 = 2
#
# print(a[0:6:1])  # iterate in forward direction
# print(a[::-1])  # iterate in backward direction
#
# print(a[2:: -1])

# ****************************** Iteration in Tuple  ***********************************

# a = ("apple", "mango", 1, "two ", 3, "four")

# With for loop
# for i in a:
#     print(i , end=" ")

# for loop along with range
# print()
# for i in range(len(a)):
#     print(a[i] , end=" ")

# along with while loop
# print()
# i = 0

# while i<len(a):
#     print(a[i] , end=" ")
#     i = i + 1

# ****************************** Function in Tuple  ***********************************

# Count Occurrences
a = ("four","apple", "mango", 1, "two ", 3, "four")

print(a.count("four"))

# Find index of any particular Element
print("Find index of any Particular element ")
print(a.index("apple"))
