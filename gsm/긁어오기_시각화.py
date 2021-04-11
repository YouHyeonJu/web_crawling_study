from  konlpy.tag import *
import matplotlib.pyplot as plt
from matplotlib import  font_manager , rc
from wordcloud import WordCloud
from collections import Counter

okt=Okt()
data1=open("C:/Users/hs46h/OneDrive/바탕 화면/동생/web_crawling_study/gsm/긁.txt").read()
data2=okt.nouns(data1)

data3=[]
for a in data2:
    if a=="언론사":
        data3.append(a.replace("언론사","유현주"))
    elif a=="제목":
        data3.append(a.replace("제목","유현주"))
    elif a=="내용":
        data3.append(a.replace("내용","유현주"))
    elif a=="번호":
        data3.append(a.replace("번호"," "))
    else:
        data3.append(a)

data4=Counter(data3)
data5=data4.most_common(100)

sword=open("C:/Users/hs46h/OneDrive/바탕 화면/동생/web_crawling_study/gsm/긁불용어.txt").read()
print(sword)
data6=[each_word for each_word in data3 if each_word not in sword]
data7=[]
for i in data6:
    if len(i)>=2 and len(i)<=10:
        data7.append(i)
data8=Counter(data7)

data9=data8.most_common(50)
print(data9)
word=dict(data9)
import numpy as np
from PIL import Image
from wordcloud import ImageColorGenerator
imarry=np.array(Image.open("C:/Users/hs46h/OneDrive/바탕 화면/동생/web_crawling_study/gsm/Data/star.jpg"))
save_image=("C:/Users/hs46h/OneDrive/바탕 화면/동생/web_crawling_study/gsm/Data/bigstar.jpg")
wordcloud=WordCloud(font_path="c:\\windows\\fonts\\H2GTRM.TTF",
                    relative_scaling=0.4,mask=imarry,
                    background_color='red').generate_from_frequencies(word)
plt.figure(figsize=(8,8))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig(save_image)
plt.show()

