import matplotlib.pyplot as plt
import seaborn as sns

fig, ax= plt.subplots(1,4,figsize=(10,3))
x=[x for x in range(7,13)]
y=[456,492,578,599,670,854]

colors=sns.color_palette('Paired',len(y))
ax[0].bar(x,y,color=colors)
ax[1].plot(x,y,color="green",marker='o')
ax[2].scatter(x,y,color='skyblue')
ax[3].barh(x,y,color=colors)
plt.show()