from bs4 import BeautifulSoup
import requests

url = 'https://www.melon.com/chart/index.htm'
res = requests.get(url)
print(res.status_code)
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.prettify())