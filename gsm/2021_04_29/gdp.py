import matplotlib.pyplot as plt
years= [1950,1960,1970,1980,1990,2000,2010]
gdp = [67.0,80.0,257.0,1686.0,6505,11865.3,22105.3]

plt.plot(years,gdp,color="green",marker='o',linestyle='solid')
axis_label_size=15
plt.title("GDP per capita of korea", fontsize=20)
plt.ylabel("dollars",fontsize=axis_label_size)
plt.xlabel("year",fontsize=axis_label_size)
plt.savefig("gdp_per_capita.png")
plt.show( )