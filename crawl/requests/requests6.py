import requests

with requests.Session() as s:
   r=s.get("https://jsonplaceholder.typicode.com/todos/1",stream=True)
   print("headers:{}".format(r.headers))
   print("json   :{}".format(r.json()))
   print("keys() :{}".format(r.json().keys()))
   print("values():{}".format(r.json().values()))
   print("encoding:{}".format(r.encoding))
   print("content :{}".format(r.content))
   #b'{\n  "userId": 1,\n  "id": 1,\n  "title": "delectus aut autem",\n  "completed": false\n}'
   #r.text  ==>   text

   #.content ==>  바이너리 형태 응답


