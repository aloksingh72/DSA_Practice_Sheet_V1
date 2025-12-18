# Dated:- 18/12/2025


# Numpy in python 


# pip install numpy
import numpy as np
import time
# normal list
lst = [1,2,3,4]


arr  =np.array([1,2,3,4,5])
print(arr)


# some common array creations method
arr2 = np.zeros(5) 
print(arr2)

arr3 = np.ones(5)
print(arr3)

# arrange method()
arrr3 = np.arange(10)
print(arrr3)

# vectorization operations over array
# basically vectorization  means applying operations on entire arrays without explicit loops in it.

# normal way (python way)
lst = [1,2,3,4,5]
result =[]
for  i in lst:
    result.append(i*2)

print(result)


arr = np.array([1,2,3,4,5])
print(arr*2)

print("----------------------------------")
# additio performing using the vectorization 
a = np.array([1,2,3,4])
b= np.array([2,3,4,8])

print(a+b)

print("----------")

# mathematical formula on dataset
x = np.array([1,2,3,4])
y= 3*x**2  + 2*x+1
print(y)

print("--------2D array multiplication-------------------")
arr4 = np.array([[1,2,3],[4,5,6]])
print(arr4 *10)

print("-----------check the execution speed of the vectorization numpy uses------------")

arr6 = np.arange(100000)

start = time.time()
arr6*2
end = time.time()

resulttime = end-start
print(resulttime)


print("------------Boolean masking")

arr = np.array([10, 20, 30, 40, 50])

mask = arr > 25  #return true or false
print(mask)
print(arr[arr>20])
