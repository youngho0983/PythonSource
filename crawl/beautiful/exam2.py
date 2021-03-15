import requests
from bs4 import BeautifulSoup

response =requests.get("https://www.gmarket.co.kr/?&jaehuid=200011048&gclid=EAIaIQobChMIx%2DycvOmG7wIVhVVgCh3sWwN%2DEAAYASAAEgJy%5FfD%5FBwE")
text=(response.text)

soup=BeautifulSoup(text,"html.parser")

# cate= soup.select("#button__category-all")
# print(cate)

categorys=soup.find_all("span",class_="link__1depth-item")
categorys2=soup.find_all("span",class_="text__emphasis")
# for category in categorys:
#     print(category.string)
for category in categorys2:
    print(category.string)
