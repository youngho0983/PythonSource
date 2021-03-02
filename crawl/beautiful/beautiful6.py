from bs4 import BeautifulSoup


with open("./crawl/beautiful/story.html","r") as f:
    response =f.read()


soup = BeautifulSoup(response, "html.parser")



#select_one() : css 선택자










