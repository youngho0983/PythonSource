from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome("./crawl/chromeDriver/chromedriver")

driver.get("http://danawa.com")

driver.find_element_by_css_selector("#danawa_header > div.danawa_top_search > div > div.my_service > div.my_service_list > ul > li.my_page_service > a > span").click()

driver.find_element_by_css_selector("#danawa-member-login-input-id").clear()
driver.find_element_by_css_selector("#danawa-member-login-input-id").send_keys("youngho0983@naver.com")

# driver.find_element_by_css_selector("#danawa-member-login-input-pwd").clear()
driver.find_element_by_css_selector("#danawa-member-login-input-pwd").send_keys("Cmdizl2115*")

driver.find_element_by_css_selector("#danawa-member-login-input-pwd").send_keys(Keys.ENTER)


time.sleep(5)