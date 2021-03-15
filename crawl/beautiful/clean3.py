#클리안 사이트의 자료실 게시판 크롤링 
#제목, 작성자, 날짜를 크롤링 한 후 엑셀 파일로 저장하기

import requests
from bs4 import BeautifulSoup
import xlsx_write1 as excel


s=requests.Session()
url=""


url="https://www.clien.net/service/board/pds"
    
response= s.get(url)
soup=BeautifulSoup(response.text)
contentlist=soup.select("#div_content > div.list_content .symph_row")

# print(contentlist)
titlelist=[]
writerlist=[]
datelist=[]
for item in contentlist:
    titlelist.append(item.select_one(".subject_fixed").string.strip())
    datelist.append( item.select_one("div.list_time > span span").string)
    if(item.select_one(".nickname span")!=None):
         writerlist.append(item.select_one(".nickname span").string)
        
    else:
       
        writerlist.append(item.select_one(".nickname img")["alt"])
# print(writerlist)
lastlist=[]
templist=[]
for num,item in enumerate(titlelist):
    templist.append(titlelist[num])
    templist.append(writerlist[num])
    templist.append(datelist[num])
    lastlist.append(templist)
    templist=[]
print(lastlist)
excel.write_excel_template("hello.xlsx","클리앙",lastlist)