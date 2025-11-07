# Dated:- 07/11/2025/Friday

student_info={
    "Name":"John",
    "Age":25,
    "City":"noida"
}

# using the get method

name = student_info.get("Name")
age = student_info.get("Age")

# Displaying the values
print("Name",name)
print("Age",age)

print("-------------------------------------")
# adding key values in existing dictionary
student_info2 = {
    "Name":"Alex Singh",
    "Age":26,
    "city":"Noida"
}
# adding the new key value pair

student_info2["Grade"] ="A"

print(student_info2)

print("---------------------------------------")
# Original dictionary
student_info3 = {"Name": "John", "Age": 25, "City": "New York"}

# Dictionary to be merged
additional_info = {"Grade": "A", "Hobbies": ["Reading", "Coding"]}

# Using update() to merge dictionaries
student_info3.update(additional_info)

# Displaying the updated dictionary
print(student_info3)