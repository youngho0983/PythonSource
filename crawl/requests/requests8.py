import requests

with requests.Session() as s:
   r=s.get("https://jsonplaceholder.typicode.com/users")
  
   for row in r.json():
      for k,v in row.items():
         print("ket : {}, values : {}".format(k,v))
         print()
  
   #b'{\n  "userId": 1,\n  "id": 1,\n  "title": "delectus aut autem",\n  "completed": false\n}'
   #r.text  ==>   text

   #.content ==>  바이너리 형태 응답


