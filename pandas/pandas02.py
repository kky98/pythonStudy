import pandas as pd
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud


okt =Okt()
test ='안녕하세요 저는 팽수 입니다. 방가방가'
parser_data =okt.pos(test)
words=['팽수','동길','팽수','길수']
cnt_word=Counter(words)
print(cnt_word)
import pandas as pd
from base.ex_db.DBManager import DBManager
param= input("워드클라우드 보고싶은 종목 코드")
mydb=DBManager()
sql ="""SELECT * FROM tb_stock_bbs WHERE item_code=:1"""

df = pd.read_sql(con=mydb.conn,sql=sql,params=[param])
print(df.head())
nouns =[]
for idx,row in df.iterrows():
    if row['BBS_CONTENTS']:
        nouns+=okt.nouns(row['BBS_CONTENTS'])
count= Counter(nouns)

wc=WordCloud(background_color='white',width=400,height=400,scale=2.0, max_font_size=250,font_path='batang.ttc')
gen=wc.generate_from_frequencies(count)
import matplotlib.pyplot as plt
plt.figure("토론방")
plt.imshow(gen)
plt.show()
print(count)
print(nouns)

