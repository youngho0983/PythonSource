from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome("./crawl/chromeDriver/chromedriver")
driver.get("https://www.gmarket.co.kr/")

element=driver.find_element_by_name("keyword")

element.send_keys("핫바")
element.send_keys(Keys.ENTER)