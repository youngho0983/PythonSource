import urllib.request as request
from urllib.parse import urlparse
from urllib.parse import urlencode
from urllib.error import HTTPError

# 행정안전부 rss 정보 가져오기

rss = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"
params=[]
for num in [1001,1012,1013,1014] :
    params.append(dict(ctxCd=num))

print(params)

for temp in params:
    url=rss+"?"+urlencode(temp)

    response=request.urlopen(url).read().decode("utf-8")

    print(response)
