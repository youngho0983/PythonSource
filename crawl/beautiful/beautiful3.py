from bs4 import BeautifulSoup


with open("./crawl/beautiful/story.html","r") as f:
    response =f.read()


soup = BeautifulSoup(response, "html.parser")

print(soup.head())
print("**"*10)
print(soup.title())
print("**"*10)
print(soup.body())

print(soup.title.string)
print("**"*10)
print(soup.title.parent)

print("**"*10)
print("**"*10)
print(soup.h1)

p1=soup.p
print("p class name>>{}".format(p1['class']))

p2=p1.find_next_sibling("p")
print("첫번쨰 p >> {}".format(p2))
print("p text >> {}".format(p2.string))
print("p gettext >>{}".format(p2.get_text()))
print("p class name >> {}".format(p2["class"]))

b=soup.b
print(b)
print(b.getText())

##--------

a1 =soup.find("a")
print(a1)

a2=a1.find_next_sibling("a")
print(a2)

a3=a2.find_next_sibling("a")
print(a3)
a4=a3.find("a")
print(a4)