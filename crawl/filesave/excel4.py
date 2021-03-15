from openpyxl import Workbook


excel_file =Workbook()

#기본 시트 활성화
sheet1=excel_file.active

# 데이터 저장하기
rows = [['name','생년월일'],['홍길동','801020'],['송혜교','851115'],['김지원','860912'],["남주혁","880705"]]

for row in rows:
    sheet1.append(row)

excel_file.save(r"./crawl/data/text3.xlsx")