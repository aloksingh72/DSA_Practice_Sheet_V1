
# Question:-3 For the given array of Strings, print the largest string.
def LargestString(A):
    largest = A[0]
    for str in A:
        if len(str) > len(largest):
            largest = str
    return largest


if __name__=="__main__":
    A=["mango","Banana","Graphes","Lichee"]
    largest = LargestString(A)
    print("the largest string in given array is:- ",largest)
