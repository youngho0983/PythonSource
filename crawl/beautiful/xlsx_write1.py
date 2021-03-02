# 엑셀 파일로 저장하는 함수

from openpyxl import Workbook


def write_excel_template(filename, sheetname, listdata):
    # 객체 생성
    excel_file = Workbook()

    excel_sheet = excel_file.active

    excel_sheet.column_dimensions["A"].width = 60

    if excel_sheet.title != "":
        excel_sheet.title = sheetname

    for row in listdata:
        excel_sheet.append(row)

    excel_file.save("./crawl/data/" + filename)

    # 엑셀 파일 닫기

    excel_file.close()


if __name__ == "__main__":
    listdata = [
        ["name", "생년월일"],
        ["홍길동", "801020"],
        ["송혜교", "851115"],
        ["김지원", "860912"],
        ["남주혁", "880705"],
    ]
    write_excel_template("info.xlsx", "정보", listdata)
