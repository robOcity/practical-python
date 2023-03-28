# report.py
#
# Exercise 2.5

import csv
from pprint import pprint


def get_portfolio(filename):
    """
    Reads file provide and returns a list of dicts of stock holdings {name, shares, price}.
    """
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
    """
    Reads price data from a file and returns a dictionary {stock, price}.
    """
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


def make_report(portfolio, prices):
    """
    Determine the change in stock prices returning a list of tuples (name, shares, price, change)
    """
    report = []
    for stock in portfolio:
        name, shares, price = stock.values()
        if not prices.get(name):
            continue
        change = prices.get(name) - price
        report.append((name, shares, price, change))
    return report


def print_report(report):
    """
    Prints a well-formatted report given a list of name, shares, change dicts.
    """
    headers = ("Name", "Shares", "Price", "Change")
    print(
        f"{headers[0]:>{10}s} {headers[1]:>{10}s} {headers[2]:>{10}s} {headers[3]:>{10}s}".format(
            headers
        )
    )
    print("{:->10}".format("") + 3 * " {:->10}".format(""))

    total_cost, aggregate_change = 0, 0
    fmt_price = ""
    for name, shares, price, change in report:
        fmt_price = "${:>,.2f}".format(price)
        print(f"{name:>10s} {shares:>10d} {fmt_price:>10s} {change:>10.2f}")
        total_cost += price * shares
        aggregate_change += change * shares

    print(f"\nCost: ${total_cost: ,.2f}   Change: ${aggregate_change: ,.2f}")


def portfolio_report(portfolio_csv_file, prices_csv_file):
    """
    Generates a report for a portfolio of stocks and current prices.
    """
    portfolio = get_portfolio(portfolio_csv_file)
    prices = get_prices(prices_csv_file)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report("Data/portfolio.csv", "Data/prices.csv")
