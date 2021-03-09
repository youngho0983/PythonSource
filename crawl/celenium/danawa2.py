from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup
import openpyxl
import requests
from io import BytesIO
from fake_useragent import UserAgent



workbook = openpyxl.Workbook()

worksheet = workbook.active

worksheet.column_dimensions["A"].width = 50
worksheet.column_dimensions["B"].width = 18
worksheet.column_dimensions["C"].width = 10

worksheet.append(["제품명", "가격", "이미지"])


driver = webdriver.Chrome("./crawl/chromeDriver/chromedriver")
driver.get("http://www.danawa.com/")

que = driver.find_element_by_css_selector("#AKCSearch")
que.send_keys("애플")
que.send_keys(Keys.ENTER)

time.sleep(3)
driver.find_element_by_css_selector(
    "#relatedKeywordArea > dl > dd > div:nth-child(1) > a:nth-child(1)"
).click()

time.sleep(3)
img_src = ""
idx = 1
cur_page, target_crawl_num = 1, 6

while cur_page <= target_crawl_num:
    soup = BeautifulSoup(driver.page_source, "html.parser")

    product_list = soup.select("div.main_prodlist > ul > li:not(.product-pot)")
    for product in product_list:

        if not product.find("div", class_="ad_header"):
            
            prod_name = product.select_one("p.prod_name > a ").text.strip()
            prod_price = product.select_one("p.price_sect > a").text.strip()
            img = product.select_one(".thumb_image img")
            if img.get("data-original"):
                img_src = img.get("data-original")
            else:
                img_src = img.get("src")


            response=requests.get(img_src,headers={"user-agent" : UserAgent().chrome})
            prod_img =BytesIO(response.content)

            worksheet.append([prod_name,prod_price])
            
            img_save =openpyxl.drawing.image.Image(prod_img)
            img_save.width =30
            img_save.height=20
            worksheet.add_image(img_save,"C"+str(idx))
            # print(idx, prod_name, prod_price, "http:" + img_src)
            worksheet.append([prod_name, prod_price])
            idx += 1
        print()
    workbook.save("./crawl/data/danawa_apple.xlsx")
    cur_page += 1
    time.sleep(10)
    # driver.execute_script("window.scrollTo(0, 88*( document.body.scrollHeight/100))")
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(

    #             (By.CSS_SELECTOR,
    #             "div.paging_number_wrap > a.snum:nthchild("+str(cur_page)+")"
    #             )

    #     )
    # ).click()
    time.sleep(4)
    print("div.paging_number_wrap > a.snum:nth-child(" + str(cur_page) + ")")
    driver.find_element_by_css_selector(
        ".paging_number_wrap >a:nth-child("+str(cur_page)+")"
    ).click()
    del soup
    # productListArea > div.search_paging_nav > div > div > a.snum:nthchild()
    # productListArea > div.search_paging_nav > div > div > a:nth-child(2)

time.sleep(3)
