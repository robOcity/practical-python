# pcost_gzip.py
#
# Exercise 1.27 - Read portfolio gzipped data file and total up cost of purchasing all shares

import gzip

total_cost = 0

with gzip.open("Data/portfolio.csv.gz", "rt") as f:
    headers = f.readline().split(",")
    print(headers)
    for line in f.readlines():
        stock, shares, price = line.split(",")
        print(stock, shares, price.strip())
        total_cost += float(shares) * float(price.strip())

print(f"Total cost ${total_cost:,.2f}")
