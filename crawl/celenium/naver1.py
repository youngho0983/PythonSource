from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./crawl/chromeDriver/chromedriver")

driver.get("http://naver.com")

# finder = driver.find_element_by_id("query")

finder=driver.find_element(By.NAME,"query")
finder.send_keys("아이폰")
finder.send_keys(Keys.ENTER)

print(driver.title)