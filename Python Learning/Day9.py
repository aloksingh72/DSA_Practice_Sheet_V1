# Dated:- 28/11/2025/Friday


# Generators
def generate_sqaures(n):
    for i in range(n):
        yield i **2


squares = list(generate_sqaures(5))
print(squares)

# regular functions
def regular_functions(n):
    result =[]
    for i in range(n):
        result.append(i**2)
    return result

print(regular_functions(5))


# --------------------------------------------------------------
# to check the memoty usage of the generators an regular functions

large_list = regular_functions(100000)
generator_list = generate_sqaures(100000)

import sys
print("regular funcitons size",sys.getsizeof(large_list))
print("Generator funcitons size",sys.getsizeof(generator_list))


# ----------------------------------------------------------------
# generate_sequence function
def generate_sequence(limit):
    i = 0
    while i < limit:
        yield i
        i += 1

# Create a generator with a limit of 3
limited_generator = generate_sequence(3)

# Use next() to get the next value
value1 = next(limited_generator)
value2 = next(limited_generator)
value3 = next(limited_generator)

# Attempt to get the next value (generator is exhausted)
try:
    value4 = next(limited_generator)
except StopIteration as e:
    exhausted_message = str(e)

print("Values using next():", value1, value2, value3)
print("Exhausted Message:", exhausted_message)

# ------------------------------------------------------------
# generator expressions

generator_expression = (x ** 2 for x in range(5))

print("Generator expression",list(generator_expression))

# --------------------------------------------------------

