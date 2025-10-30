#Dated :- 30/10/2025/thursday
# the assert statement is used for debugging purposes. 
x = 8
assert x>0
print("the value of x is ",x)

# exception handling

def divide_numbers(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    else:
        print(f"Result:{result}")
    finally:
        print("this block is execute always")


divide_numbers(10,5)
divide_numbers(5,0)

print("---------------------------------------")

my_list = [1,"hello",4,5.6]

print(my_list[0])
print(my_list[1])

my_list[1] = "world"
print(my_list[1])


my_list.append(45)
print(my_list)

my_list.remove(5.6)
print(my_list)

# list slicing
subset = my_list[1:3]
print(subset)

print("-------------------------")
# difference between list and tuple

list1 = [3,5,6,8,9]
list1[1]=77
print(list1)

# tuple
my_tuple = (2,4,6,8)
# my_tuple[1]=44

# print(my_tuple)

print("------------------------------")

my_list.insert(1,"aloksingh")
print(my_list)


# Creating two lists
list3 = [1, 2, 3]
list4 = [4, 5, 6]

# Inserting list2 into list1 at index 1
list3.insert(1, list4)

# Displaying the updated list1
print(list3)  # Output: [1, [4, 5, 6], 2, 3]
