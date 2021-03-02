import urllib.request as request

#정보를 가져올 url
url="http://google.com"

#가져온 정보를 저장할 위치
save_url="c:/google.html"
hell=""
try:
    hell=file1,header1=request.urlretrieve(url,save_url)
except Exception as e:
    print(e)
else:
    print(header1)
    print("성공")
    print(hell)