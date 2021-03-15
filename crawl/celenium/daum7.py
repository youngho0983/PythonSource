from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# wait 을 위한 묘듈
from selenium.webdriver.support.ui import WebDriverWait

# 마우스 키보드를 조작하는 모듈
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# selenium => waits         => time.sleep 으로 대체 가능
# 웹 페이지에서 dom 의 element 들이 자리를 잡는 시간이 필요함
# 자리를 잡지 못할 때 특정 엘레멘트를 찾으라고 하면  ElementNotVisibleException
# 발생 => waits 를 이용해서 이런 부분을 해결 함
# implicit wait : 요소를 찾기 위해 web driver 가 일정 시간 동안 요청
# explicit wait : web driver 가 실행을 계속하기 전에 특정 조건이 발생할 때까지 기다리는 것
driver = webdriver.Chrome("./crawl/chromeDriver/chromedriver")

driver.get("http://news.v.daum.net/v/20210305163153584")
driver.implicitly_wait(3)
loop, count = True, 0

recent = driver.find_element_by_css_selector(
    "#alex-area > div > div > div > div.cmt_box > ul.list_category > li:nth-child(3) > button > span > span"
)
if recent:
    recent.click()
else:
    time.sleep(3)
    recent = driver.find_element_by_css_selector(
        "#alex-area > div > div > div > div.cmt_box > ul.list_category > li:nth-child(3) > button > span > span"
    )

while loop and count < 10:
    print(count)
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".cmt_box > div.alex_more >button")
            )
        )
        if element:
            element.click()
        count += 1

    except TimeoutException:
        loop = False


# 댓글 내용 출력하기


reply = driver.find_elements_by_css_selector("li > div > p")

for comment in reply:
    print(comment.text)
