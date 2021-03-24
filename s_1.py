from bs4 import BeautifulSoup
from selenium import webdriver
import time

query_txt="봄여행"
path="C:\Temp\chromedriver.exe"
driver= webdriver.Chrome(path)
driver.get("https://www.naver.com/")
driver.maximize_window()
time.sleep(2)

element = driver.find_element_by_id("query")
element.send_keys(query_txt)

# 3가지 방법
# element.send_keys("\n") 엔터
# driver.find_element_by_link_text("검색").click() 텍스트보고 입력
driver.find_element_by_class_name("ico_search_submit").click()

time.sleep(3)
driver.find_element_by_link_text("뉴스").click()

full_html= driver.page_source

soup = BeautifulSoup(full_html,'html.parser')

content_list=soup.select('ul[class="list_news"] > li')


f=open("Data/네이버_뉴스_봄여행.txt","w", encoding="UTF-8")
for i in content_list:
    # title= i.find('a','api_txt_lines total_tit').get_text()
    # f.write(title+"\n")
    # f.write("\n")


    try:
        contents_1 = i.find('div', 'dsc_wrap').get_text()
        f.write(contents_1 + "\n")
        f.write("\n")
        print(contents_1 + "\n")
    except:
        pass

    # f.write("\n")
    # f.write(i.text.strip())
    # f.write("\n")
f.close()