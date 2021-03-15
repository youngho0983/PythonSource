import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["www.naver.com", "www.daum.net", "www.zyte.com/blog/"]
    start_urls = [
        "https://www.naver.com/",
        "https://www.daum.net",
        "https://www.zyte.com/blog/",
    ]

    def parse(self, response):
        print(response.css("head title::text").get())
