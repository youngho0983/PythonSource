from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver =webdriver.Chrome("./crawl/chromeDriver/chromedriver")
driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%ED%8A%B8%EB%9F%AD")
driver.implicitly_wait(3)  #time.sleep(3)

temp_imgs=driver.find_elements_by_css_selector("div.thumb > a > img")

for img in temp_imgs:
    print(img.get_attribute("src"))