import scrapy
from ..items import AlexaprojectItem


class AlexaspiderSpider(scrapy.Spider):
    name = "alexaspider"
    allowed_domains = ["alexa.com"]
    start_urls = ["http://alexa.com/topsites"]

    def parse(self, response):
        # url = response.css(
        #     "#post-1660 > div > div.fusion-fullwidth.fullwidth-box.fusion-builder-row-13.nonhundred-percent-fullwidth.non-hundred-percent-height-scrolling.fusion-equal-height-columns > div > div.fusion-layout-column.fusion_builder_column.fusion-builder-column-48.fusion_builder_column_1_3.\31 _3.fusion-one-third.fusion-column-last > div > div.fusion-title.title.fusion-title-17.fusion-sep-none.fusion-title-center.fusion-title-text.fusion-title-size-three.dark-text.link-line-dark.fusion-border-below-title > h3 > p > a::attr('href')"
        # ).get()
        # yield scrapy.Request(response.urljoin(url), self.parse_next)

        for site in response.css("div.listings > div.site-listing"):
            item = AlexaprojectItem()
            item["rank"] = site.css("div.td::text").get()
            item["name"] = site.css("div.DescriptionCell> p>a::text").get()
            item["useTime"] = site.css("div:nth-child(3)>p::text").get()
            item["viewNum"] = site.css("div:nth-child(4)>p::text").get()
            yield item
