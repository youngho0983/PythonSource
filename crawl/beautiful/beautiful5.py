from bs4 import BeautifulSoup


with open("./crawl/beautiful/story.html","r") as f:
    response =f.read()


soup = BeautifulSoup(response, "html.parser")

#find_all() 결과를 모두 찾아서 리스트를 반환한다
# a1=soup.find_all("a")
# print(a1)

# a2=soup.find_all("a",limit=2)
# print(a2)

# link =soup.find_all("a",class_="sister")

# print(link)

link1=soup.find_all("a",string=["Elsie","Tillie"])
print(link1)













