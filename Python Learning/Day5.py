# Dated :- 05/11/2025/Wednesday

my_list  = [2,4,5,6,7,8]

sliced_list  = my_list[::-2]
print(sliced_list)
print("---------------------------")
# remove and pop method 
my_list2 = [1,2,4,5,2,6,7,2]

my_list2.remove(2)
print(my_list2)

my_list2.pop(4)
print(my_list2)
print("------------------")

# check element present in the list or not
my_list3 = [2,4,6,9,7,1]
element_present = 3 in my_list3
print(element_present)

# count method 
my_list4=[3,3,3,3,5,6,7,8,3]
counted_number =my_list4.count(3)
print(counted_number)
print("-----------------------------")

# sort method in the list for sorting

my_list5 = [9,54,36,7,4,7,5,1]

my_list5.sort()

print(my_list5)

my_list5.sort(reverse=True)
print(my_list5)

print("----------------------------")

# Creating two lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30]

# Using zip() to combine elements from both lists into tuples
zipped_data = zip(names, ages)
print(zipped_data)
# Displaying the result
for data in zipped_data:
    print(data)
    print("Name:", data[0], "| Age:", data[1])



print("------------------------------------------")
# Q1. Flatten Nested List Write a Python function to flatten a nested list of arbitrary depth using recursion or iteration.
#  Example: Input: [1, [2, [3, 4], 5], [6, 7]] Output: [1, 2, 3, 4, 5, 6, 7] def flatten_list(data): pass

new_list =[]
def flattern_list(data):
    for values in data:
        if isinstance(values,list):
            flattern_list(values)
        else:
            new_list.append(values)
    
    return new_list


nested_list=[1, [2, [3, 4], 5], [6, 7]]
result = flattern_list(nested_list)
print(result)

# Q2. Word Frequency Given a string, return the top n most frequent words. 
# Example: s = 'python is great and python is dynamic and great' Output: [('python', 2), ('great', 2), ('is', 2)] 
from collections import Counter
def top_words(s, n):
    s = s.lower().split()
    count = Counter(s)
    print(count)
    values = count.most_common(n)
    print(values)


        
    

s ='python is great and python is dynamic and great'
top_words(s,3)

print("------------------------------------------")

def change_value(b):
    def wrapper(c):
        result = b(c)
        result = result.upper()
        return result
    return wrapper

@change_value
def greet(a):
    # print(a)
    return a

print(greet("hello"))


