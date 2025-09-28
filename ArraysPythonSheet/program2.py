
#Question:-2 For the given array of Strings, print and count all the Strings which has even number of characters.

# function decalration
def CountEvenStringInArray(A):
    count = 0
    for str in A:
        if (len(str))%2 ==0:
            count +=1
            print(str,end=" ")
    return count
# function declaration
def countEven(A):
    count = 0
    for str in A:
        if (len(str))%2==0:
            count+=1
            print(str,end ='')
    return count
# this is the main function
if __name__== "__main__":
     A = ["Apple", "Mango", "Banana"]
     
    #  CountEvenStringInArray(A)
     countEven(A)


# ------
