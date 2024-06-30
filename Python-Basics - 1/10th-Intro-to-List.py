# ******************************  List ***********************************

# List are written inside square Bracket
# The values inside a list is separated by comma (,)
# List is mutable , means once created , they can be changes
# Multiple data types can be stored into list ( changes on original list , not it's copy )

a = ["mango", "banana", 1, 40, 1.40]
print(a)
print(type(a))

# ******************************  List Slicing ***********************************

print(a[4])
print(a[2])

print(a[-1])

print(a[0: 4])  # 4-1 = 3  means from 0 to 3
print(a[:5])
print(a[-5:-1:])

# Reverse
print(a[:: -1])

# ****************************** List In Iteration via Loop ***********************************

# Iteration Using For loop
b = ["mango", "banana", 1, 40, 1.40]

for i in b:
    print(i, end=" ")

# Iteration using for loop with range and length function

# getLen = len(b)
#
# for i in range(0, getLen):
#     print(b[i], end=" ")

# Iteration using while loop

# i = 0
# while i <= len(b) - 1:
#     print(b[i], end=" ")
#     i = i + 1

# Using Short-Hand loop

# [print(i, end=" ") for i in b]

# ****************************** List Functions Part 1 ***********************************

# a = ["thor", "c-america", "spidy", "widow", "spidy"]

# Find length
# print(len(a))

# Count an occurrence of particular element
# print(a.count("spidy"))

# Add something to list
# a.append("Aman")
# print(a)

# Add to specific location

# a.insert(2 , "Khan")
# a.insert(1 , "Pajama ")
# print(a)

# Remove from list

# a.remove("khan")
# print(a)

# Remove from a specific location

# print(a.pop(2))
# print(a.pop(1))
# print(a)

# ****************************** List Functions Part 2 ***********************************

# a = ["thor", "c-america", "spidy", "widow", "spidy"]

# Create a Copy of list
# b = []
# print(b)
# b = a.copy()
# print(b)

# Index -> To access an Element index ( on first occurrence )
# print(a.index("spidy"))

# Extend a list by add new list

# c = ["1", "two", "3", "four"]

# this put c in form of list , which means list inside list
# a.append(c)
# print(a)

# This adds all in single list
# a.extend(c)
# print(a)

# Reverse the list

# a.reverse()
# print(a)

# Sort the list -> in lexicographically

# a.sort()
# print(a)

# to Clear all the data from the list
# a.clear()
# print(a)
