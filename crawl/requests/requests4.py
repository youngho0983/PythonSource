import requests
from fake_useragent import UserAgent

s = requests.Session()
userAgent=UserAgent()

headers={"user-agent":userAgent.chrome}


r=s.get("http://httpbin.org/get",headers=headers)




print(r.text)
print(r.headers)


s.close()