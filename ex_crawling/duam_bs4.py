from bs4 import BeautifulSoup
import requests
url = 'https://movie.daum.net/ranking/boxoffice/weekly'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
# print(soup.prettify())
ol = soup.select_one('.list_movieranking')
lis = ol.select('li')
# /movie_img/영화명.png로 저장하세요
# 폴더생성

# -----------------------------
# 랭킹 기간 23.08.28 ~ 23.09.03
# 230828_230903.csv 파일로 저장
# 영화명|개봉일자(숫자만)|관객수(숫자만)|상세내용url|포스터저장경로
# 형태로 저장하세요
# -----------------------------
import re
text = '2023.07.12'
print(text)
print(re.sub(r'[^0-9]', '', text))


import os
import urllib.request as req
path = "movie_img/"
if not os.path.exists(path):
    os.mkdir(path)
for li in lis:
    print("="*100)
    # print(li)
    title = li.select_one('.link_txt').text.replace(":", "")
    src = li.select_one('img').get('src')
    print(title, src)
    req.urlretrieve(src, path+title+'.png')
print('저장완료')