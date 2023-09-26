import os

import FinanceDataReader as fdr
import matplotlib.pyplot as plt
#국내 해외 지수 환율정보
# apple =fdr.DataReader('AAPL')
# print(apple.head())
#
# apple['Close'].plot()
# plt.show()

#한국거래소 상장종목
# df_krx =fdr.StockListing('KRX')
# print(df_krx.head())
#
# KOSPI =df_krx[df_krx['Market'].str.contains('KOSPI')]
# print(KOSPI.columns)
# print(KOSPI.head(50))
# df_samsung_2022 =fdr.DataReader('005930','2022')
# df_samsung_2000_2022=fdr.DataReader('005930','2022-01-01','2022-12-31')
#
# print(df_samsung_2000_2022.info())#기본정보
# print(df_samsung_2000_2022.describe())#기초통계량
# df_samsung_2000_2022['Close'].plot()
# plt.show()

import datetime
import matplotlib.font_manager as fm
import pandas as pd

path =os.getcwd()
font_path="../pandas/batang.ttc"
font_nm = fm.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] =font_nm
#오늘 날짜를 기준으로 1달 전의 날짜 계산
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=30)
print(start_date)

# 5개 종목 리스트(삼성, sk하이닉스, 셀트리온, 삼성바이오로직스, lg화학)
stocks = ['005930', '000660', '068270', '207940', '051910']
nm=['삼성','sk하이닉스','셀트리온','삼성바이오로직스','lg화학']
plt.figure(figsize=(12, 6))
for i,stock in enumerate(stocks):
    df = fdr.DataReader(stock, start_date, end_date)
    plt.plot(df['Close'], label=nm[i])
    file_nm='{0}_{1}_{2}.xlsx'.format(nm[i],start_date,end_date)
    writer =pd.ExcelWriter(file_nm,engine='openpyxl')
    df.to_excel(writer,'sheet1')
    writer._save()
    writer.close()
plt.title("Stock Price")
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()  # 범례 표시
plt.grid(True)  # 그리드 표시
plt.tight_layout()  # 레이아웃 조정
plt.savefig('30일.png')  # 파일 저장
plt.show()