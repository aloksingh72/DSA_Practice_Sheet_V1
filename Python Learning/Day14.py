#Dated:- 15/12/2025
# 


# important example of that affect eh original list and creates new memory location
from typing import List


def modify_list(items):
    items.append(100)
    items = items +[200]
    return items

my_list = [1,2,3]
result = modify_list(my_list)

print("after function call: ",my_list)
print("Function returned: ",result)

print("-----------------------------")
#creates the new list 

def func(x):
    x = x+[10]
    return x
    
lst1= [1,2,3]
result1=func(lst1)
print(lst1)  
print(result1)
print("-----------------------------")



def add_item(items,lst=None):
    if lst is None:
        lst = []
    lst.append(items)
    return lst



print(add_item(1))
print(add_item(2))
print(add_item(3))


print("------------------------")
funcs = []

for i in range(3):
    funcs.append(lambda: i)

for f in funcs:
    print(f())




print("check if duplicate present------>")

nums = [1,2,3,4,5]
class Soluton:
    def containsDuplicate(self,nums:List[int]):
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False    
obj = Soluton()
result1 = obj.containsDuplicate(nums)
print(result1)

