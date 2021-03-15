#http://api.ipify.org/?format=text
import urllib.request as request
from urllib.error import HTTPError
from urllib.parse import urlencode
values={"format":"json","hello":"good"}
api="http://api.ipify.org"
url=api+"?"+urlencode(values)

print("before param : {}".format(values))
print("요청 URL {} ".format(url))
print("after param : {}".format(urlencode(values)))

response=request.urlopen(url).read().decode("utf-8")
print(response)