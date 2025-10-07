# Question4:-
# WAPP to print each element of the array in
# reverse order.
# a)By running loop from 0 index
# b)By running loop from last index

def reverseOrderStart(A):
    for i in range(len(A)):
        print(A[len(A)-1-i],end=" ")

# reverese order from end function 
def reverseOrderEnd(A):
    for i in range(len(A)-1,-1,-1):
        print(A[i],end=" ")

# main function
if __name__=="__main__":
    A = [1,2,3,4,5]
    reverseOrderStart(A)
    print()
    reverseOrderEnd(A)
