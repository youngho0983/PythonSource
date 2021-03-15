#클리안 사이트의 자료실 게시판 크롤링 
#제목, 작성자, 날짜를 크롤링 한 후 엑셀 파일로 저장하기

import requests
from bs4 import BeautifulSoup
import xlsx_write1 as excel


s=requests.Session()



url="https://www.clien.net/service/board/pds"
try:    
    response= s.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    contentlist=soup.select("#div_content > div.list_content .symph_row")
    pds_lists=list()
    rows =soup.select("div.list_content >div")
    print(rows)

    for row in rows:
        title=row.select_one()
except Exception as e:
    print(e)