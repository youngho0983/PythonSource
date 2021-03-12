# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GmarketbestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sale_price = scrapy.Field()
    item = scrapy.Field()
    price = scrapy.Field()
    sale_rate = scrapy.Field()
    item_code = scrapy.Field()
    main_cate = scrapy.Field()
    sub_cate = scrapy.Field()
    ranking = scrapy.Field()
