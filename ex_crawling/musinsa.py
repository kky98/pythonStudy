from bs4 import BeautifulSoup
import requests
import csv
import re

def fn_get_musinsa(page):
    url ='https://www.musinsa.com/mz/community?p=' + str(page)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    uls = soup.find('ul', class_='ul-col')
    lis = uls.find_all('li')
    arr = []
    for i, li in enumerate(lis):
        if i > 1:
            cate = li.find('span', class_='colName').text
            date = li.find('span', class_='colDate').text
            hit = li.find('span', class_='colHit').text
            href = li.find('span'
                           , class_='colSbj-cate').find_all('a')[1]['href']
            title = li.find('span'
                            , class_='colSbj-cate').find_all('a')[1].text
            arr.append([cate, date, hit, href, title])
    return arr
if __name__ == '__main__':
    print(fn_get_musinsa(1))