import numpy as np
import random

# This return inside array
print(np.random.random(1))

# If I want to create 2d array with random number

# This generates only between 0 and 1
print(np.random.random((3, 3)))

# this is used when I want a random number from 4 to 5 within an array
print(np.random.uniform(4, 5, (3, 3)))


# This give proper int value
x = random.randint(1, 10)
print(x)

# If I want Random strings between predefined Strings
predefined = ['Heads', 'Tails', 'Nothing', 'Both']
getValue = random.choice(predefined)
print(getValue)

# ----------------------------------------------------------------

# create a random 2d array with random keyword

arr_random_float = np.random.random((3, 3))
arr_int = np.random.randint(5, 10, (3, 3))

print(arr_random_float)
print(arr_int)

# create 3d array with rand function

# arr_random_float_3d = np.random.random((3, 3,3))
# arr_int_3d = np.random.randint(1, 10, (3, 3,3))

# print(arr_random_float_3d)
# print(arr_int_3d)

# ------------------------------- Seed ( ***** ) ------------------------

# This seed function is used to memorize the random value

# Set seed to make random numbers reproducible
np.random.seed(123)

# Generate random numbers
random_numbers = np.random.randint(5)
print("Random numbers (seed=123):", random_numbers)

# Changing seed will produce a different sequence of random numbers
np.random.seed(456)
random_numbers_new = np.random.randint(5)
print("Random numbers (seed=456):", random_numbers_new)

np.random.seed(123)
print("Again Print (seed=123):", random_numbers)

np.random.seed(200)
random_numbers_new_200 = np.random.randint(2)
print("Random numbers (seed=200):", random_numbers_new_200)

np.random.seed(200)
print("Again Print (seed=200):", random_numbers_new_200)

np.random.seed(123)
print("Again Print (seed=123):", random_numbers)

# ------------------------------- ------------- ------------------------

# rand -> this is used to create random nd.array
# randn -> this is also similar to rand, the only difference is this will give a -ve and +ve value collection

array = np.random.rand(3)  # of array size 3
array_2d = np.random.rand(3, 3)

print(array)
print(array_2d)

arr_3d = np.random.randn(3, 3)
print(arr_3d)

# ------------------------------- Permutations  ------------- ------------------------

# Permutations -> does not work in ide, but this works in Jupyter Notebook, and this return in list form

predefined_title = ['Heads', 'Tails', 'Nothing', 'Both']
print(np.random.permutation(predefined_title))
