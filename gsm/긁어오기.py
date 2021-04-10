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
print(content_list)

for i in content_list:
    try:
        sinmoon=i.find("div","info_group")
        sinmoon_l.append(sinmoon)
        print('언론사: ',title)
        print('\n')
    except:
        pass
    try:
        title=i.find("a","news_tit")
        title_l.append(title)
        print('제목: ',title)
        print('\n')
    except:
        pass
    try:
        intitle=i.find("div","news_dsc")
        intitle_l.append(intitle)
        print('내용: ',intitle)
        print('\n')
    except:
        pass
f=open(f_name,'w',encoding='UTF-8')
for i in range(0,len(title_l)):
    f.write('번호',str(no),"\n")
    f.write('언론사',str(sinmoon),"\n")
    f.write('제목',str(title),"\n")
    f.write('내용',str(intitle),"\n")
    no+=1
f.close()
