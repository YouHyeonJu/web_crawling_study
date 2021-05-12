import pandas as pd
import matplotlib.pyplot as plt

weather=pd.read_csv("Data3\weather.csv",encoding='CP949')
monthly=[0 for x in range(12)]
monthly_wind=[0 for x in range(12)]
weather['month']=pd.DatetimeIndex(weather['일시']).month

for i in range(12):
    monthly[i]=weather[weather['month']==i+1]
    monthly_wind[i]=monthly[i]['평균 풍속(m/s)'].mean()
plt.plot(monthly_wind,'red')
plt.show()