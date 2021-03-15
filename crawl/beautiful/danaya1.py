# 로그인 이후에 크롤링하기
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

login_info={
    "redirectUrl":"hrrp://www.danawa.com/",
    "loginMemberType": "general",
    "id":"youngho0983",
    "isSaveId":"true",
    "password":"Cmdizl2115*"
}
headers={
    "user-agent":UserAgent().chrome,
    "Referer" : "https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2Fmember%2FmyPage.php"
}

with requests.Session() as s:
    res=s.post("https://auth.danawa.com/login",login_info,headers=headers)

    print(res.text)