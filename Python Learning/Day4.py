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