# 1st WAP to check no is positive or not

# num = int(input("Enter your fav number : "))
# if (num > 0):
#     print("No is positive ")
# else:
#     print("No is negative")

# 2nd WAP to create area calculator

# choices = int(input("Enter your choice "))
#
# if choices == 1:
#
#     print("Area of circle ")
#     rad = float(input("Enter radius "))
#     area = 3.14 * rad ** 2
#     print("area of circle ", area)
# elif choices == 2:
#
#     print("Area of rectangle ")
#     length = float(input("Enter length "))
#     breadth = float(input("Enter breadth "))
#     area = length * breadth
#     print("area of rectangle ", area)
# elif choices == 3:
#
#     print("Area of square ")
#     side = int(input("Enter side "))
#     area = side ** 2
#     print("area of square ", area)
# else:
#     print("Area of triangle ")
#     base = float(input("Enter base "))
#     height = float(input("Enter height "))
#     area = 0.5 * base * height
#     print("area of triangle ", area)

# 3rd WAP to check letter is vowel or not

letter = input("Enter your letter : ")
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
    print("This letter is vowel ")
else:
    print("This is not vowel ")

#          OR

# if (letter in "aeiou") or (letter in "AEIOU"):
#     print("This letter is vowel ")
# else:
#     print("This is not vowel ")
