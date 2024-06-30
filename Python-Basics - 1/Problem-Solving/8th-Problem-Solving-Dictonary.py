# Write a python program to sort the dictionary by value

a = {"e": 45, "a": 12, "c": 6, "b": 23, "d": 91}
a = sorted(a.keys())
print(a)

# Write a program to sort a dictionary by key

a = {"e": 45, "a": 12, "c": 6, "b": 23, "d": 91}

# This sorted function doesn't sort the original dict, it creates a new list where store the sorted key or values data
a = sorted(a.values())
print(a)

# Write a python script to print a dictionary where keys are numbers b/w 1 and 15 and values are square of keys

a = {}
for i in range(1, 16):
    a[i] = i ** 2

print(a)

# Write a program to multiply all the items in a dictionary

product = 1

a = {"e": 45, "a": 12, "c": 6, "b": 23, "d": 91}

for i in a.values():
    product = product * i

# or

# for i in a:
#     product *= a[i]

print(product)
