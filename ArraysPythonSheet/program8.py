# WAPP to store first n prime numbers into array

def storePrime(n):
    primelist=[]
    num=2
    while len(primelist)<n:
        isPrime = True
        for i in range(2,int(num*0.5)+1):
            if num%i ==0:
                isPrime = False
                break
        if isPrime:
            primelist.append(num)
        num +=1
    
    print("First", n, "prime numbers are:",primelist)





if __name__=="__main__":
    storePrime(5)