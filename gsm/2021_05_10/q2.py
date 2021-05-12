import numpy as np
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