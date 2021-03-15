from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./crawl/chromeDriver/chromedriver")

driver.get("http://daum.net")

driver.find_element_by_css_selector("#newsTab > a").click()

all_window = driver.window_handles
# driver.switch_to_window(all_window[1])

driver.find_element_by_css_selector(
    "#cSub > div > ul > li:nth-child(3) > div.item_issue > div > strong > a"
).click()


all_window = driver.window_handles

print(driver.find_element_by_css_selector("#cSub > div > span > span:nth-child(1)").text  )
