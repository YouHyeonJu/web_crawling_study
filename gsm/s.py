from bs4 import BeautifulSoup
from selenium import webdriver
import time

query_txt="봄여행"
path="C:\Temp\chromedriver.exe"
driver= webdriver.Chrome(path)
driver.get("https://korean.visitkorea.or.kr")
driver.maximize_window()
time.sleep(2)
try:
    driver.find_element_by_xpath('//*[@id="safetyStay1"]/div[1]/div/div/button').click()
except:
    print('')
element = driver.find_element_by_id("inp_search")
element.send_keys(query_txt)

# 3가지 방법
# element.send_keys("\n") 엔터
# driver.find_element_by_link_text("검색").click() 텍스트보고 입력
driver.find_element_by_class_name("btn_search").click()

full_html= driver.page_source

soup = BeautifulSoup(full_html,'html.parser')

content_list=soup.select('ul[class="list_thumType type1"] > li')

for i in content_list:
    print(i.get_text())
    print("\n")
f=open("Data/봄여행_korea.txt","w", encoding="UTF-8")
for i in content_list:
    f.write(i.text.strip())
    f.write("\n")
f.close()