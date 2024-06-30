import numpy as np

ch_name = "Indian Ai Production "
str1 = "Learning Python Numpy"

# This is used to add two string
temp_str = np.char.add(ch_name, str1)
print(temp_str)

# All this below method will not directly change into original ,
# actually it create a new memory location ,
# and that modified stored in this

print(np.char.lower(ch_name))
print(np.char.islower(str1))
print(np.char.upper(ch_name))
print(np.char.isupper(str1))

print(np.char.center(str1, 60,"-"))

print(np.char.split(ch_name))  # with every array element

# This is used to split from where the next line start
print(np.char.splitlines("hello\nIndian"))

str4 = "dummy video start"
str5 = "dummy video start "

# Separate all alphabets with some sign
print(np.char.join([":", "/"], [str4, str5]))


print(np.char.join(":",  str5))


# Replace -> from above, so it will not directly change into original ,
# actually it creates a new memory location, and that modified stored in this

s = 'hi my name is nitish'
print(s.replace('nitish', 'campusx'))

# Replace function, does not replace in original string
print(s)

# ---------------------------- equal ------------------------------

print(np.char.equal(str4, str5))

# ---------------------------- String Information ------------------------------

# Count ? any char how many times presently
# Find ? Find -> jo nhi milta , return -1

# # Index -> jo nhi milta , return error
# Index ?


















