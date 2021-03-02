#http://api.ipify.org/?format=text
import urllib.request as request
from urllib.error import HTTPError

api="http://api.ipify.org"
url=api+"?"+"format=json"
print("요청 URL {} ".format(url))

response=request.urlopen(url).read().decode("utf-8")
print(response)