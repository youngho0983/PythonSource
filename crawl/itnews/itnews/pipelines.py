# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import datetime
import time
from scrapy.exceptions import DropItem


class ItnewsPipeline:
    # 초기화 메소드
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="biguser1",
            password="12345",
            db="bigdata",
            charset="utf8",
        )
        if self.conn:
            print("conntection 성공")
        else:
            print("실패")
        self.cursor = self.conn.cursor()

    # 아이템별
    def process_item(self, item, spider):
        if not item["content"] is None:
            # 크롤링 시간 필드 추가
            item["crawled_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            sql = """
                insert into news_data(headline,contents,parent_link,article_link,crawled_time)
                values(%s,%s,%s,%s,%s)
            """
            values = (
                item["title"],
                item["content"],
                item["parent_link"],
                item["article_link"],
                item["crawled_time"],
            )

            self.cursor.execute(sql, values)
            self.conn.commit()

            spider.logger.info("Item DB inserted")
            return item
        else:
            raise DropItem("Drop Item")

    # 최초 1회 실행
    def open_spider(self, spider):
        spider.logger.info("NewSpider Pipeline  Started")
        sql = """
        Create table If not Exists news_data(
        id int primary key Auto_increment,
        headline varchar(100),
        contents varchar(2000),
        parent_link varchar(100),
        article_link varchar(100),
        crawled_time varchar(50)
        )
        """

        self.cursor.execute(sql)

    # 마지막 1회 실행
    def close_spider(self, spider):
        self.conn.close