#!/usr/bin/env python
# report.py
#
# Exercise 2.5

import gzip
import fileparse
from stock import Stock


def read_portfolio(filename, delimeter=","):
    """
    Reads file provide and returns a list of dicts of stock holdings {name, shares, price}.

    Use the delimeter parameter to provide an alternate (not comma) character.
    """
    stock_dicts = []
    with open(filename, "rt") as file_handle:
        stock_dicts = fileparse.parse_csv(
            file_handle,
            select=["name", "shares", "price"],
            types=[str, int, float],
            delimiter=delimeter,
        )
    return [Stock(sd["name"], sd["shares"], sd["price"]) for sd in stock_dicts]


def read_prices(filename, delimeter=","):
    """
    Reads price data from a file and returns a dictionary {stock, price}.

    Use the delimeter parameter to provide an alternate (not comma) character.
    """

    with open(filename, "rt") as file_handle:
        return fileparse.parse_csv(file_handle, types=[str, float], has_headers=False)


def make_report(portfolio, prices):
    """
    Determine the change in stock prices returning a list of tuples (name, shares, price, change)
    """
    report = []
    for stock in portfolio:
        if not prices.get(stock.name):
            continue
        change = prices.get(stock.name) - stock.price
        report.append((stock.name, stock.shares, stock.price, change))
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


def portfolio_report(portfolio_data_file, prices_data_file, delimeter=","):
    """
    Generates a report for a portfolio of stocks and current prices.

    Use the delimeter parameter to provide an alternate (not comma) character.
    """
    portfolio = read_portfolio(portfolio_data_file, delimeter)
    prices = read_prices(prices_data_file, delimeter)
    report = make_report(portfolio, prices)
    print_report(report)


def main(argv):
    """
    Provide portfolio and price data files to generate an investment report.
    """

    if len(argv) != 3:
        raise SystemExit(f"Usage: {argv[0]} portfolio_csv prices_csv")
    portfolio_report(argv[1], argv[2])


if __name__ == "__main__":
    import sys

    main(sys.argv)
