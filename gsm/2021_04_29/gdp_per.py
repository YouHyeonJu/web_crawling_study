import matplotlib.pyplot as plt
import seaborn as sns
years= [1950,1960,1970,1980,1990,2000,2010]
gdp = [67.0,80.0,257.0,1686.0,6505,11865.3,22105.3]
tick_size=13
axis_label_size=15
colors=sns.color_palette("hls",len(years))

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot()
bars=plt.bar(range(len(years)),gdp,color=colors)

for i,b in enumerate(bars):
    ax.text(b.get_x()+b.get_width()*(1/2),b.get_height()*(1/2),gdp[i],ha='center',fontsize=10)

plt.title("GDP per capita", fontsize=25)

plt.ylabel("dollars",fontsize=axis_label_size)
plt.xlabel("years",fontsize=axis_label_size)

plt.xticks(range(len(years)),years,fontsize=tick_size)
plt.show()