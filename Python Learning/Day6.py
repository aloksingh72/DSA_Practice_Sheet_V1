# Dated:- 06/11/2025/Thursday


# Set data types
my_set = {1,4,5,7,7,7,7,8,9,3}
print(my_set)

my_set.add(56)
print(my_set)

my_set.update({4,78})
print(my_set)

my_set.remove(1)
print(my_set)


# Creating a set
my_set2 = {3, 1, 5, 2}

# Displaying the set
print("Unordered Set:", my_set2)

print("------------------------------------")
# union, intersection and difference in set

my_set3 = {1,2,3,4,5,6}
my_set4 = {6,7,8,9}

union_set = my_set3.union(my_set4)
print(union_set)

intersection_set = my_set3.intersection(my_set4)
print(intersection_set)

difference_set = my_set3.difference(my_set4)
print(difference_set)

print("------------------------------------------")

# Forzen set
original_set = {3,4,57,89}

frozen_set = frozenset(original_set)
print(frozen_set)

try:
    frozen_set.add(6)
except AttributeError as e:
    print(f"Error:{e}")


print("original set:",original_set)
print("Frozen set",frozen_set)


print("------------------------------------------")

set1 = {1,2,3,4,5}
set2 = {5,4}

is_subset_method = set2.issubset(set1)
print(is_subset_method)


print("--------------------------------")

# set comprehension
squares = {x**2 for x in range(1,6)}
print("Set of squares",squares)

# list comprehension
squares_list = [x**2 for x in range(2,7)]
print("List of squares:- ",squares_list)

print("---------------------------")

# Dictionary 

person={
    "Name":"John",
    "Age":25,
    "City":"Noida"
}

# acessing values
print("Name:",person["Name"])
print("Age:",person["Age"])
print("City:",person["City"])


