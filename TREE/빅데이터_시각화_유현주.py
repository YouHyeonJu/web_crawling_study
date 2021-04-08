from  konlpy.tag import *
import matplotlib.pyplot as plt
from matplotlib import  font_manager , rc
from wordcloud import WordCloud
from collections import Counter

okt=Okt()

data1=open("D:/3학년/개발/빅데이터/TREE/Data/빅데이터_d.txt").read()
data2=okt.nouns(data1)

data3=[]
for a in data2:
    if a == "제목":
        data3.append(a.replace("제목", "유현주"))
    elif a == "내용":
        data3.append(a.replace("내용", "유현주"))
    elif a == "번호":
        data3.append(a.replace("번호", ""))
    else:
        data3.append(a)


data4=Counter(data3)

data5=data4.most_common(100)

sword=open("D:/3학년/개발/빅데이터/TREE/Data/빅데이터불용어.txt").read()
print(sword)
data6=[each_word for each_word in data3
if each_word not in sword]
data7=[]
for i in data6:
    if len(i)>=2 and len(i)<=5:
        data7.append(i)

data8=Counter(data7)
print(data8)
data9=data8.most_common(50)
print(data9)
word=dict(data9)
import numpy as np
from PIL import Image
from wordcloud import ImageColorGenerator
wat=np.array(Image.open("D:/3학년/개발/빅데이터/TREE/Data/korea.jpg"))
save_image=("D:/3학년/개발/빅데이터/TREE/Data/bigdata.jpg")
wordcloud = WordCloud(font_path="c:\\windows\\fonts\\H2GTRM.TTF",
                      relative_scaling=0.4,mask=wat,
                      background_color='white').generate_from_frequencies(word)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig(save_image)
plt.show()


