import csv
with open('musinsa.csv', 'r', encoding='utf-8') as f:
    res = csv.reader(f, delimiter='|', quotechar='"')
    for d in res:
        if d:
            print(d)