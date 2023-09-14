import sqlite3
import requests
import json
import datetime
conn = sqlite3.connect('mydb.db')
cur = conn.cursor()
cur.execute("SELECT * FROM stocks")
# 커서에서 바로 출력( 커서는 휘발성, 꺼내오면 사라짐)
# for row in cur:
#     print(row)
# fetchone 단건
# one = cur.fetchone()
# print(one)
# many = cur.fetchmany(3) # 3건만 꺼내오기
# print(many)
# 전체
rows = cur.fetchall()
print(rows)
conn.close()
url = "https://api.upbit.com/v1/ticker?markets="
for row in rows:
    print(url + row[0])
    res = requests.get(url + row[0])
    if res.status_code == 200:
        json_data = json.loads(res.text)
        # print(json_data)
        market = json_data[0]['market']
        trade_price = "{:.15f}".format(json_data[0]['trade_price'])
        trade_timestamp = json_data[0]['timestamp'] * 0.001  # 초단위로 변환
        str_timestamp =\
            datetime.datetime.fromtimestamp(trade_timestamp).strftime(
                "%Y-%m-%d %H:%M:%S")
        print(market, trade_price, str_timestamp)