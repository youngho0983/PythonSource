from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome("./crawl/chromeDriver/chromedriver")
driver.get("https://ecos.bok.or.kr/EIndex.jsp")
time.sleep(3)
driver.find_element_by_css_selector("#frm > div.EScontent.ESwrap > div.ESsubject > ul > li:nth-child(1) > a > img").click()

windows=driver.window_handles

driver.switch_to_window(windows[1])
print(driver.title)
time.sleep(3)
driver.find_element_by_css_selector(".HScontent-header fieldset  a").click()
time.sleep(3)

