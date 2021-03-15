#https://finance.naver.com/ 인기 검색 이름 , 가격

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError

try:
    with requests.Session() as s:

        response=s.get("https://finance.naver.com/")

        soup=BeautifulSoup(response.text,"html.parser")

       

except Exception as e:
    print(e)

else:
    result= soup.select(".aside_popular table tbody >tr")

    # print(result)

    for rep in result :
    
        #print(rep)
        print("**"*10)
        name=rep.select_one("a")
        print(name.string)
        
        price=rep.select_one("td")
        print(price.string)
        print("---")





