import requests
from bs4 import BeautifulSoup

s=requests.Session()
url=""

for i in range(5):
    url="https://www.clien.net/service/group/allinfo?&od=T31&po="+str(i)
    
    response= s.get(url)
    soup=BeautifulSoup(response.text)
    titles =soup.select("span.subject_fixed")
    print("현재의 페이지"+str(i+1))
    num=1
    for tt,title in enumerate(titles ,start=1):
        print("현재의 게시물 넘버"+str(num) )
        num+=1
        print(title.string.strip())