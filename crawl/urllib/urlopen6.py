#  http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml

import urllib.request as request
from urllib.error import HTTPError
url="http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=f5eef3421c602c6cb7ea224104795888&targetDt=20200101"
try:
    file1 , header1 =request.urlretrieve(url,"c:/movie.mxl")
    response =request.urlopen(url).read().decode("utf-8")
    print("***"*40)
except HTTPError as e:
    print(e)
else:
    print(file1)
    print(header1)
    print(response)
    with open("c:/hello.txt","w") as f:
        f.write(response)

