import requests
from bs4 import BeautifulSoup

with open("./crawl/beautiful/story.html","r") as f:
    response =f.read()


soup=BeautifulSoup(response,"html.parser")


b=soup.select_one("p")
print(b)
print(b.string)
print(b.get_text())
print(b.text)

print()

link1=soup.select_one("#link1")
print(link1)

# print(link1.text)


link2=soup.select("p.story>a")
print(link2)
link4=soup.select("p.story")
for i in link4:
    
    temp = i.find_all("a")
    if temp:
        for v in temp:
            print("-----",v)
            print("----",v.string)
    else:
        print("------ 종료~")


