from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
query_txt="빅데이터"
f_name="D:/3th/개발/빅데이터/web_crawling_study/gsm/Data2/슥.txt"
fc_name="D:/3th/개발/빅데이터/web_crawling_study/gsm/Data2/슥.csv"
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
content_l=[]
no=1

html=driver.page_source
soup=BeautifulSoup(html,"html.parser")

all_list=soup.find("ul","list_news").find_all('li')

for i in all_list:
    try:
        title=i.find('a','news_tit').get_text()
        title_l.append(title)
        print('\n')
    except:
        pass
    try:
        content=i.find('div','dsc_wrap').get_text()
        content_l.append(content)
        print('\n')
    except:
        pass

f=open(f_name,'w',encoding="utf-8")
for i in range(0,len(title_l)):
    f.write("번호: "+str(no)+"\n")
    f.write("제목: "+str(title_l[i])+"\n")
    f.write("내용: "+str(content_l[i])+"\n")
    no+=1

f.close()
no=list(range(1,len(title_l)+1))
big=pd.DataFrame()
big['번호']=pd.Series(no)
big['제목']=pd.Series(title_l)
big['내용']=pd.Series(content_l)
big.to_csv(fc_name,encoding='utf-8-sig',index=False)
df=pd.read_csv(fc_name,index_col=0)
print(df)
