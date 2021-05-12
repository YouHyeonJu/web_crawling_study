import pandas as pd
import matplotlib.pyplot as plt
coutries_df=pd.read_csv("Data3\countries.csv",index_col=0)
print(coutries_df)
coutries_df['population'].plot(kind='bar',color=('b','darkorange','g','r','m'))
plt.legend()
plt.show()