import requests

s = requests.Session()

#r=s.get("https://httpbin.org/get")
data={
    "name":"hong"
}
#r=s.post("http://httpbin.org/post",data=data)

#r=s.delete("https://httpbin.org/delete")

r=s.put("https://httpbin.org/put",data=data)
print(r.text)

s.close()