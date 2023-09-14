import sqlite3
# 경량 db, 파일 형태
# 파일로 만들지 않고 일회성으로 사용할때는 :memory:
# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("mydb.db")
print(sqlite3.version)
# sql = """CREATE TABLE stocks (
#              stock_code VARCHAR2(20)
#             ,stock_kr   VARCHAR2(100)
#             ,stock_en   VARCHAR2(100) )
# """
sql = "SELECT * FROM stocks"
cur = conn.cursor()
cur.execute(sql)
row = cur.fetchall()  #전체 조회결과
print(row)
conn.close()
