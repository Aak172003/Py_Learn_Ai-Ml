# Set are unordered collection of data. Every element inside the set is unique and mutable
# Here no indexing present in a set

# a = {"a", "b", "c", "d"}

# print("this is a : ", a)
# print(type(a))

# Iteration in Sets
# for i in a:
#     print(i)

# ******************************  Set Functions ***********************************

# add: add an element in a set at random position
# a.add("e")
# print("this is a : ", a)

# pop: remove an element from last
# popped_element = a.pop()
# print(popped_element)
# print(a)

# Remove: This method removes the specified element from the set.
# If the element is not present, it raises a KeyError.

# a.remove('k')
# print(a)

# discard: This method removes the specified element from the set if it is present.
# Unlike remove(), it does not raise an error if the element is not found.

# a.discard('k')
# print(a)

# copy

# b = a.copy()
# print("this is b : ", b)

# ******************************  Set Functions - 2  ***********************************

# a1 = {"IronMan", "Hulk", "Thor", "Caption America"}
# b1 = {"SuperMan", "Batman", "Wonder-Women"}
# c1 = {"Hulk", "Thor"}

# isdisjoint: check set a has every element of set b or not
# if not return true otherwise false

# print("This is Disjoint Result: ", a1.isdisjoint(b1))

# --------------------------------------------------------------------

# issubset
# c1 ke element is present in a1 or not

# print("This is Subset Result : ", c1.issubset(a1))

# --------------------------------------------------------------------

# issuperset: all element present
# c1(set-b) all element present in set a1(set-a)

# print("This is Superset Result: ", a1.issuperset(c1))

# --------------------------------------------------------------------

# update: Perform Union Operation
# between a1 and b1 (add those elements of b1 which I not present in a1)
# a1.update(b1)
# print(a1)

# --------------------------------------------------------------------

# clear: This will clear the set

# a1.clear()
# print(a1)

# a1.add(12)
# print(a1)


# ******************************  Set Functions - 3  ***********************************

first = {"IronMan", "Thor", "Hulk", "Caption America"}
second = {"SuperMan", "Batman", "IronMan", "Wonder-Women"}
third = {"Hulk", "Thor"}

print(first)

# Union: Remove duplicate data, and add only single occurrence data
# unionData = first.union(second)
# print("unionData : ", unionData)

# --------------------------------------------------------------------

# Difference: return a new lists of sets of those elements which are not present in b1
# difference_Element = first.difference(second)
# print("difference_Element : ", difference_Element)

# This is not reflecting the original
# print(first)

# --------------------------------------------------------------------

# Difference Update: This is the same as Difference, but different is this performs operation on the original set
# But above Difference does not perform any operation on an original set, return another

# print("Before : ", first)
#
# # return none, because this not returns anything, this basically updates the original set
# difference_Element = first.difference_update(second)
# print("difference_Element : ", difference_Element)
#
# print("After : ", first)

# --------------------------------------------------------------------

# Intersection

# # returns a new lists of sets of those elements which are common in both first and third
# unique_sets = first.intersection(third)
# print("unique_sets : ", unique_sets)
#
# print(first)

# --------------------------------------------------------------------

# Intersection Update:

# This is the same as Intersection, but different is this performs operation on the original set,
# But above Intersection does not perform any operation on an original set, return another set

# unique_sets = first.intersection_update(third)
# # return none, because this not returns anything, this basically updates the original set
# print("unique_sets : ", unique_sets)
# print(first)

# --------------------------------------------------------------------

# Symmetric Difference:

# Return all values except common values from sets
# returns a new lists of sets of those elements which are not common in both first and third

notCommon_Element = first.symmetric_difference(second)

print("notCommon_Element : ", notCommon_Element)
print(first)

# --------------------------------------------------------------------

# Symmetric Difference Update :

# This is the same as symmetric_difference, but different is this performs operation on the original set
# But above symmetric_difference does not perform any operation on an original set, return another set


# return none, because this not returns anything, this basically updates the original set
notCommon_Element = first.symmetric_difference_update(second)

print("notCommon_Element : ", notCommon_Element)
print(first)

