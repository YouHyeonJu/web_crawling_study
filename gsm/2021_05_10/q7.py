import pandas as pd
import matplotlib.pyplot as plt
coutries_df=pd.read_csv("Data3\weather.csv",index_col=0,encoding='CP949')
print(coutries_df)
coutries_df['평균 풍속(m/s)'].plot(kind='hist',bins=33,color='yellowgreen')
plt.show()