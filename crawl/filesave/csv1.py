import csv

with open("./crawl/data/sample1.csv","r") as f:
    

    reader =csv.reader(f)

    print(reader)
    print(type(reader))
    print(dir(reader))
    print()
    next(reader)
    for c in reader:
        print(c)