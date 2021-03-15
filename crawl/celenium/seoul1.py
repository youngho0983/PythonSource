from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./crawl/chromeDriver/chromedriver")

driver.get("https://sll.seoul.go.kr/main/MainView.dunet")

driver.find_element_by_css_selector("#close2_14324326 >img").click()

driver.find_element_by_css_selector(".srh-in").click()

element = driver.find_element_by_name("query")

element.send_keys("자바")
element.send_keys(Keys.ENTER)
time.sleep(5)

all_window=driver.window_handles

driver.switch_to.window(all_window[1])

print(driver.current_url)

driver.find_element_by_css_selector("#contArea > div.article-full > div:nth-child(9) > a").click()

# all_window=driver.window_handles

# driver.switch_to_window(all_window[2])

elements=driver.find_elements_by_css_selector(".subject")

for title in elements:
    print(title.text)


time.sleep(6)

