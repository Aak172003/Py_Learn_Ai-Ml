A = ["Rose", "Rachel", "Monica", "Joe "]

# WAP to swap first and fourth element form above list

# List is a Mutable ,
# but replace in string create a new string not changes into original string

# Best Method
A[0], A[3] = A[3], A[0]

print(A)

# WAP to add new value to the second position

A.insert(1 , "Maalik Kiase ho")
print(A)

# WAP to delete  value from the third 3rd position

# This Accept the string parameter
A.remove(A[2])
print(A)

# or via pop -> it accept the index , whatever u want to delete
A.pop(2)
print(A)



