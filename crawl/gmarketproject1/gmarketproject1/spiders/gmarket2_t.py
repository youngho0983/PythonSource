import scrapy
import time

import scrapy
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from scrapy_selenium import SeleniumRequest


class Gmarket1Spider(scrapy.Spider):
    name = "gmarket2_t"
    # allowed_domains = ["http://corners.gmarket.co.kr"]
    start_urls = ["http://corners.gmarket.co.kr/Bestsellers"]
    # def start_requests(self):
    #     url = "http://corners.gmarket.co.kr/Bestsellers"
    #     yield scrapy.Request(url=url, callback=self.parse_countries)

    def parse(self, response):
        url = response.css("#categoryTabG > li.group11 > a::attr('href')").get()

        yield scrapy.Request(response.urljoin(url), self.parse_next)
        # yield SeleniumRequest(
        #     url=response.urljoin(url),
        #     callback=self.parse_next,
        #     wait_time=5,
        #     wait_until=EC.element_to_be_clickable((By.CSS_SELECTOR, "h1.itemtit")),
        # )

    def parse_next(self, response):

        url = response.url

        print("url 1차시기")
        print(url)
        if url.find("corner") != -1:
            print("corner ", response.url)
            urls = response.css(
                "#gBestWrap > div > div:nth-child(5) > div:nth-child(3) > ul > li > a::attr('href')"
            ).getall()
            i = 1
            for url in urls:
                print("for the for")
                print(url)
                i += 1
                if i == 10:
                    break
                yield scrapy.Request(response.urljoin(url), self.parse_next)

        else:

            # print("gtour", response.url)
            driver = webdriver.Chrome("C:\pythonSource\crawl\chromeDriver\chromedriver")
            url = response.url
            if url.find("item") != -1:
                driver.get(response.url)
            else:
                print("")
                print("")
                print("")
                print(url)
                print("")
                print("")
                print("")

                driver.get(response.url)
            driver.implicitly_wait(5)
            item = driver.find_element_by_css_selector("h1.itemtit").text

            # price = driver.find_element_by_css_selector(
            #     "#itemcase_basic > div > p > span > strong"
            # ).text
            # container > div.item-topinfowrap.top_area > div.item-topinfo > div.item-topinfo_headline > p.price > span > strong

            # item = response.css("h1.itemtit::text").get()
            # container > div.item-topinfowrap.top_area > div.item-topinfo > div.item-topinfo_headline > h1
            # price = response.css(
            #     "#itemcase_basic > div.box__item-title > p > span > strong::text"
            # ).get()
            print("엠링ㄴ모리오밀")
            print(item, url)
            driver.quit()
            yield {"item": item, "url": url}
