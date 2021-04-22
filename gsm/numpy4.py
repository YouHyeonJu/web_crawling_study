import numpy as np
y=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(y)
np_y=np.array(y)
print(np_y)

print(np_y[0])
print(np_y[0:2,2:4])
print(np_y[1,1:3])

print(np_y[1::2,1::2])
print(np_y[::2][::2])
print("end")
print(np_y[np_y>5])
print(np_y[np_y%2==0])

print(np_y[np_y[:,1]>5])