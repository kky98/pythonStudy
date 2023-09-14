import sqlite3
import requests
import json
url = "https://api.upbit.com/v1/market/all"
sql = """ INSERT INTO stocks
          VALUES(:1, :2, :3)"""
res = requests.get(url)
text = res.text
json_data = json.loads(text)
conn = sqlite3.connect("mydb.db")
cur = conn.cursor()
for row in json_data:
    cur.execute(sql, [ row['market']
                     , row['korean_name']
                     , row['english_name']])
conn.commit()
conn.close()

