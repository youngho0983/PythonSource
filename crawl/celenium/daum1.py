from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver =webdriver.Chrome("./crawl/chromeDriver/chromedriver")

driver.get("http://daum.net")

print(driver.title)


print("Session Id : {} ".format(driver.session_id))
print("Cookies    : {}".format(driver.get_cookies))

element=driver.find_element_by_name("q")

element.send_keys("아이폰")
time.sleep(5)
element.send_keys(Keys.ENTER)


print(driver.title)
time.sleep(5)
driver.back()
driver.forward()