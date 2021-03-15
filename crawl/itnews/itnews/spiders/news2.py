import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ItnewsItem


class News1Spider(CrawlSpider):
    name = "news2"
    allowed_domains = ["news.daum.net"]
    start_urls = ["http://news.daum.net/breakingnews/digital"]
    # LinkExtractor : 링크 추출식
    rules = [
        Rule(
            LinkExtractor(allow=r"breakingnews/digital\?page=\d$"),
            callback="parse_parent",
            follow=True,
        )
    ]

    def parse_start_url(self, response):
        # self.logger.info("parse_start_url {}".format(response.url))
        return self.parse_parent(response)

    def parse_parent(self, response):
        self.logger.info("parse_parent {}".format(response.url))

        # 링크 추출
        links = response.css(
            "#mArticle > div.box_etc > ul > li > a::attr('href')"
        ).getall()
        for link in links:

            # yield {"article_url": link}
            yield scrapy.Request(
                link,
                self.parse_child,
                meta={"parent_link": response.url},
                dont_filter=True,
            )

    def parse_child(self, response):
        self.logger.info(
            "Response From Parent URL {}".format(response.meta["parent_link"])
        )
        self.logger.info("Child URL {} ".format(response))

        parent_link = response.meta["parent_link"]

        title = response.css("#cSub > div > h3::text").get()
        article_link = response.url

        content = ""
        contents = response.css("#harmonyContainer > section>p::text").getall()
        for cont in contents:
            content += cont.strip()

        item = ItnewsItem()
        item["parent_link"] = parent_link
        item["title"] = title
        item["article_link"] = article_link
        item["content"] = content

        yield item
        # 상세 기사에서 아이템에 담기

    # def parse(self, response):
    #     pass
