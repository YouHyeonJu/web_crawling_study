import numpy as np
import matplotlib.pyplot as plt
num_1=np.arange(1,31)
print(num_1)
print(num_1[::-1])
print(num_1.sum())
print(num_1.mean())
print(np.median(num_1))
num_2=num_1+5
print(num_2)
result=np.corrcoef([num_1,num_2])
print(result)
num_1=num_1.reshape(6,5)
print(num_1)

n_arr=np.arange(25).reshape(5,5)
np_arr=n_arr[::2,::2]
print(np_arr)

x=[x for x in range(-10,10)]
y1=[2*t for t in x]
plt.plot(x,y1,color='green',marker='o')
plt.show()
