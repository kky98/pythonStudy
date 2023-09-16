html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie&quot; class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie&quot; class="sister" id="link2" /> and
<a href="http://example.com/tillie&quot; class="sister">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
# find : 1개의 태그만 찾음
# find_all :모든 태그를 찾음
# select_one : 1개의 태그만 찾음
# select : 모든 태그를 찾음
a_tag = soup.a  # 첫번째 a태그
print(a_tag.name)         # 태그 명
print(a_tag.text)         # 태그 하위에 있는 모든 텍스트
print(a_tag['href'])      # 속성 명으로 접근
print(a_tag.get('href'))  # 위와 동일함.
print(a_tag.get('id'))

text_a = soup.find_all('a', string=True) # text가 있는 a태그만
print(text_a)
import re  # <-- 정규표현식 사용 라이브러리
a_l = soup.find_all('a', string=re.compile('l')) # l<-- 이 존재하는
a_e = soup.find_all('a', string=['Elsie'])
print(a_l, a_e)
a_tags = soup.find_all('a')
for a in a_tags:
    print(a.get('href'))