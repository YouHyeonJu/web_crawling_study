import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
fm.get_fontconfig_fonts()

font_location="C:\\windows\\fonts\\H2GTRM.TTF"
font_name=fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)

books=[1,6,2,3,1,2,0,2,7]
num_book=['0~1미만','1~2미만','2~3미만','3~4미만',
'4~5미만','5~6미만','6~7미만','7~8미만']
plt.hist(books,bins=8,color='gold',alpha=0.7,rwidth=0.9)
plt.title("학생들의 독서량",fontsize=25)
plt.xlabel("books")
plt.ylabel("frequency")
plt.xticks(range(8),num_book)
plt.show()