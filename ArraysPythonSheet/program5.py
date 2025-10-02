# Question 5:- WAPP to print and count all the prime number
# elements from array.


# function to check the is prime or not
def isPrime(num):
    if num <=1:
        return False

    for i in range(2,int(num**0.5)+1):
        if num %i ==0:
            return False
    return True

        

# function to count the prime number and print the array
def countPrime(A):
    prime_list = []
    for num in A:
        if isPrime(num):
            prime_list.append(num)
    
    print("Print the prime numbers in the array:-",prime_list)
    print("the prime numbers count",len(prime_list))

# this is the main function 
if __name__=="__main__":
    A = [10, 2, 3, 4, 5, 7, 9, 11, 13, 15]
    countPrime(A)

