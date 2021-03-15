import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class News1Spider(CrawlSpider):
    name = "news1"
    allowed_domains = ["news.daum.net"]
    start_urls = ["http://news.daum.net/breakingnews/digital"]
    # LinkExtractor : 링크 추출식
    rules = [
        Rule(
            LinkExtractor(allow=r"breakingnews/digital\?page=\d$"),
            callback="parse_headline",
            follow=True,
        )
    ]

    def parse_start_url(self, response):
        # self.logger.info("parse_start_url {}".format(response.url))
        return self.parse_headline(response)

    def parse_headline(self, response):
        # self.logger.info("parse_headline {}".format(response.url))
        news = response.css("#mArticle > div.box_etc > ul>li")
        for new in news:
            title = new.css("div >strong > a::text").get()
            content = new.css("div > div> span::text").get()

            print(title)
            print(content)

    # def parse(self, response):
    #     pass
