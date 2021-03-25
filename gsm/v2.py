from konlpy.tag import *
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

from wordcloud import WordCloud
from collections import Counter

okt = Okt()
# kkma=Kkma()

data1 = open("Data/two.txt").read()
print(data1)

# print("kkma:",kkma.nouns("나는 사과,사과 , 복숭아, 복숭아가 좋아요"))
# print("kkma:",okt.nouns("나는 사과,사과 , 복숭아, 복숭아가 좋아요"))

data2 = okt.nouns(data1)
print("1. 추출된 키워드:",data2)

print('\n')
data3 =Counter(data2)
print("2.단어별 빈도수:",data3)

sword= open("Data/one.txt").read()

data4=[each_word for each_word in data2 if each_word not in sword]
print(data4)

data5=[]
for i in data4:
    if len(i)>= 2 | len(i) <= 10:
        data5.append(i)
print(data5)

data6=Counter(data5)
print(data6)
data7 = data6.most_common(10)
print(data7)

data8 = dict(data7)
print(data8)

wordcloud=WordCloud(font_path="c:\\windows\\fonts\\BMDOHYEON_ttf.ttf",
                    relative_scaling=0.5,
                    background_color="skyblue",
                    max_words=100,
                    max_font_size=200
                    ).generate_from_frequencies(data8)
plt.figure(figsize=(8,4))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()