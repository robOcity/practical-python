# pcost.py
#
# Exercise 1.27 - Read portfolio data file and total up cost of purchasing all shares

import csv
import sys
import report


def portfolio_cost(filename):
    "returns the total cost to purchase the portfolio contained in file"
    total_cost = 0.0

    portfolio = report.get_portfolio(filename)
    stock_cost = [stock.get("shares") * stock.get("price") for stock in portfolio]
    return sum(stock_cost)


def main(argv):
    """
    Calculate the total cost of the portfolio using the CSV file provided.
    """
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = "Data/portfolio.csv"

    cost = portfolio_cost(filename)
    print(f"Total cost: ${cost:,.2f}")


if __name__ == "__main__":
    import sys

    main(sys.argv)
