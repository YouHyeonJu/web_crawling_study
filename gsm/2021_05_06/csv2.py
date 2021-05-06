import csv
f= open("Data3\weather.csv")
data=csv.reader(f)
header=next(data)
for row in data:
    print(row[3],end=',')
f.close()