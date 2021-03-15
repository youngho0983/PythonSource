# Beautifulsoup
# 다양한 파서 사용 가능 으헤헿 흐에헤으으헤헿에흐이흐에흥
# html.parser, lxml ....
# 태그명 , name , 속성 ( 아이디 , 클래스 ,클래스 선택자 ) 를 이용하여 원하는 요소
# 찾기 가능
import requests
from bs4 import BeautifulSoup

# 페이지 용정
r = requests.get("https://gallery.v.daum.net/p/viewer/5014013/cKotzJWsRE")

#soup 객체 생성
soup = BeautifulSoup(r.text , "html.parser")

#확인
#print(soup)

#이쁘게 나오게
#print(soup.prettify())

print(soup.head)

print("******"*10)
print(soup.body)
print("******"*10)
print(soup.title)
print("******"*10)
print(soup.title.name)
print("******"*10)

print(soup.title.string)
print("******"*10)

print(soup.title.get_text())
print("******"*10)


#print(dir(soup))
