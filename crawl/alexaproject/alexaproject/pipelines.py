# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl


class AlexaprojectPipeline:
    # def process_item(self, item, spider):
    #     if int(item["rank"]) <= 40:
    #         return item
    #     else:
    #         raise DropItem("사십위 밖")

    # 초기화 메소드

    def __init__(self):
        # 엑셀 처리
        self.workbook = openpyxl.Workbook()
        self.worksheet = self.workbook.active
        # 너비 조절
        self.worksheet.column_dimensions["A"].width = 10
        self.worksheet.column_dimensions["B"].width = 15
        self.worksheet.column_dimensions["C"].width = 15
        self.worksheet.column_dimensions["D"].width = 20

    def process_item(self, item, spider):
        if int(item["rank"]) < 41:
            return item
        else:
            raise DropItem("40위 이상임")

    def close_spider(self, spider):
        self.workbook.save("./result.xlsx")
        self.workbook.close()