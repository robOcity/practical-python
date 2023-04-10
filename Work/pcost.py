#!/usr/bin/env python
# pcost.py
#
# Reads a portfolio data file and totals up the cost of purchasing all shares

import sys
import report
from portfolio import Portfolio


def portfolio_cost(filename):
    "returns the total cost to purchase the portfolio contained in file"
    with open(filename, "rt") as file_handle:
        portfolio = Portfolio.from_csv(file_handle)
        return portfolio.total_cost


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
