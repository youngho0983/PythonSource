from selenium import  webdriver

driver=webdriver.Chrome("./crawl/chromeDriver/chromedriver")


driver.get("http://python.org")

print(driver.title)

assert "Pythone" in driver.title

print(driver.page_source)