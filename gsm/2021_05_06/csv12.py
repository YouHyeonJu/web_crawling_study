import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import pandas as pd
fm.get_fontconfig_fonts()
import seaborn as sns
font_location="c:\\windows\\fonts\\H2GTRM.TTF"
font_name=fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)
font0={'family':'font_name','color':'red','weight':'normal','size':13}
months=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']

weather= pd.read_csv("Data3\weather.csv",encoding='CP949')
monthly=[0 for x in range(12)]
monthly_wind=[0 for x in range(12)]

weather['month']=pd.DatetimeIndex(weather['일시']).month
for i in range(12):
    monthly[i]=weather[weather['month']==i+1]
    monthly_wind[i]=monthly[i]['평균 풍속(m/s)'].mean()

plt.title("울릉도의 풍속",fontsize=25)
plt.plot(monthly_wind,'blue',marker='o')
plt.xticks(range(len(months)),months)
for i in range(12):
    plt.text(i,monthly_wind[i],round(monthly_wind[i],2),fontdict=font0)
plt.show()