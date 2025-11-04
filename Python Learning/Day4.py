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


print("-------------------------------------------------")
# recusive fucntions

def factorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)


ans = factorial(5)

print("the factorial of :- ",ans)


print("--------------------------------------------------")

def calculate_area(len,width):
    """
    this is the dummy calculate area
    document inside the doc string literials

    """
    area = len *width
    return area

area = calculate_area(5,6)

print(calculate_area.__doc__)
print("the area of  the rectangle",area)

print("-------------------------------------------------")

def outer_function(x):
    # Inner function is defined within the scope of outer_function
    def inner_function(y):
      
        return x + y
    # Return the inner function, creating a closure
    return inner_function

# Create closures with different values of x
closure_1 = outer_function(10)
closure_2 = outer_function(5)

# Call the closures with different values of y
result_1 = closure_1(3)
result_2 = closure_2(3)

# Print the results
print(result_1)  # Output: 13
print(result_2)  # Output: 8



print("-----------------------------------------")

numbers= [1,2,3,4,5]
squared = list(map(lambda x:x**2,numbers))


even_numbers = list(filter(lambda x:x%2 ==0,numbers))
print("Squared numbers:-",squared)
print("Filter  even numbers",even_numbers)

print("----------------------------------------")


# decorators
import time
def my_decorators(func):
    def wrapper():
        start  =  time.time()
        print("before the function calling")
        func()
        print("after the function calling")
        end= time.time()
        print("time taken",end-start,"seconds")
    return wrapper

@my_decorators
def say_hello():
    print("Hello!")
    time.sleep(3)

say_hello()

print("--------------------------------------------")


