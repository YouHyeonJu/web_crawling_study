import matplotlib.pyplot as plt
import pandas as pd
import csv

# f= open("Data3\weather.csv")
# data=csv.reader(f)
# for row in data:
#     print(row)
# f.close()

df=pd.read_csv("Data3\weather.csv",encoding="CP949",index_col=0)
print(df)