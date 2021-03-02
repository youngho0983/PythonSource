from openpyxl import Workbook
from openpyxl.drawing.image import Image

excel_file =Workbook()

#기본 시트 활성화
sheet1=excel_file.active

# 데이터 저장하기
rows = [['name','생년월일'],['홍길동','801020'],['송혜교','851115'],['김지원','860912'],["남주혁","880705"]]

for idx,row in enumerate(rows,2):
    img=Image("./crawl/data/cat.png")
    img.width=30
    img.height=20
    sheet1.append(row)
    sheet1.add_image(img,'C'+str(idx))

excel_file.save(r"./crawl/data/text4.xlsx")