# WAPP to print and count all the palindrome
# number elements from array.
# Plaindrome:- Same backward as forward

# function  declaration
def countPlaindrome(A):
    count =0
    for num in A:
        orgNum =  num
        
        rev =0
        while(num>0):
            rem  = num%10
            rev = rev*10 +rem
            num = num//10
        
        if rev == orgNum:
            print(orgNum,end=" ")
            count +=1
    print("\ntotal palindrome numbers",count,end=" ")
         




# main function 
if __name__=="__main__":
    A=[121,544,999,66,83,707]
    countPlaindrome(A)

