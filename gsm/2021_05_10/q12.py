import pandas as pd
import matplotlib.pyplot as plt
weather=pd.read_csv("Data3\weather.csv",encoding='CP949')
weather['month']=pd.DatetimeIndex(weather['일시']).month
means=weather.groupby('month').mean()

import seaborn as sns
colors=sns.color_palette('Paired',12)

means["평균기온(°C)"].plot(kind='bar',color=colors)
plt.title("Mean of Temperature",fontsize=25,color='green')
plt.show()
