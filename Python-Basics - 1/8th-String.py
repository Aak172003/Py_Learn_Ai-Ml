# String -> Strings are sequence of Characters
# In Python specifically, strings are a sequence of Unicode Characters

# ******************************  Creating Strings  ***********************************

# s = 'hello'
# s = "hello"

# multiline strings
s = '''hello
my name is '''

# s = """hello
# My name is
# """

# s = str('hello')
print(s)

# ******************************  Accessing Strings  ***********************************

'''
Note -> if we traverse from left to right then string start from 0th index 
But if i consider for right to left start from -1 
 0  1  2  3  4  5
 A  a  k  a  s  h 
-6 -5 -4 -3 -2 -1
'''

# Positive Indexing
s = 'hello world'
print(s[4])

# Negative Indexing
s = 'hello world'
print(s[-3])

# ******************************  String Slicing  ***********************************

# syntax -> s[start , end-1 , gap ]
# end-1 , because string start with 0th index
# By Default gap = 1

s = 'hello world'
print(s[0:5])  # 4 -> like 5-1 = 4

# Slicing
s = 'hello world'
print(s[5:0:-1])  # 4 -> like 5-1 = 4

# ******************************  Editing and Deleting in Strings  ***********************************

# Python strings are immutable ,
# so we can not add and delete any portion in string
# But we can delete full string using del keyword , after this we can't use delete string


# ******************************  Operations on Strings  ***********************************

# Arithmetic Operations

print('delhi' + ' ' + 'mumbai')
print('delhi ' * 5)

# Relational Operations

print('mumbai' > 'pune')

# Note
'''
lexicographically
those words come first which is small , and those comes after which is greater
capital value has small ASCII Value , small value has high ASCII Value
'''

print('Pune' > 'pune')

# Logical Operations

# in python , if string have any char , which means true , if empty means false
# jb tk usko true milta hai tb tk jaata hai , or wo jaha true mila wo print

print('hello' and 'world' and 'aman')

# if first true , aage nhi jaega
print('hello' or 'world')

# first empty , so aag nhi jaega false ko hi print kr dega jiski wjh se false aaya
print('' and 'world')

# if first false  , aage bhi jaega , jb true milega , tb ruk jaega
print('' or 'world')

print(not 'hello')

# Loops on Strings

for i in 'delhi':
    print('pune')

for i in 'hello':
    print(i)

# ******************************  String Common Functions  ***********************************

# len , max , min , sorted , Capitalize , Title , Upper / Lower , Swapcase , count , find , index , endswith , startwith , split , join , replace , strip , centralise a string

print(len('hello world'))
print(max('hello world'))  # print max character
print(min('hello world'))  # print min character  space is highly less character
print(sorted('hello world', reverse=True))

# Format Literals
'''
Note : 

name = 'nitish'  # 0
gender = 'male'  # 1
age = 25         # 2

'Hi my name is {1} and I am a {0} and my age is {2}'.format(gender,name , age)

'''
