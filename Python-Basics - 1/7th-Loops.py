# Types of loops

# ******************************  1 For Loops ***********************************

# Syntax - for i in range(1 , n + 1, gap)

# For loop demo
for i in {1, 2, 3, 4, 5}:
    print(i)

# 1 , 1<11
for i in range(1, 11):
    print("Hello Babes ")
    i = i + 1  # i += 1

# 1 , 1<11 space 2 ka
for i in range(1, 11, 2):
    print(i)

# ******************************  2 while Loops ***********************************

number = int(input('enter the number'))
i = 1

while i <= 10:
    print(number, '*', i, '=', number * i)
    i += 1

# ******************************  3 while true Loops ***********************************

# while True:
#     print("Hii , How r u ?")

# ******************************  4 Nested Loop  ***********************************

# 1st example

# for i in range(1, 11):
#     print("i is -> ", i)
#
#     for j in range(1, 6):
#         print("value for ", i, " -> ", j)
#     print()

# 2nd example

# for i in range(1, 4):
#     for j in range(1, 11):
#         print(j)
#     print()

# ******************************  5 For Loop with Conditionals  ***********************************

# 1st Example

for i in range(1, 11):
    if i == 3:
        print("this is 3 ")
    else:
        print(i)

# 2nd Example

# Find common Multiple
for i in range(1, 101):
    if i % 8 == 0 and i % 12 == 0:
        print(i)

# 3rd Example
# while loop with else

x = 1
while x < 3:
    print(x)
    x += 1
else:
    print('limit crossed')
