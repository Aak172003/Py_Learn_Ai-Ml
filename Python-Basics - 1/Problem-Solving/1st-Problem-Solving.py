
# 1st WAP to display a person name , age and address in three different Lines
name = input("Enter your name : ")
age = int(input("Enter your age "))
address = input("Enter yor address")

print(name , age , address , sep="\n")

# 2nd WAP to swap two variable .
x = 12
y = 13

# 1st Method
z = x
x = y
y = z

# 2nd Method
x = x + y
y = x - y
x = x - y

# 3rd Method
x,y = y,x

print("x is : " , x)
print("y is : " , y)

