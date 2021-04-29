import matplotlib.pyplot as plt
import matplotlib
#한글설정
import matplotlib.font_manager as fm
fm.get_fontconfig_fonts()

font_location="C:\\windows\\fonts\\H2GTRM.TTF"
font_name=fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)
times=[8,14,2]

timelabels=["잠","공부","놀기"]

colors=['gold','skyblue','yellowgreen']
explode=[0.05,0.05,0.05]
wedgeprops={'width':0.7,'edgecolor':'w','linewidth':3}
plt.pie(times,labels=timelabels,autopct='%.2f'\
    ,colors=colors,explode=explode,shadow=True,wedgeprops=wedgeprops)
plt.show()