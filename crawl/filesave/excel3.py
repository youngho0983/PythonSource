from openpyxl import Workbook


excel_file =Workbook()
excel_file.remove(excel_file["Sheet"])

sheet1=excel_file.create_chartsheet(index=0,title="Column")

sheet2=excel_file.create_chartsheet(index=1,title="매출표")

print(excel_file.sheetnames)

excel_file.save(r"./crawl/data/text2.xlsx")