import pandas as pd
countries_df=pd.read_csv("Data3\countries.csv",index_col=0)

print(countries_df.head())
print()
print(countries_df[:3])
print()
print(countries_df.tail())
print()
print(countries_df.loc['KR'])
print()
print(countries_df['capital'].loc['KR'])
print()

countries_df['density']=countries_df['population']/countries_df['area']
print(countries_df)
print()
print(countries_df['population'][:3])
print()