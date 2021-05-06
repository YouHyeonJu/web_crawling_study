import pandas as pd
weather= pd.read_csv("Data3\weather.csv",index_col=0,encoding='CP949')
print(weather.describe())
print("평균 분석-------------------------")
print(weather.mean())
print()
print(weather['평균기온(°C)'].mean())
print("표준편차 분석------------------------")
print(weather.std())