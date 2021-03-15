from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("./crawl/chromeDriver/chromedriver")
driver.get("http://daum.net")

search=driver.find_element_by_css_selector("[id=q]")
search.send_keys("아이폰")
search.send_keys(Keys.ENTER)
elements=driver.find_elements_by_css_selector("#recomm_lists_top > span")

driver.save_screenshot("./crawl/data/iphone1.jpg")

driver.get_screenshot_as_file("./crawl/data/iphone2.png")

