import scrapy


class Zyte2Spider(scrapy.Spider):
    name = "zyte2"
    allowed_domains = ["www.zyte.com/blog"]
    start_urls = ["http://www.zyte.com/blog/"]

    def parse(self, response):
        # # 타이틀 추출
        # title = response.css(
        #     "#_posts_grid-14-940 > div > div.oxy-post > div > div:nth-child(1) > a::text"
        # ).get()
        # # 작성 날짜 추출
        # date = (
        #     response.css(
        #         "#_posts_grid-14-940 > div > div.oxy-post > a > div.oxy-post-image-date-overlay::text"
        #     )
        #     .get()
        #     .strip()
        # )
        # # 링크 추출
        # link = response.css(
        #     "#_posts_grid-14-940 > div > div.oxy-post > div > div:nth-child(1) > a::attr('href')"
        # ).get()

        # print(title)
        # print(date)
        # print(link)
        dates = response.css(
            "#_posts_grid-98-2233 > div.oxy-posts > div > a > div.oxy-post-image-date-overlay::text"
        ).getall()
        titles = response.css(
            "#_posts_grid-98-2233 > div.oxy-posts > div > div.oxy-post-wrap > div > a::text"
        ).getall()
        # _posts_grid-98-2233 > div.oxy-posts > div:nth-child(1) > div.oxy-post-wrap > div > a
        links = response.css(
            "#_posts_grid-98-2233 > div.oxy-posts > div > div.oxy-post-wrap > div > a::attr('href')"
        ).getall()
        i = 0
        # while i < len(titles):
        #     print(dates[i])
        #     print(titles[i])
        #     print(links[i])
        #     i += 1
        for idx, title in enumerate(titles):
            # print("{} {} {} ".format(dates[idx].strip(),title,links[idx]))
            yield {"date": dates[idx].strip(), "title:": title, "link": links[idx]}
