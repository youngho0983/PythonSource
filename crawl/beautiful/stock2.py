#https://finance.naver.com/ 인기 검색 이름 , 가격

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from fake_useragent import UserAgent

try:
    with requests.Session() as s:
        useragent=UserAgent()
        headers={
            "user-agent":useragent.chrome
        }
        response=s.get("https://finance.naver.com/",headers=headers)

        soup=BeautifulSoup(response.text,"html.parser")

       

except Exception as e:
    print(e)

else:
    result= soup.select(".aside_stock table tbody >tr")

    # print(result)

    for rep in result :
    
        #print(rep)
        print("**"*10)
        name=rep.select_one("a")
        print(name.string)
        
        price=rep.select_one("td")
        print(price.string)
        print("---")





