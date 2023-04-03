# ticker.py

import csv
import tableformatter
import report
from follow import follow


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def filter_symbols(rows, names):
    for row in rows:
        if row["name"] in names:
            yield row


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows


def ticker(portfolio_csv, stock_ticker_csv, fmt="txt"):
    portfolio = report.read_portfolio(portfolio_csv)
    lines = follow(stock_ticker_csv)
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    formatter = tableformatter.create_formatter(fmt)
    formatter.headings(["name", "price", "change"])
    for row in rows:
        formatter.row([row["name"], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])


def main(argv):
    """
    Provide portfolio and price data files to generate an investment report.
    """

    if len(argv) < 3:
        raise SystemExit(f"Usage: {argv[0]} portfolio_csv stock_ticker_csv fmt='txt'")
    elif len(argv) == 3:
        ticker(argv[1], argv[2])
    elif len(argv) == 4:
        fmt = argv[3].strip().lower()[4:]
        ticker(argv[1], argv[2], fmt=fmt)
    else:
        raise RuntimeError(
            "Usage: python report.py portfolio_csv prices_csv [fmt=txt, csv, or html]"
        )


if __name__ == "__main__":
    import sys

    main(sys.argv)
