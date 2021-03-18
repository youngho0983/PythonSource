# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class GmarketbestPipeline:
    def __init__(self):
        print("으앙")
        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="biguser1",
            password="12345",
            database="bigdata",
            charset="utf8",
        )
        if self.conn:
            print("Connection 성공")
        else:
            print("Connection 실패")
        self.cursor = self.conn.cursor()

    def open_spider(self, spider):
        spider.logger.info("GmarketBest Pipeline Started")
        print("      ")
        print("      ")
        print("      ")
        print("      ")
        print("      ")
        print("      ")
        print("      ")
        print("      ")
        print("      ")
        print("      ")
        print("      ")
        print("      ")
        print("      ")
        print("      ")
        sql = """
            Create table if not exists product(
                item_code varchar(20) not null primary key,
                title varchar(200) not null,
                ori_price int not null,
                dis_price int not null,
                discount_percent int not null
            )
        """
        self.cursor.execute(sql)

        sql = """
            create table if not exists ranking(
                num int auto_increment not null primary key,
                main_category varchar(80) not null,
                sub_category varchar(80) not null,
                item_ranking tinyint unsigned not null,
                item_code varchar(20) not null
            )
        """

        self.cursor.execute(sql)

    def process_item(self, item, spider):
        sql = """
            insert into product(item_code , title , ori_price ,dis_price,discount_percent)
            values(%s,%s,%s,%s,%s) 
        
        """
        values = (
            item.get("item_code"),
            item.get("item"),
            item.get("price"),
            item.get("sale_price"),
            int(item.get("sale_rate")),
        )

        self.cursor.execute(sql, values)

        sql = """
        insert into ranking(main_category,sub_category,item_ranking,item_code)
        values(%s,%s,%s,%s)
        """

        values = (
            item.get("main_cate"),
            item.get("sub_cate"),
            item.get("ranking"),
            item.get("item_code"),
        )
        self.cursor.execute(sql, values)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        spider.logger.info("GmarketBest Pipelines Stopped")
        self.conn.close()