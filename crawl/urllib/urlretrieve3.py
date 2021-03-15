import urllib.request as request

url="http://google.html"
img_url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAxMTRfMTgw%2FMDAxNjEwNjAwNzg0OTc4.762VbtVaQQJcD-uWkVscpsqnNnqzJPZ1SnXEa22BMGgg.tT6vivTQ7TgSDAXdnK4PBhu9G0dog4YcxCcdrv4pF5Yg.JPEG.yb5692%2F1610600484418.jpg&type=sc960_832"

save_file="c:/gooble.html"
save_img="c:/catcat.jpg"

try:
    file1,header1=request.urlretrieve(img_url,save_img)
except Exception as e:
    print(e)
else:
    print(file1)
    print("----"*80)
    print(header1)
    print("성공")