import matplotlib.pyplot as plt
import numpy as np
xData= np.arange(20,50)
yData=xData+2* np.random.randn(30)
plt.scatter(xData,yData,edgecolors='orange',color='limegreen')
plt.title('Real Age vs Physical Age',fontsize=25)
plt.xlabel("read Age")
plt.ylabel("Physical Age")
plt.show()