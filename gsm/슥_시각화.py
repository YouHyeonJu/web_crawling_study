from  konlpy.tag import *
import matplotlib.pyplot as plt
from matplotlib import  font_manager , rc
from wordcloud import WordCloud
from collections import Counter

okt=Okt()
data1=open("D:/3th/개발/빅데이터/web_crawling_study/gsm/Data2/슥.txt").read()
data2=okt.nouns(data1)
data3=[]
for i in data2:
    if i=="제목":
        data3.append(i.replace("제목","유현주"))
    elif i=="내용":
        data3.append(i.replace("내용","유현주"))
    elif i== "번호":
        data3.append(i.replace("번호"," "))
    else:
        data3.append(i)

data4=Counter(data3)
data5=data4.most_common(100)
sword=open("D:/3th/개발/빅데이터/web_crawling_study/gsm/Data2/슥불용어.txt").read()
data6=[each_word for each_word in data3 if each_word not in sword]
data7=[]
for i in data6:
    if len(i)>=2 and len(i)<=8:
        data7.append(i)
data8=Counter(data7)
data9=data8.most_common(50)
word=dict(data9)

