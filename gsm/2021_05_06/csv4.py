import pandas as pd
f_name="Data3\pandas_y.csv"

name=['이순신','김만덕','홍길동']
gender=['남','여','남']
age=[25,40,18]
first=pd.DataFrame()
first['이름']=name
first['성별']=gender
first['나이']=age

print(first)
first.to_csv(f_name,encoding="utf-8-sig",index=False)
name=pd.Series(['이순신','김만덕','홍길동'])
gender=pd.Series(['남','여','남'])
age=pd.Series([25,40,18])

second=pd.DataFrame()
second['이름']=name
second['성별']=gender
second['나이']=age
print(second)

third=pd.DataFrame({'이름':name,'성별':gender,'나이':age})
print(third)