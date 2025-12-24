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

# arrange method() for the creation of the sequential array 
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

# it returns the array values from the array

# check the comparsion to compare the time taken in list creation
print("------->>>>before using the Numpy---------")
n = 10000
m1= [[e for e in range(n)] for i in range(n)]
m2 = [[e for e in range(n)] for i in range(n)]


start = time.time()

for i in range(n):
    for j in range(n):
        m1[i][j]+m2[i][j]

end = time.time()
print("%.6f sec "%(end-start))


print("----->>>>after using the Numpy")
start1 = time.time()

m3 = np.array(m1)
m4 = np.array(m2)
m1+m2

end1 = time.time()
print("%.6f sec"%(end1-start1))
