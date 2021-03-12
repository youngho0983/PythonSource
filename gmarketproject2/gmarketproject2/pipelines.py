# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class Gmarketproject2Pipeline:
    def process_item(self, item, spider):
        # return item
        # print("pipeline", item)
        if int(item["price"]) > 10000:
            return item
        else:
            raise DropItem("가격이 10,000 보다 적음")
