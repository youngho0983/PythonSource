import requests
from bs4 import BeautifulSoup
import xlsx_write1 as excel
import regex
s=requests.Session()
url=""
title_lists=[]
for i in range(1):
    url="https://www.clien.net/service/group/allinfo?&od=T31&po="+str(i)
    
    response= s.get(url)
    soup=BeautifulSoup(response.text)
    titles =soup.select("span.subject_fixed")
    # print("현재의 페이지"+str(i+1))
    
    for item in titles:
        title=regex.sub("/xld"," " , item.text.strip())
        title_lists.append([title])
excel.write_excel_template("clien.xlsx","팁과 강좌",title_lists)