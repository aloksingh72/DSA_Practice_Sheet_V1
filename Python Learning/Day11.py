# Dated:- 02/12/2025

import numpy as np
import time

import pandas as pd
arr = np.array([1,2,3,4])

print(arr*2)


# What is Numpy ?
# ----> NumPy Python ka maths & scientific calculation library hai.
# ----> Iske andar fast arrays (NumPy arrays) hote hain.

# why we use the numpy 
# ----------execution time difference
# using the python list
python_list = list(range(10000000))

start = time.time()
python_result = [x*2 for x in python_list]
end = time.time()

final_result = end -start
print("Python list time:- ",final_result)



# using  the NumPy library

numpy_array = np.arange(10000000)
start = time.time()
numpy_result = numpy_array *2
end = time.time()

numpy_time = end -start
print("Numpy execution time",numpy_time)


# -------------------------------------------------------

data = {
    "Name":["Alok","Rahul"],
    "Age":[22,25],
    "City":["Ayodhya","Bareilly"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("-------------------------------")
# --------- SEARCH / FILTER METHODS ---------

# 1. Filter by column value (Age > 22)
print("\n1. Filter Age > 22:")
result1 = df[df["Age"] > 22]
print(result1)

result3 = df["Age"] ==22

result4 = df[df["Age"] ==22]
print(result3)
print("-------------->>>")
print(result4)

print("------------------------------")

# 2. Filter by string match (Name contains 'Alok')
print("\n2. Filter Name == 'Alok':")
result2 = df[df["Name"] == "Alok"]
print(result2)



class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return "Woof!"

# Creating an instance of the subclass
dog_instance = Dog("Buddy", "Labrador")

# Accessing attributes
print(dog_instance.name)   # Output: Buddy
print(dog_instance.breed)  # Output: Labrador






