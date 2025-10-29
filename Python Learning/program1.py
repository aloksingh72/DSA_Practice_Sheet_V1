#Dated :- 29/10/2025/Wednesday

# Variable type conversion example
integer_variable = 42
float_variable = 3.14
string_variable = "123"

# Converting integer to float
float_from_integer = float(integer_variable)
print("Float from integer:", float_from_integer)

# Converting float to integer
integer_from_float = int(float_variable)
print("Integer from float:", integer_from_float)

# Converting string to integer
integer_from_string = int(string_variable)
print("Integer from string:", integer_from_string)

print("=========shallow copy and deep copy=======")

import copy
original_list = [1,[2,3],5]
shallow_copy = copy.copy(original_list)

original_list[1][0]='X'
print(original_list)
print(shallow_copy)

deep_copy = copy.deepcopy(original_list)
original_list[1][0]='Y'

print("============deep copy====")
print(original_list)
print(deep_copy)