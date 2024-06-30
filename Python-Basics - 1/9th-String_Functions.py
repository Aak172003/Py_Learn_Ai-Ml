a = "hell21521"
b = "Hello"
c = "123456"
d = "HELLO"
e = " "
f = "Hello 123@"
g = "1.234"

# isalnum -> check if string present alphabet and numeric combination true , otherwise false
print(a.isalnum())

# isalpha -> check if string present only alphabet true , otherwise false
print(b.isalpha())

# isdigit -> check if string present only numeric true , otherwise false
print(c.isdigit())

# isIdentifier -> check if string is valid identifier so true , otherwise false
print(d.isidentifier())

# isdecimal -> return true if all character in string is decimal or not
print(e.isdecimal())

# isnumeric -> return true if all character in string is numeric or not
print(f.isnumeric())

# islower -> return true if all character in string is in lowercase or not

# isupper -> return true if all character in string is in uppercase or not

# Ends with
print('my name is nitish'.endswith('nitish'))

# Start with
print('my name is nitish'.startswith('my'))

# Swapcase -> convert capital to lower , lower to capital
print('HeLlO WorLD'.swapcase())

# Count
print('my name is nitish'.count('i'))

# Find -> jo nhi milta , return -1
print('my name is nitish'.find('x'))

# Index -> jo nhi milta , return error
print('my name is nitish'.index('a'))

'''
rindex -> searches the string for a specified value and returns the last position of where it was found

lindex -> searches the string for a specified value and returns the first position of where it was found

'''

# ljust -> Return left justified version of the string

a = "Aakash Prajapati"

# a pr kaam krega
x = a.ljust(50, '#')

print(a)
print(x, "is my name ")

# rjust -> Return right justified version of the string

a = "Aakash Prajapati"
# a pr kaam krega

x = a.rjust(50, '*')

print(a)
print(x, "is my name ")

s = "Aakash Prajapati"

# Capitalize -> capital only first letter
print(s.capitalize())
print(s)

# Title -> every first letter even after space
print(s.title())

# Upper
print(s.upper())

# Lower
print('Hello Wolrd'.lower())

# Split

# from above so it will not directly change into original ,
# actually it create a new memory loaction ,
# and that modified stored in this

s = 'hi my name is nitish'
print(s.split())

print(s)

# Join
" ".join(['hi', 'my', 'name', 'is', 'nitish'])

# Replace -> from above, so it will not directly change into original ,
# actually it create a new memory location , and that modified stored in this

s = 'hi my name is nitish'
print(s.replace('nitish', 'campusx'))

# Replace function ,does not replace in original string
print(s)

# Strip -> remove trial spaces from left side and right side , but not remove space form middle
'nitish                           '.strip()

# Centrailise
s = "Aakash"
print(s.center(20))
