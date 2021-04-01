from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
query_txt = "여름여행"

f_name = "D:/3th/개발/빅데이터/web_crawling_study/gsm/Data/여름여행_k.txt"
fc_name = "D:/3th/개발/빅데이터/web_crawling_study/gsm/Data/여름여행_k.csv"

path = "c:/temp/chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get("https://korean.visitkorea.or.kr")
driver.maximize_window()
try:
    driver.find_element_by_xpath('//*[@id="safetyStay1"]/div[1]/div/div/button').click()
except:
    print('')
element=driver.find_element_by_id("inp_search")
element.send_keys(query_txt)
element.send_keys("\n")

html = driver.page_source
soup= BeautifulSoup(html,'html.parser')

content_list=soup.find('ul',class_='list_thumType type1').find_all('li')
print("\n")

no2=[]
contents2=[]
tags2=[]
no=1

for i in content_list:
    try:
        title=i.find("div","tit").get_text()
        contents2.append(title)
        print('내용:',title)
        print("\n")
    except:
        pass

    try:
        hash=i.find("p",class_="tag_type").get_text()
        tags2.append(hash)
        print('태그:',hash)
        print("\n")
    except:
        pass

f=open(f_name,'w',encoding='UTF-8')
for i in range(0,len(contents2)):
    f.write('번호:'+str(no)+"\n")
    f.write('내용:'+str(contents2[i])+"\n")
    f.write('태그:'+str(tags2[i])+"\n")
    no+=1
f.close()
print("txt 파일 저장 경로: %s" % f_name)

no= list(range(1,len(contents2)+1))
korea_trip=pd.DataFrame()
korea_trip['번호']=pd.Series(no)
korea_trip['내용']=pd.Series(contents2)
korea_trip['태그']=pd.Series(tags2)
korea_trip.to_csv(fc_name,encoding="utf-8-sig",index=False)
print("csv 파일 저장 경로: %s"% fc_name)

df= pd.read_csv("D:/3th/개발/빅데이터/web_crawling_study/gsm/Data/여름여행_k.csv",index_col=0)
#print(df)
print(df['내용'])
print(df['태그'])