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
        headers = next(rows)
        for row in rows:
            sym, shares, price = row[0], int(row[1]), float(row[2])
            total_cost += calc_total_cost(shares, price)
    return total_cost


def portfolio_cost(filename):
    "returns the total cost to purchase the portfolio contained in file"
    total_cost = 0
    with open(filename, "rt") as f:
        headers = f.readline().split(",")
        print(headers)
        for line in f.readlines():
            sym, shares, price = line.split(",")
            total_cost += calc_total_cost(shares, price)
    return total_cost


def calc_total_cost(shares, price):
    "calculates the total cost of purchasing shares"
    try:
        return int(shares) * float(price)
    except ValueError:
        print(f"Cannot parse either {shares} and/or {price}")


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f"Total cost ${cost:,.2f}")

cost = portfolio_cost_csv("Data/portfolio.csv")
print(f"Total cost by csv ${cost:,.2f}")
