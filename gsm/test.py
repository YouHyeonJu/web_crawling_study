from  konlpy.tag import *
import matplotlib.pyplot as plt
from matplotlib import  font_manager , rc
from wordcloud import WordCloud
from collections import Counter

okt=Okt()

data1=open("D:/3학년/개발/빅데이터/TREE/Data/빅데이터.txt").read()
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
print(data3)