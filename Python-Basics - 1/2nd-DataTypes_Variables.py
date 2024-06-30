# 1e308 or 1e+308 => 1 * 10 ^ 308
print(1e308)

# 1.7e308 or 1.7e+308 => 1.7 * 10 ^ 308
print(1.7e308)

# ******************************  Data Types  ***********************************

'''
Data Types : 

Text-type : String(str)
Numeric-type : int , float , complex
Sequence-type : list , tuple , range
Mapping-type : dict
Set-type : set , frozenset
Boolean-type : true , false
Binary-type : bytes , bytearray , memoryview
'''

# List in C language => we called as Array
list = [1, 2, 3, 4, 5]
print("This is List -> ", list)

# Tuple
tuple = (1, 2, 3, 4, 5)
print("this is tuple data -> ", tuple)

# Set
set = {1, 2, 3, 4, 5, 6, 1, 2, 3}
print("this is set data -> ", set)

# Dictionary
my_dict = {'name': 'Aman', 'age': 70}
print(my_dict['name'])

# ******************************  Variables ***********************************

name = "Aakash"
print('My name is : ', name)

# Eval Function -> return a final result after evaluating expression
exp1 = eval(input("Enter your Expression : "))
print(exp1)

'''
expression = 'x*(x+1)*(x+2)'
print(expression)

# (Whatever variable we used while creating expression -> we need to assign value for each variable , other wise hiow this will evalute expression)

x = 3
result = eval(expression)
print(result)
'''

print("type of exp1 : ", type(exp1))

# Assignment Operator
a, b, c = 1, 2, 3
print(a, b, c)

# All Assign with the same value
a = b = c = 1
print(a, b, c)

# Play with some dictionary
data = {'name': "Aakash", 'age': 50}

# This popitem extracts the key and its value from last
key, value = data.popitem()
print("key : ", key, " value : ", value)

# This way also works for assign via using a list, this also works same for tuple
x, y, z = [10, 20, 30]
print(x, y, z)

# * keyword -> this will store all value in array form inside it
x, y, *rest = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(x, y, rest)

# with string
x, y, z = 'abc'
print(x, y, z)
