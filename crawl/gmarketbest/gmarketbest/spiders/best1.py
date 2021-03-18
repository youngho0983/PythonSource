import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import GmarketbestItem
import re


class Best1Spider(CrawlSpider):
    name = "best1"
    allowed_domains = ["corners.gmarket.co.kr"]
    start_urls = ["http://corners.gmarket.co.kr/Bestsellers/"]

    rules = [
        Rule(
            LinkExtractor(allow=r"Bestsellers\?viewType=G&groupCode=G(0|1)\d$"),
            callback="parse_sub_category",
        )
    ]

    def parse_start_url(self, response):
        print(">>> parse_start_url", response.url)

        # yield scrapy.Request(
        #     response.url, self.parse_item, meta={"main_cate": "ALL", "sub_cate": "ALL"}
        # )

    def parse_sub_category(self, response):
        print(">>> parse_sub_category", response.url)

        main_cate = response.css("div.gbest-cate ul li.on a::text").get()
        # print("{} {}".format(main_cate, response.url))

        yield scrapy.Request(
            response.url,
            self.parse_item,
            meta={"main_cate": main_cate, "sub_cate": main_cate},
            dont_filter=True,
        )

        sub_cate_addr = response.css(
            "div.navi ul li[class!='related'] a::attr('href')"
        ).getall()
        sub_cate_name = response.css(
            "div.navi ul li[class!='related'] a::text"
        ).getall()
        for idx, sub_addr in enumerate(sub_cate_addr):
            sub_url = response.urljoin(sub_addr)
            sub_name = sub_cate_name[idx]
            # print("2차 카테고리", sub_url, sub_name)
            yield scrapy.Request(
                sub_url,
                self.parse_item,
                meta={"main_cate": main_cate, "sub_cate": sub_name},
                dont_filter=True,
            )

    def parse_item(self, response):
        # print(
        #     "parse_item {},main_cate {} , sub_cate {}".format(
        #         response.url, response.meta["main_cate"], response.meta["sub_cate"]
        #     )
        # )

        # ALL : 1~200 아이템 추출
        # 나머지 : 100개 아이템 추출
        # gBestWrap > div > div:nth-child(5) > div:nth-child(3) > ul > li:nth-child(1)
        # 제품명

        # items = response.css(
        #     "#gBestWrap > div > div:nth-child(5) > div:nth-child(3) > ul > li> a::text"
        # ).getall()
        # # 원가
        # prices = response.css(
        #     "#gBestWrap > div > div:nth-child(5) > div:nth-child(3) > ul > li > div.item_price > div.o-price > span > span::text"
        # ).getall()
        # # 판매가
        # sale_prices = response.css(
        #     "#gBestWrap > div > div:nth-child(5) > div:nth-child(3) > ul > li > div.item_price > div.s-price > strong > span > span::text"
        # ).getall()
        # # 할인율
        # sale_rates = response.css(
        #     "#gBestWrap > div > div:nth-child(5) > div:nth-child(3) > ul > li > div.item_price > div.s-price > span > em::text"
        # ).getall()
        # for idx, item1 in enumerate(items):
        #     item = GmarketbestItem()
        #     item["item"] = item1
        #     item["price"] = prices[idx]
        #     item["sale_price"] = sale_prices[idx]
        #     item["sale_rate"] = sale_rates[idx]
        #     yield item
        sectors = response.css(
            "#gBestWrap > div > div:nth-child(5) > div:nth-child(3) > ul > li"
        )

        for idx, sector in enumerate(sectors, 1):
            item = GmarketbestItem()
            item["item"] = sector.css("a::text").get()
            code = sector.css("a::attr('href')").get()

            pattern = re.compile("code=[0-9]+")
            temp = pattern.findall(code)
            item["item_code"] = temp[0].replace("code=", "")

            item["price"] = sector.css(
                "div.item_price > div.o-price > span > span::text"
            ).get()
            item["sale_price"] = (
                sector.css(" div.item_price > div.s-price > strong > span > span::text")
                .get()
                .replace("원", "")
                .replace(",", "")
            )
            if item["price"] == None:
                item["price"] = item["sale_price"]
            else:
                item["price"] = item["price"].replace("원", "").replace(",", "")
            item["sale_rate"] = sector.css(
                " div.item_price > div.s-price > span > em::text"
            ).get()

            if item["sale_rate"] == None:
                item["sale_rate"] = "0"
            else:
                item["sale_rate"] = item["sale_rate"].replace("%", "")
            item["main_cate"] = response.meta["main_cate"]
            item["sub_cate"] = response.meta["sub_cate"]
            item["ranking"] = idx
            yield item
            # rank = scrapy.Field()
            # item = scrapy.Field()
            # price = scrapy.Field()
            # link = scrapy.Field()
