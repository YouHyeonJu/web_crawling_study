from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
query_txt="빅데이터"
f_name="C:/Users/hs46h/OneDrive/바탕 화면/동생/web_crawling_study/gsm/긁.txt"
fc_name="C:/Users/hs46h/OneDrive/바탕 화면/동생/web_crawling_study/gsm/긁.csv"
path="C:/Temp/chromedriver.exe"
driver= webdriver.Chrome(path)

driver.get("https://www.naver.com/")
time.sleep(2)
driver.maximize_window()

element= driver.find_element_by_id("query")
element.send_keys(query_txt)
element.submit()

driver.find_element_by_link_text("뉴스").click()

number=[]
title_l=[]
sinmoon_l=[]
intitle_l=[]
no=1

html=driver.page_source
soup=BeautifulSoup(html,"html.parser")

content_list=soup.find('ul',class_='list_news').find_all('li')


for i in content_list:
    try:
        sinmoon=i.find("a","info press").get_text()
        sinmoon_l.append(sinmoon)
        print('언론사: ',sinmoon)
        print('\n')
    except:
        pass
    try:
        title=i.find("a","news_tit").get_text()
        title_l.append(title)
        print('제목: ',title)
        print('\n')
    except:
        pass
    try:
        intitle=i.find("div","news_dsc").get_text()
        intitle_l.append(intitle)
        print('내용: ',intitle)
        print('\n')
    except:
        pass
f=open(f_name,'w',encoding='UTF-8')
for i in range(0,len(title_l)):
    f.write('번호: '+str(no)+"\n")
    f.write('언론사: '+str(sinmoon_l[i])+"\n")
    f.write('제목: '+str(title_l[i])+"\n")
    f.write('내용: '+str(intitle_l[i])+"\n")
    no+=1
f.close()

no=list(range(1,len(title_l)+1))
bigdatas=pd.DataFrame()
bigdatas['번호']=pd.Series(no)
bigdatas['언론사']=pd.Series(sinmoon_l)
bigdatas['제목']=pd.Series(title_l)
bigdatas['내용']=pd.Series(intitle_l)
bigdatas.to_csv(fc_name,encoding="utf-8-sig",index=False)
df=pd.read_csv(fc_name,index_col=0)
print(df)

