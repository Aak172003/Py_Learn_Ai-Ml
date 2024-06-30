# ****************************** Dict ***********************************

# Dictionaries allow user to write the data in the form of Keys and values
# Dictionaries are enclosed inside curly brackets {}.
# Keys and values are separated by colon
# Every key value pair is separated by comma( , )


emp_data = {"name": "john", "age": 24, "gender": "male"}

# print(emp_data)
# print(emp_data["age"])

# Add new key and value data into the existing dictionary
emp_data["phone_id"] = "+91-9310483028"

# print(emp_data)
# print(emp_data["phone_id"])

# Iteration in dictionary

stud_data = {"name": "john", "age": 24, "gender": "male", "roll_no": 5}

# *****************************************************************
# Print all key names one by one

for i in stud_data:
    print(i, end=" ")

print('\n')

# *****************************************************************
# Find Keys , using Keys function
for keys in stud_data.keys():
    print(keys)

# *****************************************************************
# Print all key->values one by one

for i in stud_data:
    print(i, " -> ", stud_data[i])

# *****************************************************************
# Find values , using value function
for value in stud_data.values():
    print(value)

# *****************************************************************
# print both key and value at a time using items function
for x, y in stud_data.items():
    print(x, ":", y)
