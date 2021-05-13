import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
fm.get_fontconfig_fonts()
import seaborn as sns
import pandas as pd
font0={'family':'font_name','color':'red','weight':'normal','size':13}
months=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']


font_location="c:\\windows\\fonts\\H2GTRM.TTF"
font_name=fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)
weather=pd.read_csv("Data3\weather.csv",encoding='CP949')
weather['month']=pd.DatetimeIndex(weather["일시"]).month
means=weather.groupby('month').mean()
print(means)
print(means['평균기온(°C)'])
temp=means['평균기온(°C)']
print(temp)

plt.title("평균기온",fontsize=25)
plt.plot(temp,'blue',marker='o')
plt.xticks(range(len(months)),months)
for i in range(1,13):
    plt.text(i, temp[i], round(temp[i],2),fontdict=font0)
plt.show()