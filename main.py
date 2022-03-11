from openpyxl import load_workbook
from openpyxl import Workbook

# 엑셀파일 쓰기
write_wb = Workbook()
# 이름이 있는 시트를 생성
write_ws = write_wb.create_sheet('생성시트')
write_wb.save("/Users/jinjoolee/Desktop/Project/python/sample.xlsx")

# 입력 자리를 지정
write_ws.cell(1,1,'연습해보자')


write_wb.save("/Users/jinjoolee/Desktop/Project/python/sample.xlsx")


# 과제: 최소 20개 컬럼에 대해서 최소 10000개 로우를 가져와서 합치기 응용하기!
# 다음주 수요일에 1차 피드백, 그 다음 월요일 수업