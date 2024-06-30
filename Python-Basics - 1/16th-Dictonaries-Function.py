stud_data = {"name": "john", "age": 24, "gender": "male", "roll_no": 5}

# Get
x = stud_data.get("gender")
print(x)

# Item
x = stud_data.items()
print(x)

# All keys
keys = stud_data.keys()
print(keys)

# All values
values = stud_data.values()
print(values)

# Copy the stud_data into new_data in the form of dictionaries
new_data = stud_data.copy()
print(new_data)

