Student = {"name": "Akash", "roll_no": 50, "College": "Raj Kumar Goal Inst. of Tech"}

# ******************************  1 SetDefault in Dictionary ***********************************

# setDefault : The setdefault() method returns the value of a specified key from the dictionary.
# print(Student.setdefault('roll_no'))

# If the key does not
# exist, it inserts the key with a specified value (defaulting to None) into the dictionary.

x = Student.setdefault("gender", "Male")
# print(x)
print(Student)

# ******************************  2 Update in Dictionary ***********************************

# update: Update Keywords update the value corresponding to that key ,
# But if that key not exists which I need to update,
# so this will add the new key and value corresponding to it

Student.update({"age": 20, "grade": "A"})  # Adding new key-value pairs
print(Student)

# ******************************  3 pop in Dictionary ***********************************

# pop
age = Student.pop("age")
print(age)  # output 20
print(Student)

# ******************************  4 popitem in Dictionary ***********************************

# popitem: Pop Item (key-value) from last
item = Student.popitem()  # Removing and returning an arbitrary (key, value) pair
print(item)  # Output: ('grade', 'A')
print(Student)

# ******************************  5 clear in Dictionary ***********************************

# clear: Clear the student Dictionary
Student.clear()
print(Student)
