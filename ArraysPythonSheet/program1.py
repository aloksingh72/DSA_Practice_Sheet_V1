# Print biggest element , smallest elements and their difference from the given array.


# print("hello")
# a=12
# b=12
# sum = a+b
# print("The sum of two number",sum)

def biggestSmallestDifference(A):
    biggest = float('-inf')
    smallest = float('inf')

    for num in A:
        if(num >biggest):
            biggest = num
        if(num <smallest):
            smallest = num
    
    diff = biggest-smallest
    print("the biggest number is ",biggest)
    print("the smallest number is ",smallest)
    print("the difference among the number is ",diff)
    return

if __name__ == "__main__":
    A=[1,5,9,7,6,3]
    biggestSmallestDifference(A)