from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
years=[1965,1975,1985,1995,2005,2015]
ko=[130,650,2450,11600,17790,27250]
jp=[890,5120,11500,52130,40560,38780]
ch=[100,200,290,540,1750,7940]
colors=sns.color_palette("Paired",len(years))

x_range= np.arange(len(years))
plt.bar(x_range+0.0,ko,width=0.25,color=colors)
plt.bar(x_range+0.3,jp,width=0.25,color=colors)
plt.bar(x_range+0.6,ch,width=0.25,color=colors)
plt.title("GDP per capita")
plt.ylabel("dollars")
plt.xticks(range(len(years)),years)
plt.show()