# reverser the number
num = 1234
rev= 0
while num >0:
     rem = num %10
     rev  = (rev*10) +rem
     num = num // 10

print("the reverse of the number",rev)

print("----------------------------------")
# reverse a string
string= "Mango"
revstr = ""
for i in range(len(string)-1,-1,-1):
    revstr += string[i]
print("the reverse string",revstr)

print("-----------------------------------")

# palindrome string
num = 12321
pal = num 
rev = 0
while num>0:
    rem = num %10
    rev = (rev*10) +rem
    num = num //10

if pal == rev:
    print("this is plaindrome")
else:
    print("this is not plaindrome")
    
print("------------------------------------")

# check the number is  Armstrong number
# approcah-1
# num = 153
# arm  = num 
# no_of_digit = len(str(num))
# total = 0

# while num >0:
#     rem  = num %10
#     total = total +(rem ** no_of_digit)
#     num = num //10
# if arm == total:
#     print("the given no is Armstrong number",arm)
# else:
#     print("this is not Armstrong number.")
    
# ----->>>approach-2
num = 153
arm = num 
# calculation of no. of digit
temp = num 
count = 0
while temp>0:
    # rem = temp%10
    count +=1
    temp = temp//10
# armstrong calculation
total =0
while num >0:
    rem  = num %10
    total = total +(rem **count)
    num = num //10

if total == arm:
    print("this is armstrong number",arm)
else:
    print("this is not armstrong no",arm)
    
    
print("---------------------------------")
#facotial number

n = int(input("enter the number"))
# using for loop
# fact = 1
# for i in range(1,n+1):
#     fact = fact *i
    
# print(fact)

# using fucniton 

# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact*i
#     return fact

# result = factorial(n)
# print("the factorial of the number is ",result)


# using the recursion
def fact(n):
    if n ==0 or n==1:
        return 1
    return n*fact(n-1)
    
result = fact(n)
print("the factorial of the number is ",result)


# fibonacci series



























    
    



















