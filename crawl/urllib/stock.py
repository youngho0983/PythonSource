import urllib.request as request
from fake_useragent import UserAgent
import json
import csv

userAgent=UserAgent()

header={
    'user-agent':userAgent.chrome,
    'referer':'http://finance.daum.net'

}
data =[]
url='https://finance.daum.net/api/search/ranks?limit=10'
try:

    request_url=request.Request(url,headers=header)

    response=request.urlopen(request_url).read().decode("utf-8")
    
except Exception as e:
    print(e)
    
else :
    #print( response)

    rank_json =json.loads(response)["data"]
    #print(rank_json)
    for item in rank_json :
        print("순위 :{} , 금액 : {} ,  회사명 : {} ".format(item['rank'],item['tradePrice'] ,item['name'],))

        data.append(item)
with open("c:/stock.txt","a") as f1 ,open("c:/finance.csv","w",newline="") as f2:
    f1.write("순위 :{} , 금액 : {} ,  회사명 : {} ".format(item['rank'],item['tradePrice'] ,item['name']))

    output=csv.writer(f2)
    print(data[0].keys())
    output.writerow(data[0].keys())
    for row in data:
        output.writerow(row.values()) # value
