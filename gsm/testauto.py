from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
query_txt="빅데이터"
f_name="C:/Users/hs46h/OneDrive/바탕 화면/동생/web_crawling_study/gsm/긁.txt"
fc_name="C:/Users/hs46h/OneDrive/바탕 화면/동생/web_crawling_study/gsm/긁.csv"
path="C:/Temp/chromedriver.exe"
driver= webdriver.Chrome(path)

LOGIN_INFO = {
    'userId': 'gsm2130415',
    'userPassword': 'gsm2130415'
}
driver.get("https://youth.keli.kr/MainYouth_indexMain.do")
time.sleep(2)
driver.maximize_window()

log_id= driver.find_element_by_id("log_id")
log_id.send_keys(LOGIN_INFO['userId'])
print(LOGIN_INFO['userId'])
pwd= driver.find_element_by_id("log_pwd")
pwd.send_keys(LOGIN_INFO['userPassword'])
print(LOGIN_INFO['userPassword'])
# pwd.submit()
driver.find_element_by_link_text("로그인").click()
driver.find_element_by_link_text("마이페이지").click()

driver.find_element_by_link_text("강의듣기").click()
html=driver.page_source
soup = BeautifulSoup(html, 'html.parser')
gag=driver.find_element_by_link_text("학습하기").text
print(gag)
print(type(gag))
while gag=="학습하기":
    print("1")
    gag=driver.find_element_by_link_text("학습하기").text
    driver.find_element_by_link_text("학습하기").click()
    time.sleep(10)
    driver.find_element_by_link_text("x2.0").click()
    while driver.find_element_by_link_text("수고하셨습니다.").text!="수고하셨습니다.":
        if driver.find_element_by_link_text("다음페이지로 이동하세요.").text=="다음페이지로 이동하세요.":
            driver.find_element_by_link_text("다음페이지로 이동하세요.").click()
    


