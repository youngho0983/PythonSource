from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./crawl/chromeDriver/chromedriver")

driver.get("http://www.google.com")

print("현재 창 :{} ".format(driver.title))

parent_window = driver.current_window_handle

driver.execute_script("window.open('https://www.naver.com')")

all_windows = driver.window_handles
print(all_windows)
child_window = [window for window in all_windows if window != parent_window][0]
print("child_window info :{}".format(child_window))

driver.switch_to.window(child_window)
print("현재 창 : {} ".format(driver.title))

driver.close()

driver.switch_to_window(parent_window)
print("제어권 확인 : {}".format(driver.title))
