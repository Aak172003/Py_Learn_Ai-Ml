# ******************************  Operators in Python   ***********************************

# Arithmetic Operators
print(5 + 6)
print(5 - 6)
print(5 * 6)
print(5 / 2)

print(5 // 2)  # Integer Division
print(5 % 2)  # Modulus
print(5 ** 2)  # Power

# Comparison Operator
print(5 < 6)
print(5 <= 5)
print(5 != 5)
print(5 == 5)
print(5 >= 6)
print(5 > 6)

# Logical Operators
print(1 and 0)
print(1 or 0)
print(not 1)

# Assignment Operator -> ( = , += , -= , *= )
a = 5
print(a)

a = a + 6
print(a)

a = a - 6
print(a)

a = a * 6
print(a)

# Identity Operator:
# is / is not This Operator is used to compare items to see if they are the same object
# with the same memory address check data type, and its value is equal or not

a = 5
b = "5"
print("Identity Operator")
print(a is b)

# Membership Operators
# (In c, c++ and Java -> if we want this thing, so we have to traverse a loop for finding that result)
# in/not in

print('D' not in 'Delhi')
print(2 in [2, 3, 4, 5, 6])

# Bitwise Operators -> Work on binary representation

# bitwise and
print(2 & 3)

# bitwise or
print(2 | 3)

# bitwise xor
print(2 ^ 3)

print(~3)

print(4 >> 2)  # Right shift (2 times Divide by 2)

print(5 << 2)  # Left shift (2 times Multiply by 2)
