import pandas as pd
weather=pd.read_csv("Data3\weather.csv",encoding="CP949")
weather['month']=pd.DatetimeIndex(weather['일시']).month
means=weather.groupby('month').mean()
print(means)
print(means['평균기온(°C)'])