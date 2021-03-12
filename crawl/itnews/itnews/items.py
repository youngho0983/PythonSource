# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItnewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    parent_link = scrapy.Field()

    title = scrapy.Field()

    article_link = scrapy.Field()

    content = scrapy.Field()

    crawled_time = scrapy.Field()
