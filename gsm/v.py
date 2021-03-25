from bs4 import BeautifulSoup
from selenium import webdriver
import time

query_txt = "인공지능"
f_name = "Data/인공지능1.txt"

path = "C:\Temp\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.naver.com/")
driver.maximize_window()

element = driver.find_element_by_id("query")
element.send_keys(query_txt)
element.send_keys("\n")

driver.find_element_by_link_text("뉴스").click()

full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')

news_list = soup.find('ul', 'list_news').find_all('li')

with open(f_name, 'w', encoding='UTF-8') as f:
    for news in news_list:
        try:
            title = news.find('a', 'news_tit').get_text()
            f.write(title)
            f.write('\n')
        except:
            pass

        try:
            text = news.find('div', 'news_dsc').get_text()
            f.write(text)
            f.write('\n')
        except:
            pass