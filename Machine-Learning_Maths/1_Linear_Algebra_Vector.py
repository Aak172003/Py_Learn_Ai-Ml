
import numpy as np

# --------------  find magnitude or distance of vector from origin  -------------------------

A = np.array([1, 2, 3, 4, 5])

# This is 5 dimension Vector
# This below function is used to find the magnitude of vector

distance = np.linalg.norm(A)
print("Distance : ", distance)


# --------------  find euclidean distance between two vector  -------------------------------

A = np.array([1,2,3,4,5])
B = np.array([6,7,8,9,10])

difference = A-B

# Calculate Euclidean distance between A and B
distance = np.linalg.norm(difference)

print('Euclidean Distance : ', distance)






