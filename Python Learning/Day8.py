# Dated:- 10/11/2025/Monday
# a = b = 256
# print(a is b)

# a = b = 300
# print(a is b)

# def remove_dupes(nums):
#     result =[]
#     for n in nums:
#         if n not in result:
#             result.append(n)



class A:
    def show(self):
        print("A")
    
class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B,C):
    pass

D().show()


def check(n):
    if n<=1:
        return n
    return check(n-1)+check(n-2)




