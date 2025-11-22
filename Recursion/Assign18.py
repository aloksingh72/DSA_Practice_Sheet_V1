# Dated:- 22/11/2025/Saturday
# Recursion Questions

# Ques:-1 print first n natural number 
def printNaturalNumber(n):
    if n>0:
        printNaturalNumber(n-1)
        print(n,end=" ")

printNaturalNumber(5)

