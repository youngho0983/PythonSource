import requests
from bs4 import BeautifulSoup

s=requests.Session()
response=s.get("https://news.v.daum.net/v/20210226123347076")
temp=response.text
soup=BeautifulSoup(temp,"html.parser")

news_title =soup.select_one(".tit_view")
print(news_title)
print(news_title.string)

print()

num_date =soup.select_one("span.num_date")
print(num_date)
print(num_date)


print()


paragraph =soup.select_one("p[dmcf-pid='c0eD2HXtps']")
print(paragraph)

print()

writer =soup.select_one("span.txt_info")
print(writer)

print(writer.string)




