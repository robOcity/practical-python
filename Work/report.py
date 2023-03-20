# report.py
#
# Exercise 2.5

import csv
from pprint import pprint


def read_portfolio(filename):
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


portfolio = read_portfolio("Data/portfolio.csv")
total_cost = 0
for stock in portfolio:
    total_cost += stock.get("shares", 0) * stock.get("price", 0.0)

pprint(portfolio)
print(f"Total cost: ${total_cost:,.2f}")
