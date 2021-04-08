from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

query_txt="빅데이터"
f_name="D:/3학년/개발/빅데이터/TREE/Data/빅데이터_d.txt"
fc_name="D:/3학년/개발/빅데이터/TREE/Data/빅데이터_d.csv"
path="C:/Temp/chromedriver.exe"
driver= webdriver.Chrome(path)

driver.get("https://www.daum.net/")
time.sleep(2)
driver.maximize_window()

element= driver.find_element_by_id("q")
element.send_keys(query_txt)
element.submit()

driver.find_element_by_link_text("뉴스").click()

number=[]
title_l=[]
content_l=[]

no=1

html = driver.page_source
soup= BeautifulSoup(html,'html.parser')

content_list=soup.find('ul',class_='list_info mg_cont clear').find_all('li')
print("\n")

for i in content_list:
    try:
        title=i.find("div","wrap_tit mg_tit").get_text()
        title_l.append(title)
        print('제목:',title)
        print("\n")
    except:
        pass

    try:
        content=i.find("p",class_="f_eb desc").get_text()
        content_l.append(content)
        print('내용:',content)
        print("\n")
    except:
        pass

f=open(f_name,'w',encoding='UTF-8')
for i in range(0,len(title_l)):
    f.write('번호:'+str(no)+"\n")
    f.write('제목:'+str(title_l[i])+"\n")
    f.write('내용:'+str(content_l[i])+"\n")
    no+=1
f.close()
print("txt 파일 저장 경로: %s" % f_name)

no= list(range(1,len(title_l)+1))
korea_trip=pd.DataFrame()
korea_trip['번호']=pd.Series(no)
korea_trip['제목']=pd.Series(title_l)
korea_trip['내용']=pd.Series(content_l)
korea_trip.to_csv(fc_name,encoding="utf-8-sig",index=False)
print("csv 파일 저장 경로: %s"% fc_name)

df= pd.read_csv(fc_name,index_col=0)
print(df)
print(df['제목'])
print(df['내용'])