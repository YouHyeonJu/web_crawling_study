import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
fm.get_fontconfig_fonts()

font_location="c:\\windows\\fonts\\H2GTRM.TTF"
font_name=fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)

x=[x for x in range(7,13)]
y=[456,492,578,599,670,854]
plt.plot(x,y,marker="o",color="orange")
plt.xlabel("Month",fontsize=15)
plt.ylabel("User",fontsize=15)
plt.title("신규사용자",fontsize=25)
font0={'family':font_name,'color':'purple','weight':'normal','size':16}
for i in range(6):
    plt.text(x[i],y[i],y[i],fontdict=font0)
plt.show()