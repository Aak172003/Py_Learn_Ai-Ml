
# Nested Dictionaries

employee = {
    1: {"name": "Akash", "age": 24},
    2: {"name": "Lisa", "gender": "Female"},
    3: {"name": {"nested": "value"}, "gender": "Female"}
}

print(employee)

# --------------------------------------------------------

print(employee[1])
print(employee[1]["name"])
print(employee[1]["age"])
print(employee[2]["name"])
print(employee[2]["gender"])
print((employee[3]["name"]["nested"]))
