# pcost.py
#
# Exercise 1.27 - Read portfolioi data file and total up cost of purchasing all shares

import csv
import sys


def portfolio_cost(filename):
    "returns the total cost to purchase the portfolio contained in file"
    total_cost = 0
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        print(header)
        for row_no, row in enumerate(rows):
            record = dict(zip(header, row))
            try:
                shares = int(record["shares"])
                price = float(record["price"])
                total_cost += shares * price
            except ValueError:
                print(f"Row #{row_no} contains missing/invalid data: {row}")
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f"Total cost: ${cost:,.2f}")
