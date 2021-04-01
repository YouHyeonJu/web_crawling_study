from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
query_txt="코로나"
f_name="Data/코로나_n.txt"
fc_name="Data/코로나_n.csv"

path = "c:/temp/chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get("https://www.naver.com")
driver.maximize_window()

element=driver.find_element_by_id("query")
element.send_keys(query_txt)
element.submit()