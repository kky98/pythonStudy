from selenium import webdriver
import urllib.request
from selenium.webdriver.common.by import By
import time
import os

url = "https://www.google.com/search?q="
img_dir = "./dataset/"
if not os.path.exists(img_dir):
    os.mkdir(img_dir)


def get_image(query, dir):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(3)
    driver.get(url + query)
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
    #해당페이지 가장 하단까지
    scroll_height = driver.execute_script('return document.body.scrollHeight')
    print(scroll_height)
    while True:
        driver.execute_script(f'window.scrollTo(0,{scroll_height})')
        time.sleep(1)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if scroll_height == new_height:
            btn = driver.find_element(By.CLASS_NAME, 'LZ4I')
            if btn:
                try:
                    btn.click()
                except Exception as e:
                    break

            else:
                break
        else:
            scroll_height = new_height

    img = driver.find_elements(By.TAG_NAME,'img')
    img_arr=set()
    for v in img:
        if v:
            if v.get_attribute('src') !=None:
                img_arr.add(v.get_attribute('src'))
    print("여기")
    print(img_arr)
    driver.close()
    for idx, img_data in enumerate(img_arr):
        urllib.request.urlretrieve(img_data, dir + "/" + query + "_" + str(idx) + ".png")

keyword =["돌고래","향유고래","고래상어","쿠로미","헬로키티","한교동"]
for k in keyword:
    if not os.path.exists(img_dir+k):
        os.mkdir(img_dir+k)
    #수집시작
    get_image(k,img_dir+k)