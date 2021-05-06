import csv
f= open("Data3\weather.csv")
data=csv.reader(f)
header=next(data)
max_wind=0.0
for row in data:
    if row[2]=='':
        wind=0
    else:
        wind=float(row[2])
    if max_wind<wind:
        max_wind=wind
print("지난 10년간 울릉도의 최대풍속중 초대값은 ",max_wind,"m/s")
data.read_csv(f,encoding='CP949')