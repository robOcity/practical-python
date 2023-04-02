#!/usr/bin/env python
# pcost.py
#
# Reads a portfolio data file and totals up the cost of purchasing all shares

import sys
import report
from stock import Stock


def portfolio_cost(filename):
    "returns the total cost to purchase the portfolio contained in file"
    total_cost = 0.0

    portfolio = report.read_portfolio(filename)
    return sum([stock.cost for stock in portfolio])


def main(argv):
    """
    Calculate the total cost of the portfolio using the CSV file provided.
    """
    if len(argv) != 2:
        raise SystemExit(f"Usage: {argv[0]} portfolio_csv")

    cost = portfolio_cost(argv[1])
    print(f"Total cost: ${cost:,.2f}")


if __name__ == "__main__":
    import sys

    main(sys.argv)
