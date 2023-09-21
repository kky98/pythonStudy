from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from tkinter import *
import  chromedriver_autoinstaller
import img_util
search_word=""
chromedriver_autoinstaller.install()
url="https://seil.hanatour.com/package/international"
def fn_search_tour():
    print('tour search')
    search_word = word_entry.get()
    driver=webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get(url)
    time.sleep(1)
    input_search= driver.find_element(By.ID,'input_keyword')
    input_search.send_keys(search_word)
    time.sleep(2)
    btn=driver.find_element(By.CSS_SELECTOR,'button.btn_search').click()
    driver.find_element(By.XPATH,'//*[@id="contents"]/div[3]/div[1]/div[1]/a').click()
    time.sleep(2)
    soup =BeautifulSoup(driver.page_source,'html.parser')
    lis = soup.select('.prod_list li')
    driver.get_screenshot_as_file('tour.png')
    img_util.fullpage_screenshot(driver,'tour_all.png')

    for li in lis:
        info=li.select_one('.txt_info').text
        text.insert(END,info+'\n')
    driver.quit()
app=Tk()
app.title("tour search")
word_entry= Entry(app,width=100)
word_entry.pack()
search_btn=Button(app,text='search & save',command=fn_search_tour)
search_btn.pack()
text=Text(app,width=100,height=50)
text.pack()
app.mainloop()