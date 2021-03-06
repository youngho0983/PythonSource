from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()

options.add_argument("headless")
# options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome("./crawl/chromeDriver/chromedriver", options=options)


driver.get("http://daum.net")

search = driver.find_element_by_css_selector("[id=q]")
search.send_keys("아이폰")
search.send_keys(Keys.ENTER)
elements = driver.find_elements_by_css_selector("a.keyword")
a = 1
for title in elements:
    print(title.text)
    print(a)
    a += 1
