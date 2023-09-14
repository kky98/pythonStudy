import matplotlib.pyplot as plt
import pandas as pd
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
# pip install wordcloud
# pip install konlpy #한국어 자연어 처리 관련 라이브러리
okt = Okt()
test = '안녕하세요 저는 팽수 입니다. 만나서 방가 방가'
parser_data = okt.pos(test)
words = ['팽수','동길','팽수','길수']
cnt_word = Counter(words)
print(cnt_word)
import pandas as pd
from ex_db.DBManager import DBManager
param = input("워드클라우드를 보고싶은 종목코드:")
mydb = DBManager()
sql = """SELECT * FROM tb_stock_bbs WHERE item_code =:1 """
df = pd.read_sql(con=mydb.conn, sql=sql, params=[param])
print(df.head())
nouns = []
for idx, row in df.iterrows():
    if row['BBS_CONTENTS']:
        nouns +=okt.nouns(row['BBS_CONTENTS'])
count = Counter(nouns)

wc = WordCloud(background_color='white', width=400, height=400
               , scale=2.0, max_font_size=250
               , font_path='NanumGothicBold.ttf')
gen = wc.generate_from_frequencies(count)
import matplotlib.pyplot as plt
# pip install matplotlib
plt.figure(param)
plt.imshow(gen)
plt.show()
print(count)

