import scrapy


class ZyteSpider(scrapy.Spider):
    name = "zyte"
    allowed_domains = ["www.zyte.com/blog"]
    start_urls = ["https://www.zyte.com/blog/"]

    def parse(self, response):
        # print(response.text)
        # print("body: {}".format(response.body))
        # print("response.url : {}".format(response.url))
        # print("dir : {}".format(dir(response.url)))
        # print("status : {}".format(response.status))
        print(response.css("body::text").get())