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


print("-----------------------------------------")

removed_value = student_info3.pop("Age")
print("this is the removes value",removed_value)

print(student_info3)

print("-----------------------------------")


# Dictionary  comprehension
squared_values = {x:x**2 for x in range(1,6)}

#  
print(squared_values)

# to check the key present in the dictionary

if 'Name' in student_info:
    print("Name is present in the dictionay.")
else:
    print("the name key is not present in the dictionay. ")


print("--------------------------------")

sample_dict={
    'name':'John',
    'age':25
}
print(sample_dict)
sample_dict.clear()

print(sample_dict)


# nested dictionary

contacts={
    'person1':{
        'name':"Alex",
        'age':25,
        "email":"sample1@gmail.com"

    },
    'person2':{
        'name':"John",
        'age':35,
        "email":"sample2@gmail.com"

    }
}

# accesing the nested element in the dictionary
print("Contact details of the person1",contacts["person1"]["name"])
print("contact details of the person2",contacts["person2"]["email"])