
# Fibonacci Series

# a = 0
# b = 1
# n = int(input("Enter a number : "))
#
# if n == 1:
#     print(1)
# else:
#     print(a)
#     print(b)
#     for i in range(2, n+1):
#         c = a + b
#         a = b
#         b = c
#         print(c)

# Check if a number is prime or not

n = int(input("Enter number to check whether it is a prime or not "))

if n <= 1:
    print("it is not prime no.")
else:
    for i in range(2, n):
        if n % i == 0:
            print("No is Not prime")
            break
    else:
        print("Number is prime ")








