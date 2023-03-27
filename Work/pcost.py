# pcost.py
#
# Exercise 1.27 - Read portfolioi data file and total up cost of purchasing all shares

import csv
import sys


def portfolio_cost_csv(filename):
    "returns the total cost to purchase the portfolio contained in file"
    total_cost = 0
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        next(rows)  # step over header
        for row_no, row in enumerate(rows):
            try:
                sym, shares, price = row[0], int(row[1]), float(row[2])
                total_cost += int(shares) * float(price)
            except ValueError:
                print(f"Row #{row_no} contains missing/invalid data: {row}")
    return total_cost


def portfolio_cost(filename):
    "returns the total cost to purchase the portfolio contained in file"
    total_cost = 0
    with open(filename, "rt") as f:
        headers = f.readline().split(",")
        for line in f.readlines():
            sym, shares, price = line.split(",")
            try:
                total_cost += int(shares) * float(price)
            except ValueError:
                print(f"Cannot parse '{shares}' or '{price}'")
            except TypeError:
                print(f"Cannot multiple '{shares}' and '{float(price)}'")

    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f"Total cost: ${cost:,.2f}")

cost = portfolio_cost_csv(filename)
print(f"Total cost using CSV: ${cost:,.2f}")
