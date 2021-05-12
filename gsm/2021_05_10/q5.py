import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
fm.get_fontconfig_fonts()
import seaborn as sns
font_location="c:\\windows\\fonts\\H2GTRM.TTF"
font_name=fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)

x=[x for x in range(7,13)]
y=[456,492,578,599,670,854]
import seaborn as sns
colors= sns.color_palette('Set3',len(x))
font0={'family':'font_name',
        'color':'purple',
        'weight':'normal',
        'size': 16}
fig= plt.figure(figsize=(8,8))
ax=fig.add_subplot()
bars= plt.bar(range(len(x)),y,color=colors)
for i ,b in enumerate(bars):
    ax.text(b.get_x()+b.get_width()*(1/2),b.get_height()*(1/2),\
        y[i],ha='center',fontdict=font0)
plt.title("신규가입자",fontsize=25)
plt.ylabel("가입자 수",fontsize=15)
plt.xlabel("월",fontsize=15)
plt.xticks(range(len(x)),x,fontsize=15,color='green')
plt.show()