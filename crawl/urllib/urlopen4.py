import urllib.request as request
from urllib.error import HTTPError

# ㄷ다운로드 경로 및 파일명
path_list =["c:/cat.jpg",'c:/naver.html']

#다운로드 받을 이미지 및 파일 지정
target_url = ['https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAyMTZfNjIg%2FMDAxNjEzNDM5MDczMzc2.9KhhTa8Y_A1vsdtSWoMMILilcCqEwiYY9rNz5nZYxN0g._a2rrtn5e6AZqd_Qg90lcchKHHtmIF7BFYergElIlegg.JPEG.seahee21%2F20210215_121335.jpg&type=sc960_832','http://www.naver.com']


#
for i ,url in enumerate(target_url):
    try:
        response =request.urlopen(url)
        contents =response.read()
        print("*"*50)
        print()
        print("Header info {} -{}".format(i,response.info()))
        print("Http Status Code {}".format(response.getcode()))
        print()
        print("*"*50)

        #파일 지정
        with open(path_list[i],'wb') as f:
            f.write(contents)
    except HTTPError as e:
        print(e)
    else :
        print("succeed")