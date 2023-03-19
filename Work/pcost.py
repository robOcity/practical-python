# pcost.py
#
# Exercise 1.27 - Read portfolioi data file and total up cost of purchasing all shares


def portfolio_cost(file):
    "returns the total cost to purchase the portfolio contained in file"
    total_cost = 0
    with open(file, "rt") as f:
        headers = f.readline().split(",")
        print(headers)
        for line in f.readlines():
            stock, shares, price = line.split(",")
            print(stock, shares, price.strip())
            total_cost += float(shares) * float(price.strip())
    return total_cost


cost = portfolio_cost("Data/portfolio.csv")
print(f"Total cost ${cost:,.2f}")
