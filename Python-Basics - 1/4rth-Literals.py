# Literal -> values which stored in variable
name = "Aakash"

'''
nam is variable or identifier 
= is operator
"Aakash" is literal

'''

a = 0b1010  # Binary Literals
b = 100  # Decimal Literal
c = 0o310  # Octal Literal
d = 0x12c  # Hexadecimal Literal

# Float Literal
float_1 = 10.5
float_2 = 1.5e2  # 1.5 * 10^2
float_3 = 1.5e-3  # 1.5 * 10^-3

# Complex Literal
x = 3.14j

print("c", c)
print(a, b, c, d)
print(float_1, float_2, float_3)
print(x, x.imag, x.real)

# ******************************  String Literals ***********************************

string = 'This is Python'
strings = "This is Python"
char = "C"

multiline_str = """This is a multiline string with
 more than one line code."""

# Emoji
unicode = u"\U0001f600\U0001F606\U0001F923"

# as it is
raw_str = r"raw \t string"

# apply an escape sequence if we write
raw = "raw \t string"
print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)
print(raw)
