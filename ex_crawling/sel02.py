from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Edge('./msedgedriver.exe')
driver.implicitly_wait(3)  # 브라우저 켜질때까지 기다리기
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.prettify())