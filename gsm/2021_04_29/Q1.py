import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib
fm.get_fontconfig_fonts()

font_location="C:\\windows\\fonts\\H2GTRM.TTF"
font_name=fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)

x=[x for x in range(7,13)]
y=[456,492,578,599,670,854]
plt.plot(x,y,marker="o",color="orange")
plt.xlabel('month',fontsize=15)
plt.ylabel('User',fontsize=15)
plt.title("신규사용자",fontsize=25)
plt.show()