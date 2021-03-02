import urllib.request as request

url="http://google.com"

#이미지 가져오기
img_url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAxMDdfMjMz%2FMDAxNjA5OTg4OTgxMjI1.WT8N1z9s9qGejegen-1rykYcpi6ime052aSsPDbmCA0g.zb_aX3GrOBVEu-Ee1G8x22rNkP23a2BPmvguJc5CN7og.JPEG.gmk72000%2FDSC08697.JPG&type=sc960_832"

save_url="c:/google.html"
save_img="c:/cat.png"
try:
    file1,header1=request.urlretrieve(url,save_url)
    file2,header2=request.urlretrieve(img_url,save_img)
except Exception as e:
    print(e)
else:
    print(header1)
    print("성공")
    print(file1)
    print("-------------"*20)
    print(header2)
    print(file2)