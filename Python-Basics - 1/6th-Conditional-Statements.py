# Types of Conditional Statements

# ******************************  1 If the statement ***********************************

a = 10
if a == 10:
    print("No is equal to 10 ")

# ******************************  2 if-else Statement ***********************************

a = 20
if a == 10:
    print("No is equal to 10 ")
else:
    print("No is not 10 , something else")

# ******************************  3 if-elif-else Statement ***********************************

marks = 60

# Simply Chained Comparisons
if 90 < marks <= 100:
    print("You can go goa")
elif 50 < marks < 80:
    print("You can go manali ")
else:
    print("No means no ")

# Or

# if marks > 90 and marks <= 100:
#     print("You can go goa")
# elif marks > 50 and marks < 80:
#     print("You can go manali ")
# else:
#     print("No means no ")

# ******************************  4 Nested Statement ***********************************

# login program and indentation
# email -> nitish.campusx@gmail.com
# password -> 1234

email = input("Enter your email: ")
password = input("Enter your password: ")

if email == "123@gmail.com":
    if password == "123":
        print("Welcome")
    else:
        print("Password is wrong")
else:
    print("Email is wrong")

# ******************************  5 Short hand if Statement ***********************************

a = 6
if a > 5: print("a is greater than 5")

# ******************************  5 Short hand if-else Statement ***********************************

a = 10
print("a is greater") if (a > 5) else print("a is not equal to 5 ")
