# import scrapy
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import time

# driver = webdriver.Chrome("./crawl/chromeDriver/chromedriver")
# driver.get("http://gtour.")

# print(driver.page_source)

# WebDriverWait(driver, 3).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "h1.itemtit"))
# )

# soup = BeautifulSoup(driver.page_source, "html.parser")

# print(soup.select_one("h1.itemtit").text)

# time.sleep(3)