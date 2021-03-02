#다음 
# https://news.v.daum.net/v/20210225101511841


import urllib.request as request
from urllib.error import HTTPError

url="https://news.v.daum.net/v/20210225101511841"

try:
    response =request.urlopen(url).read().decode("utf-8")
except HTTPError as e:
    print(e)
else :
    print(response)