import scrapy


class Computer1Spider(scrapy.Spider):
    name = "computer1"
    allowed_domains = ["www.computerworld.com"]
    start_urls = ["http://www.computerworld.com/"]

    def parse(self, response):
        print("hello")
