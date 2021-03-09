from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./crawl/chromeDriver/chromedriver")
driver.get("http://www.danawa.com/")
driver.find_element_by_css_selector(
    "#danawa_header > div.danawa_top_search > div > div.my_service > div.my_service_list > ul > li.my_page_service > a > span"
).click()

idtext = driver.find_element_by_css_selector("#danawa-member-login-input-id")
idtext.clear()
idtext.send_keys("youngho0983")

passwordtext = driver.find_element_by_css_selector("#danawa-member-login-input-pwd")
passwordtext.clear()
passwordtext.send_keys("Cmdizl2115*")
passwordtext.send_keys(Keys.ENTER)


query = driver.find_element_by_css_selector("#AKCSearch")
query.send_keys("맥북")
query.send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element_by_css_selector(
    "#SearchOption_BasicOption_1208_All > div:nth-child(1) > div > label > span"
).click()
driver.find_element_by_css_selector(
    "#SearchOption_BasicOption_310238_All > div:nth-child(1) > div > label > span"
).click()
driver.find_element_by_css_selector(
    "#SearchOption_BasicOption_1207_All > div:nth-child(1) > div > label > span.ico.i_chkbox"
).click()
driver.execute_script("window.scrollTo(0, 10*( document.body.scrollHeight/100))")
time.sleep(1)
driver.find_element_by_css_selector(
    "#productItem9526743 > div > div.prod_info > p > a"
).click()
time.sleep(5)
windows = driver.window_handles
print(windows[0])
print(windows[1])
driver.switch_to_window(windows[1])
driver.find_element_by_css_selector("#interest > span.ico.ico_interest").click()
time.sleep(3)
driver.find_element_by_css_selector("#wishFolder_101515623").click()

driver.find_element_by_css_selector(
    "#danawa_header > div.danawa_top_search > div > div.my_service2 > div.my_service_list3 > ul > li.interest_goods_service > a > span.my_serv_tit"
).click()
time.sleep(4)
product_name = driver.find_element_by_css_selector(
    "#wishProductListArea > table > tbody > tr > td.info > div.tit > a"
).text
product_price = driver.find_element_by_css_selector(
    "#wishProductListArea > table > tbody > tr > td.lowest > dl > div.cost > span > em"
).text
product_img_src = driver.find_element_by_css_selector(
    "#wishProductListArea > table > tbody > tr > td.img > a > span > img"
).get_attribute("src")
print("제품명" + product_name)
print("제품 가격" + product_price)
print("제품 이미지 주소" + product_img_src)
