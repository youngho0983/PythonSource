from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./crawl/chromeDriver/chromedriver")


driver.get("http://python.org")

element = driver.find_element_by_name("q")

element.send_keys("python")
element.send_keys(Keys.ENTER)

elements = driver.find_elements_by_css_selector("ul li h3")
for title in elements:
    print(title)
