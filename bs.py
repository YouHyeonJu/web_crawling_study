
from bs4 import BeautifulSoup

with open("Data/bs2.html",'r',encoding='cp949')as ex:
    soup= BeautifulSoup(ex,"html.parser")

img_src_2017=[]
img_src_2018=[]
img_src = soup.find('div', 'flex_grid credits search_results').find_all('img')
for c in img_src:
    img_src1=c['src']
    if '2017' in img_src1:
        img_src_2017.append(img_src1)
    elif '2018' in img_src1:
        img_src_2018.append(img_src1)




