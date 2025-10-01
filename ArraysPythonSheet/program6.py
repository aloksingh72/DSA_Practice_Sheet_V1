# question 6:- WAPP to get sum of all the prime number
# elements from array.



def isPrime(num):
    if num<=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
        
        return True
    


def sumOfPrime(A):
     count =0
     sum = 0
     print("prime numbsers in array:- ", end="")

     for num in A:
         if isPrime(num):
             print(num,end=" ")
             count +=1
             sum = sum+num

     print("\n the count of the prime numbers is",count)
     print("\n the sum of the prime numbers is ",sum)


if __name__=="__main__":
    A= [2,5,6,9,8,3,6,7]
    sumOfPrime(A)