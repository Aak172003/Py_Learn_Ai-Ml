# It is used when anonymous function is required for a short period of time,
# It can Take numerous argument
# It can only have one expression

# a variable has lambda b anonymous function
x1 = lambda b: b * 5

print(x1(5))
print(x1(4))

x2 = lambda a, b, c, d: (a + b + (c * d) + a * b)

print(x2(2, 2, 2, 2))
