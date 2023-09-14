# pip install xlsxwriter
# 엑셀 생성 라이브러리
import xlsxwriter
ex_data = [[1, 2, 3]
         , [4, 5, 6]
         , [7, 8, 9]]
# 새 엑셀 파일과 워크 시트 생성
workbook = xlsxwriter.Workbook("test.xlsx")
worksheet = workbook.add_worksheet()
# 엑셀에 작성
for row_num, row_data in enumerate(ex_data):
    for col_num, col_data in enumerate(row_data):
        worksheet.write(row_num, col_num, col_data)
# 저장 후 닫기
workbook.close()