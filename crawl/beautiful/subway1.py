#https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError

try :

    url="https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0"

    with requests.Session() as s:
        response =s.get(url)
        result=BeautifulSoup(response.text,"html.parser")
except Exception as e:
    print(e)

else:
    pic1= result.select_one("#mw-content-text > div.mw-parser-output > div.thumb.tright > div > a > img")
    print(pic1)
    print( (pic1.attrs["src"]) )

    image2 =result.select_one("img.thumbimage")
    print(image2)

    

    print(image2["src"])