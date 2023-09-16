from bs4 import BeautifulSoup
import requests
import csv
import re

url ='https://www.musinsa.com/mz/community?p=1'
res = requests.get(url)
# print(res.content)
soup = BeautifulSoup(res.content, 'html.parser')
# print("="* 100)
# print(soup.prettify()) # 구조화되게 출력
uls = soup.find('ul', class_='ul-col')
lis = uls.find_all('li')
arr = []
for i, li in enumerate(lis):
    if i > 1:
        # print(li)
        cate = li.find('span', class_='colName').text
        date = li.find('span', class_='colDate').text
        hit = li.find('span', class_='colHit').text
        href = li.find('span'
                       , class_='colSbj-cate').find_all('a')[1]['href']
        title = li.find('span'
                        , class_='colSbj-cate').find_all('a')[1].text
        # print(cate, date, hit, href, title)
        arr.append([cate, date, hit, href, re.sub(r'&nbsp;', "", title)])
        # print(title)
        # print(re.sub(r'&nbsp;', "", title))


with open('musinsa.csv', 'w', encoding='utf-8') as f:
    write = csv.writer(f, delimiter='|')
    write.writerows(arr)
    # for d in arr:
    #     write.writerow(d)
