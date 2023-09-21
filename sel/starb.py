from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import xlsxwriter
from tkinter import *
import  chromedriver_autoinstaller
import img_util
search_word=""
chromedriver_autoinstaller.install()
url="https://www.starbucks.co.kr/store/store_map.do"


driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/header[2]/h3/a').click()
driver.find_element(By.XPATH,'//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[5]/a').click()
driver.find_element(By.XPATH,'//*[@id="mCSB_2_container"]/ul/li[1]/a').click()
time.sleep(2)
soup = BeautifulSoup(driver.page_source, 'html.parser')
list=soup.select('.quickResultLstCon')

driver.quit()
arr=[]
for li in list :
    dlat=li.get('data-lat')
    dlong=li.get('data-lat')

    name = li.find('strong').text
    name= name.replace(' ','')
    path = li.find('p').text
    path= path.replace(' ','')
    print(path)
    path= path.replace(',','')
    path=path.replace('1522',',1522')

    str=name+','+dlat+','+dlong+','+path
    print(str)
    strarr=str.split(",")

    arr.append(strarr)
print(arr)
workbook =xlsxwriter.Workbook('str.xlsx')
workseet =workbook.add_worksheet()
for row_num,row_data in enumerate(arr):
    for col_num,col_data in enumerate(row_data):
        workseet.write(row_num,col_num,col_data)
workbook.close()
