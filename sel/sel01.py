from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

driver=webdriver.Edge('./msedgedriver.exe')
driver.implicitly_wait(3)
time.sleep(2)
url='https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%ED%96%84%EB%B2%84%EA%B1%B0'

driver.get(url)
time.sleep(1)
cnt=3
pagedown =1
body =driver.find_element(By.TAG_NAME,'body')
while pagedown<cnt:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    pagedown+=1
res=requests.get(url)
soup= BeautifulSoup(res.content,'html.parser')
#print(soup.prettify())
#main=soup.find('div', class_='photo_tile _grid')
main=soup.find('div', class_='thumb')
timg=main.find_all('img')
print(timg)
for i, img in enumerate(timg):
    src = img['src']
    print(src)