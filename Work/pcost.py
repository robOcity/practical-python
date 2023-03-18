# pcost.py
#
# Exercise 1.27 - Read portfolioi data file and total up cost of purchasing all shares

total_cost = 0

with open("Data/portfolio.csv", "rt") as f:
    headers = f.readline().split(",")
    print(headers)
    for line in f.readlines():
        stock, shares, price = line.split(",")
        print(stock, shares, price.strip())
        total_cost += float(shares) * float(price.strip())

print(f"Total cost ${total_cost:,.2f}")
