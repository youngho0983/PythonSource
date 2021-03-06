from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver = "./crawl/chromeDriver/chromedriver"

headless_options =webdriver.ChromeOptions()
headless_options.add_argument("headless")
driver =webdriver.Chrome(chrome_driver , options = headless_options)

driver.get("http://www.python.org")

print(driver.title)