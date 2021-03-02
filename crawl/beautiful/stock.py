#https://finance.naver.com/ 인기 검색 이름 , 가격

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError

try:
    with requests.Session() as s:

        response=s.get("https://finance.naver.com/")

        temp=BeautifulSoup(response.text,"html.parser")

       

except Exception as e:
    print(e)

else:
    popul=temp.select_one(".aside_popular")
    print(popul)
    compa=popul.select("th")
    