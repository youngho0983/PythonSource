import scrapy


class TestSpider(scrapy.Spider):
    name = "test2"
    allowed_domains = ["www.naver.com", "www.daum.net", "www.zyte.com"]
    start_urls = [
        "https://www.naver.com/",
        "https://www.daum.net",
        "https://www.zyte.com/blog/",
    ]

    def parse(self, response):
        yield scrapy.Request(response.url, self.parse_title)

    def parse_title(self, response):
        print(response.css("head title::text").get())
