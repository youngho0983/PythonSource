import scrapy


class TestSpider(scrapy.Spider):
    name = "test3"
    # allowed_domains = ["www.naver.com", "www.daum.net", "www.zyte.com"]
    # start_urls = [
    #     "https://www.naver.com/",
    #     "https://www.daum.net",
    #     "https://www.zyte.com/blog/",
    # ]
    def start_requests(self):
        yield scrapy.Request("https://www.naver.com/", self.parse)
        yield scrapy.Request("https://www.daum.net", self.parse)
        yield scrapy.Request("https://www.zyte.com/blog/", self.parse)

    def parse(self, response):
        # print(response.url)
        self.logger.info("Response URL : {} ".format(response.url))
        self.logger.info("Response Status : {} ".format(response.status))

        if response.url.find("zyte"):
            yield {"sitemap": response.url, "content": response.text[:1000]}
        elif response.url.find("naver"):
            yield {"sitemap": response.url, "content": response.text[:1000]}
        elif response.url.find("daum"):
            yield {"sitemap": response.url, "content": response.text[:1000]}
