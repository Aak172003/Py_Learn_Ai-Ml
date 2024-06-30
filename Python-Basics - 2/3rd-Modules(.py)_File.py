# Modules are the (.py) files,
# that contains set of functions you want to include in your program

# In-Built Modules

# ******************************  DateTime ***********************************

import datetime
import random
import math

todayDate = datetime.datetime.now()
print("todayDate : ", todayDate)

# Get Today Day
days_of_week = todayDate.weekday()
print(days_of_week)

# Define a list of days, Starting form 0th index
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

today = days[days_of_week]
print(today)

# -------------------------------------------------------------------

y = datetime.datetime(2004, 10, 22)

print(y.strftime("%A"))  # full
print(y.strftime("%a"))  # short
print(y.strftime("%B"))  # full
print(y.strftime("%b"))  # short

# ******************************  Random ***********************************

x = random.randint(1, 10)
print(x)

# If I want Random strings between predefined Strings
predefined = ['Heads', 'Tails']

getValue = random.choice(predefined)
print(getValue)

# ******************************  Math ***********************************

a = pow(5, 6)
print("pow(5, 6) : ", a)

maxi = max(3, 4, 5, 6, 9, 4, 1)
print("Max value is : ", maxi)

mini = min(3, 4, 5, 6, 9, 4, 1)
print("Min value is : ", mini)

squareRoot = math.sqrt(4)
print("squareRoot : ", squareRoot)

# -------------------------------------------------------------------

# Absolute
positive = abs(-22)
print("positive : ", positive)

# Ceil
ceil = math.ceil(2.2)
print("ceil Value : ", ceil)

# Floor
floor = math.floor(2.2)
print("floor Value : ", floor)
