# Functions 

def add_numbers(a,b):
    result = a +b
    return result


ans = add_numbers(3,6)
print("the sum of two numners",ans)


# default values in function 

def greeting(name,greet = "hello"):
    print(f"{greet},{name} !")


# function calling
greeting("Alison")


# positonal and keywords arguments

def print_args(*args,**kwargs):
    print("Postional requirement",args)
    print("keywords arguments",kwargs)

print_args(1, 2, 3, name="Alice", age=30)

print("----------------------------------------------")
# use of the positional and keywords argument

def ex_funciton(args1,*args,kwargs1="default_value",**kwargs):
    print("args1:-",args1)
    print("additional arguments:-",args)
    print("keywords arguments:-",kwargs1)
    print("additonal keywords arguments:-",kwargs)

ex_funciton("value1","values2","values3",kwargs1="modifed values",key1 = "custom key",key2 = "another keys")



# lambda function

add_lambda = lambda x,y :x+y

result = add_lambda(5,6)
print(result)


# recusive fucntions

def factorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)


factorial(5)