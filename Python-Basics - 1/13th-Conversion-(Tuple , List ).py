
# Conversion from tuple to list

a = ("apple", "mango", 1, "two ", 3, "four")
print(type(a), "before Conversion")
print(a)

a = list(a)
print(type(a), "After Conversion")
print(a)


print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")

# After Conversion, we can make any kind of changes in our list ,
# because List is mutable Data type

c = [20, 30, "forty", "fifty"]

for i in c:
    a.append(i)

print(type(a), "Befor Conversion")
print(a)

# Again Convert into tuple form list data type ( For making Im-mutable Data Type )

a = tuple(a)
print(type(a), "After Conversion")
print(a)


