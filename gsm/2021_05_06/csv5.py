import pandas as pd
import matplotlib.pyplot as plt
df_no_index= pd.read_csv('Data3\countries.csv')
print(df_no_index)
df_my_index=pd.read_csv("Data3\countries.csv",index_col=0)
print(df_my_index)

print(df_my_index['population'])
print(df_my_index[['area','population']])