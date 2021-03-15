from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import urllib.request as request
import os

driver = webdriver.Chrome("./crawl/chromeDriver/chromedriver")

driver.implicitly_wait(3)  # time.sleep(3)

driver.get("https://search.naver.com")
driver.maximize_window()

query = driver.find_element_by_id("query")

query.send_keys("트럭")
query.send_keys(Keys.ENTER)

image_tab = driver.find_element_by_css_selector(
    "#lnb > div.lnb_group > div > ul > li:nth-child(2) > a"
)
image_tab.click()

img_tiles = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.photo_tile._grid"))
)

# 스크롤 이동



driver.execute_script("console.log(document.body.scrollHeight)")
time.sleep(3)



driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)




time.sleep(3)

driver.execute_script("window.scrollTo(0,0)")
time.sleep(3)
temp=0
for i in range(1,80):
    driver.execute_script( " window.scrollTo(0,"+str(i)+ "* document.body.scrollHeight /100)")
    
    time.sleep(0.1)
    
temp_imgs = driver.find_elements_by_css_selector("div.thumb > a > img")
save_path="C:\\imagedown\\"

for img in temp_imgs:
    print("hello?")
    print(img.get_attribute("src"))
    file_name=os.path.join(save_path,save_path+str(temp)+".png")
    request.urlretrieve(img.get_attribute("src"),file_name)

    print(temp)
    temp+=1
time.sleep(2)
