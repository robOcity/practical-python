# report.py
#
# Exercise 2.5

import csv
from pprint import pprint


def get_portfolio(filename):
    """Reads file provide and returns a list of dicts of stock holdings {name, shares, price}."""
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio.append(
                {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            )
    return portfolio


def get_prices(filename):
    """Reads price data from a file and returns a dictionary {stock, price}."""
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


portfolio = get_portfolio("Data/portfolio.csv")
total_cost = 0
for stock in portfolio:
    total_cost += stock.get("shares", 0) * stock.get("price", 0.0)

pprint(portfolio)
print(f"Total cost: ${total_cost:,.2f}")

prices = get_prices("Data/prices.csv")
change = 0.0
for stock in portfolio:
    name, shares, price = stock.values()
    if not prices.get(name):
        print(f"Unable to find current price for {name} shares")
        continue
    cost = shares * price
    current_value = shares * prices.get(name, 0.0)
    change += current_value - cost

print(f"The value of the portfolio has changed by ${change:,.2f}")
