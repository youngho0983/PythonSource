import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

userAgent =UserAgent()
data={
    "user-agent":userAgent.chrome
}


r=requests.get("https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=437&aid=0000260072",
                headers=data)


soup=BeautifulSoup(r.text,"html.parser")

#print(type(soup))
#print("***"*10)
#print(soup)

# find() : 제일 처음에 만나는 태그를 가져오기
title=soup.find("h3")
print(title)
print(title.string)
print(title.get_text)