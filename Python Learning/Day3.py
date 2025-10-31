my_list = [1,"hello",4,5.6]

my_list.insert(1,"aloksingh")
print(my_list)

# ------extend and insert method----------
# Creating two lists
list3 = [1, 2, 3]
list4 = [4, 5, 6]

# Inserting list2 into list1 at index 1
list3.insert(1, list4)

# Displaying the updated list1
print(list3)  # Output: [1, [4, 5, 6], 2, 3]


