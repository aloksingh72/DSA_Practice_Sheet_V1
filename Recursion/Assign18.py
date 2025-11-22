# Dated:- 22/11/2025/Saturday
# Recursion Questions

# Ques:-1 print first n natural number 
def printNaturalNumber(n):
    if n>0:
        printNaturalNumber(n-1)
        print(n,end=" ")

def printNReverse(n):
    if n>0:
        print(n,end=" ")
        printNReverse(n-1)

def printOddNaturalNo(n):
    if n >0:
        printOddNaturalNo(n-1)
        print(2*n-1,end=" ")

def evenNaturalNo(n):
    if n>0:
        evenNaturalNo(n-1)
        print(2*n,end=" ")
def oddNaturalNumberRev(n):
    if n>0:
        print(2*n-1,end = " ")
        oddNaturalNumberRev(n-1)
def evenNaturalNoRev(n):
    if n>0:
        print(2*n,end=" ")
        evenNaturalNoRev(n-1)

printNaturalNumber(10)
print()
printNReverse(10)
print()
printOddNaturalNo(10)
print()
evenNaturalNo(10)
print()
oddNaturalNumberRev(10)
print()
evenNaturalNoRev(10)


