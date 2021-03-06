from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./crawl/chromeDriver/chromedriver")
driver.get("http://youtube.com")

search=driver.find_element_by_id("search")

search.send_keys("아잉눈")
search.send_keys(Keys.ENTER)
# time.sleep(3)
driver.implicitly_wait(3)

elements= driver.find_elements_by_css_selector(".title-and-badge")
for title in elements:
    print(title.text)
