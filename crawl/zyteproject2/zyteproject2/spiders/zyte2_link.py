import scrapy


class Zyte2Spider(scrapy.Spider):
    name = "zyte2_link"
    allowed_domains = ["www.zyte.com"]
    start_urls = ["http://www.zyte.com/blog/"]

    def parse(self, response):

        for url in response.css(
            "#_posts_grid-98-2233 > div.oxy-posts > div > div.oxy-post-wrap > div > a::attr('href')"
        ).getall():
            # yield scrapy.Request("https://www.zyte.com" + url, self.parse_article)
            # print(self.parse_article)

            yield scrapy.Request(response.urljoin(url), self.parse_article)

    def parse_article(self, response):
        print(response.url)

        contents = response.css("#blog-body span p::text").extract_first()
        # print(contents)
        # return {"contents": contents}
        yield {"content": contents}
