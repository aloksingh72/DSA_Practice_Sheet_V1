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


