import json

# dumps -> convert dict data into json format ( convert dict to string )
# loads -> convert json data into dict format ( convert string to dict )

# Dict
# student_data = {"name": "Akash", "age": 13, "marks": 87}
# print(type(student_data))  # dictionary data type
#
# #  Convert the following dictionary into JSON Format
#
# json_data = json.dumps(student_data)
#
# print("This is json_data : ", json_data)
#
# print(type(json_data))  # json ( string data type )

# *****************************************************************
#
# # Dict
# # student_data = {"name": "Akash","age": 13,"marks": 87}
#
# # String -> JSON Data
# student_data = '{"name": "Akash","age": 13,"marks": 87}'
#
# # This is How we access the data from the json data
# print(type(student_data))
#
# data = json.loads(student_data)
# print("This is Load data ", data)
# print(data["name"])

# *****************************************************************

# Pretty Print the following JSON Data

# student_data = {"name": "Akash", "age": 13, "marks": 87}
#
# data = json.dumps(student_data, indent=4, separators=(",", ":"))
# print(data)

# *****************************************************************

# write the below Dictionary data  into a Demo.json file

student_data = {"name": "Akash", "age": 13, "marks": 87, "school":"Rkgit"}

f = open("Demo.json", "w")
data = json.dumps(student_data, indent=4, sort_keys=True)
f.write(data)
print("The data has been added to the new file ")


# *****************************************************************

# Access the nested key "marks" from the following nested data

# This is Json Data
stud_data = """{ "Student" : {
    "grade" : {
        "name" : "David",
        "marks" : {
            "math" : 87
            }
    }
}}"""

# Here name and marks both are the same branch

print(stud_data)
print(type(stud_data))

data = json.loads(stud_data)
print(type(data))

print(data["Student"]["grade"]["name"])  # Accessing the "name" field
print(data["Student"]["grade"]["marks"]["math"])  # Accessing the "math" field


# *****************************************************************

# Access the nested key "marks" from the following nested data


newStud_data = """{"Student": {
    "grade": {"name": "David", "marks": 87}
}}"""

data = json.loads(newStud_data)

print(data["Student"]["grade"]["marks"])
print(data["Student"]["grade"]["name"])
