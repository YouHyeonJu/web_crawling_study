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
driver.find_element_by_link_text("나의 수강현황").click()
webdriver.ActionChains(driver).move_to_element(ref)