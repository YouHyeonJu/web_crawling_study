from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

query_txt="미와야키 사쿠라"
f_name="C:/Users/hs46h/OneDrive/바탕 화면/동생/web_crawling_study/gsm/벅.txt"
fc_name="C:/Users/hs46h/OneDrive/바탕 화면/동생/web_crawling_study/gsm/벅.txt"
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

content_list=soup.find("ul",class_="list_news").find_all("li")

for i in content_list:
    try:
        content=i.find("a","news_tit").get_text()
        content_l.append(content)
        print("제목: ",content)
        print("\n")
    except:
        pass
    try:
        title=i.find("div","dsc_wrap").get_text()
        title_l.append(title)
        print("내용: ",title)
        print("\n")
    except:
        pass
f=open(f_name,'w',encoding="utf-8-sig")
for i in range(0,len(content_l)):
    f.write("번호: "+str(no)+"\n")
    f.write("제목: "+str(content_l[i])+"\n")
    f.write("내용: "+str(title_l[i])+"\n")
    no+=1

f.close()
no =list(range(1,len(content_l)+1))
good=pd.DataFrame()
good["번호: "]=pd.Series(no)
good["제목: "]=pd.Series(content_l)
good["내용: "]=pd.Series(title_l)
good.to_csv(fc_name,encoding="utf-8-sig",index=False)
df=pd.read_csv(fc_name,index_col=0)
print(df)