import numpy as np
import random

x=np.arange(12)
print(x)
y=x.reshape(3,4)
print(y)
z=y.flatten()
print(z)



print(np.random.rand(5))
print(np.random.rand(5,3))
print(np.random.randint(1,10,size=10))
print(np.random.randint(1,100,size=(3,5)))


print("end")
data_2=np.random.randint(1,10,size=10)
print(data_2)
print(data_2[::-1])
print(np.mean(data_2))
print(np.median(data_2))

print(data_2.sum())
print(data_2.mean())

print("end")
x=[i for i in range(100)]
y=[i ** 4 for i in range(100)]
print(x)
print(y)
result=np.corrcoef(x,y)
print(result)

print("end")

x=[i for i in range(10)]
y=[i ** 2 for i in range(10)]
z=[i for i in range(10,0,-1)]
print(x)
print(y)
print(z)
result= np.corrcoef([x,y,z])
print(result)
print("end")

num_arr=np.arange(1,21)
print(num_arr)
print(num_arr[::-1])
print(num_arr.sum())
print(num_arr.mean())
print(np.median(num_arr))
num_arr=num_arr.reshape(5,4)
print(num_arr)
