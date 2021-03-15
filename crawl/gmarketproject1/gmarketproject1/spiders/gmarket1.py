import scrapy


class Gmarket1Spider(scrapy.Spider):
    name = "gmarket1"
    allowed_domains = ["http://corners.gmarket.co.kr/Bestsellers"]
    start_urls = ["http://corners.gmarket.co.kr/Bestsellers/"]

    def parse(self, response):
        product_names = response.css("div.best-list ul:not(.plus) li a::text").getall()
        product_prices = response.css(
            "div.best-list ul:not(.plus) > li > div.item_price > div.s-price > strong > span > span::text"
        ).getall()
        for idx, product in enumerate(product_names):
            print(product)
            print(product_prices[idx])
