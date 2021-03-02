from bs4 import BeautifulSoup


with open("./crawl/beautiful/story.html","r") as f:
    response =f.read()


soup = BeautifulSoup(response, "html.parser")

# find() : 제일 처음 만나는 요소
# title =soup.find("title")
# print("title : {}".format(title.string))
# print("title .parent: {}".format(title.find_parent()))


# h1=soup.find("h1")
# print("h1 {}".format(h1))
# print("h1 text {}".format(h1.string))

p1=soup.find("p")
p1=soup.find("p","title")
print(p1)

# print(p1)
# print(p1.string)

# #두번쨰 p
# p2=soup.find("p",class_="story")
# print(p2)
# print(p2.get_text())

# p3=p2.find_next_sibling()
# print(p3)

# b1=soup.find("b")

# print(b1)

a1 =soup.find("a",id="link1")
print(a1)
print(a1.string)


# 세번째 a 를 찾아봅시다.

a3=soup.find('a',{"class":"sister","data-io":"link3"})
print(a3)
print(a3["href"])