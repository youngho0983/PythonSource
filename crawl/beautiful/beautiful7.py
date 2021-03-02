import requests
from bs4 import BeautifulSoup

s=requests.Session()
response=s.get("https://news.v.daum.net/v/20210226123347076")
temp=response.text
soup=BeautifulSoup(temp,"html.parser")

title=soup.find("h3")
print(title.text)

writer=soup.find("span",class_='txt_info')
print(writer.text)

time_=soup.find("span",class_='num_date')
print(time_.string)

first=soup.find("p",{"dmcf-ptype":"general"})
print(first.string)






