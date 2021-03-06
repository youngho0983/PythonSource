from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver = "./crawl/chromeDriver/chromedriver"

headless_options =webdriver.ChromeOptions()
#브라우저 안 띄우기
headless_options.add_argument("headless")
#그래픽 카드 안쓰기
headless_options.add_argument("disable-gpu")
#클라이언트 user-agent 설정
headless_options.add_argument("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36")

#브라우저 크기 조정 
headless_options.add_argument("window-size=1920x1080")

#사용자의 언어
headless_options.add_argument("lang=ko_KR")

driver =webdriver.Chrome(chrome_driver , options = headless_options)

driver.get("http://www.python.org")

print(driver.title)