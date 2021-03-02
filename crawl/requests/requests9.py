import requests

with requests.Session() as s:
   r=s.get("https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=GMP&durationDays=30&count=100&_=1614242576538")
  
   for row in r.json():
      for k,v in row.items():
         if(k=="product_name"):
            print("ket : {}, values : {}".format(k,v))
            print()
  
   #b'{\n  "userId": 1,\n  "id": 1,\n  "title": "delectus aut autem",\n  "completed": false\n}'
   #r.text  ==>   text

   #.content ==>  바이너리 형태 응답


