import requests

s = requests.Session()

r=s.get("http://httpbin.org/cookies",cookies={"name":"hong"})




print(r.text)
print(r.headers)


s.close()