# Dated:- 23/11/2025
# recursion concept
# Assignment:- 19
# sum of n natural number through Recursion
def sumN(n):
    if n == 0:
        return 0
    return n+sumN(n-1)

# sum of N odd natural number
def sumNodd(n):
    if n ==0:
        return 0
    return 2*n-1 + sumNodd(n-1)

# sum of N even natural number
def sumNEven(n):
    if n==0:
        return 0
    return 2*n +sumNEven(n-1)

# calculate the factorial of number
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
# sum of squares of first n natural numbers
def sumNSquare(n):
    if n ==0:
        return 0
    return n*n +sumNSquare(n-1)


# result1 = sumN(5)
# print(result1)
print(sumN(5))
print(sumNodd(10))
print(sumNEven(10))
print(fact(5))
print(sumNSquare(3))


