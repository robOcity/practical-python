#!/usr/bin/env python
# report.py
#
# Provides a nicely formatted report showing changes in stock valuations.

import fileparse
import tableformatter
from stock import Stock
from portfolio import Portfolio


def read_portfolio(filename, **opts):
    """
    Reads file provide and returns a list of dicts of stock holdings {name, shares, price}.

    Use the delimiter parameter to provide an alternate (not comma) character.
    """
    with open(filename, "rt") as file_handle:
        return Portfolio.from_csv(file_handle, **opts)


def read_prices(filename, delimiter=","):
    """
    Reads price data from a file and returns a dictionary {stock, price}.

    Use the delimiter parameter to provide an alternate (not comma) character.
    """

    with open(filename, "rt") as file_handle:
        return fileparse.parse_csv(
            file_handle, delimiter=delimiter, types=[str, float], has_headers=False
        )


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
        # TODO REMOVE DEBUG
        print(f"make_report()\n{report}")
    return report


def print_report(report, formatter):
    """
    Prints a well-formatted report given a list of name, shares, change data.
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])

    total_cost, aggregate_change = 0, 0
    for name, shares, price, change in report:
        rowdata = [name, f"{str(shares):s}", f"{price:>.2f}", f"{change:>.2f}"]
        formatter.row(rowdata)
        total_cost += price * shares
        aggregate_change += change * shares

    print(f"\nCost: ${total_cost: ,.2f}   Change: ${aggregate_change: ,.2f}")


def portfolio_report(portfolio_data_file, prices_data_file, delimiter=",", fmt="txt"):
    """
    Generates a report for a portfolio of stocks and current prices.

    Use the delimiter parameter to provide an alternate (not comma) character.
    """
    portfolio = read_portfolio(portfolio_data_file, delimiter=delimiter)
    prices = read_prices(prices_data_file, delimiter)
    report = make_report(portfolio, prices)
    print_report(report, tableformatter.create_formatter(fmt))


def _get_fmt(arg: str) -> str:
    """
    Returns a valid format string.
    """
    return arg.strip().lower()[4:]


def main(argv):
    """
    Provide portfolio and price data files to generate an investment report.
    """

    if len(argv) < 3:
        raise SystemExit(
            f"Usage: {argv[0]} portfolio_csv prices_csv fmt='txt' delimiter=','"
        )
    elif len(argv) == 3:
        portfolio_report(argv[1], argv[2])
    elif len(argv) == 4:
        fmt = _get_fmt(argv[3])
        portfolio_report(argv[1], argv[2], fmt=fmt)
    elif len(argv) == 5:
        fmt = _get_fmt(argv[3])
        delimiter = argv[4][10:]
        portfolio_report(argv[1], argv[2], fmt=fmt, delimiter=delimiter)
    else:
        raise RuntimeError(
            "Usage: python report.py portfolio_csv prices_csv [fmt=txt, csv, or html]"
        )


if __name__ == "__main__":
    import sys

    main(sys.argv)
