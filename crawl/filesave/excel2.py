from openpyxl import Workbook


excel_file =Workbook()

print(excel_file.sheetnames)

excel_file.save(r"./crawl/data/text1.xlsx")