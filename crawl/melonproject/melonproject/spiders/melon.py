import scrapy


class MelonSpider(scrapy.Spider):
    name = "melon"
    allowed_domains = ["https://www.melon.com/chart/index.htm"]
    start_urls = ["https://www.melon.com/chart/index.htm"]

    def parse(self, response):
        # titles = response.css(
        #     "#frm > div > table > tbody > tr > td:nth-child(4) > div > div > div.ellipsis.rank01 > span > a::text"
        # ).getall()
        # singers = response.css(
        #     "#frm > div > table > tbody > tr > td:nth-child(4) > div > div > div.ellipsis.rank02 > a::text"
        # ).getall()
        # albums = response.css(
        #     "#frm > div > table > tbody > tr > td:nth-child(5) > div > div > div > a::text"
        # ).getall()

        # for idx, title in enumerate(titles):
        #     yield {"title": title, "singer": singers[idx], "album": albums[idx]}
        songs = response.css("tbody > tr")

        idx = 0
        for song in songs:
            # 노래명 추출
            title = song.css("td:nth-child(4) div.rank01 a::text").get()
            singer = song.css("td:nth-child(4) div.rank02 a::text").get()
            album = song.css("td:nth-child(5) div.rank03 a::text").get()

            idx += 1
            yield {"idx": idx, "title": title, "singer": singer, "album": album}
