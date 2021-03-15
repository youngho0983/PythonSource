#다음 
# https://news.v.daum.net/v/20210225101511841


import urllib.request as request
from urllib.error import HTTPError

#url="https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=421&aid=0005186491"
url="https://news.v.daum.net/v/20210225101511841"
try:
    request_url=request.Request(url)
    response =request.urlopen(request_url).read().decode("utf-8")
except HTTPError as e:
    print(e)
else :
    print(request_url.header_items())
    #print(response)