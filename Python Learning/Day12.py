# Dated:- 03/12/2025
import copy

list1 = [[1,2],[3,4]]

shallow = copy.copy(list1)
shallow[0][1] = 99

print("original list",list1)
print("shallow copied list",shallow)


print("----------------------------")

print("------------------------------")

list2 = [[2,4],[6,7]]
deep = copy.deepcopy(list2)
deep[0][1] =89
print("original list",list2)
print("Deep list copy",deep)