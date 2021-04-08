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