import csv
list1=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
with open("./crawl/data/sample3.csv","w",newline="") as f:
    # 2차원 리스트를 csv로 저장
    wt=csv.writer(f)
    
    wt.writerows(list1)