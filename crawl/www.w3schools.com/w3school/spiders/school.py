import scrapy


class SchoolSpider(scrapy.Spider):
    name = "school"
    allowed_domains = ["w3schools.com"]
    start_urls = ["https://w3schools.com/"]

    def parse(self, response):
        titles = response.css("#mySidenav > div> a::text").getall()

        links = response.css("#mySidenav>div>a::attr('href')").getall()

        for idx, title in enumerate(titles):
            yield {"title": title, "link": links[idx]}
