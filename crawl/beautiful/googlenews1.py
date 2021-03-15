import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def main():
    url="https://news.google.com/search?q=python&hl=ko&gl=KR&ceid=KR%3Ako"

    try:
        with requests.Session() as s:
            response=s.get(url)

            soup=BeautifulSoup(response.text,"html.parser")
            news_clipping=data_extract(soup)
            
            for news_section in news_clipping:
                for k,v in news_section.items():
                    print("{} :{} ".format(k,v))
                print()
    except HTTPError as e:
        print(e)


def data_extract(soup):
    # 뉴스 섹션 영역 가져오기

    section =soup.select("div.xrnccd > article")
    # print(section)

    # 링크 , 제목 , 내용 , 출처, 등록일시
    news=[]
    news_item={}
    base_url="https://news.google.com"
    for item in section :
        link_title = item.select_one("h3>a")
        # print(linkheader)
        # print(linkheader["href"])
        # print(linkheader.string)
        news_item["href"]=base_url +link_title["href"][1:]

        news_item["title"]=link_title.get_text()
        news_item["contents"]=item.select_one("div >span").get_text()
        
        report_time_date_writer =item.select_one("div.QmrVtf > div.SVJrMe")
        
        news_item["writer"] =report_time_date_writer.select_one("a").get_text()

        report_date_time =report_time_date_writer.select_one("time")

        if report_date_time:
            report_date_time=report_date_time["datetime"].split("T")
            news_item["report_date"]=report_date_time[0]
            news_item["report_time"]=report_date_time[1]

        else:
            news_item["report_date"]=""
            news_item["report_time"]=""

        news.append(news_item)
        news_item={}

    return news
if __name__ =="__main__":
    main()


# s=requests.Session()



# response=s.get("https://news.google.com/search?q=python&hl=ko&gl=KR&ceid=KR%3Ako")
# soup=BeautifulSoup(response.text,"html.parser")

# print(soup)