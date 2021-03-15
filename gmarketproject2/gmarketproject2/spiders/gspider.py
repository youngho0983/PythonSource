import scrapy
from ..items import Gmarketproject2Item


class GspiderSpider(scrapy.Spider):
    name = "gspider"
    allowed_domains = ["corners.gmarket.co.kr/Bestsellers"]
    start_urls = ["http://corners.gmarket.co.kr/Bestsellers/"]

    def parse(self, response):
        product_names = response.css(
            "div.best-list ul:not(.plus) >li >a::text"
        ).getall()

        product_prices = response.css(
            "div.best-list > ul:not(.plus) > li div.s-price strong span span::text"
        ).getall()

        for idx, product in enumerate(product_names, 0):
            item = Gmarketproject2Item()
            item["title"] = product
            item["price"] = int(product_prices[idx].replace("원", "").replace(",", ""))
            yield item