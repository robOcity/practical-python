# portfolio.py
#
# Has a collection of stocks and provides useful behaviors
from stock import Stock
from fileparse import parse_csv


class Portfolio:
    def __init__(self):
        self.stocks = []

    def __iter__(self):
        return self.stocks.__iter__()

    def __len__(self):
        return len(self.stocks)

    def __getitem__(self, index):
        return self.stocks[index]

    def __contains__(self, name):
        return any(stock.name == name for stock in self.stocks)

    def append(self, stock):
        if not isinstance(stock, Stock):
            raise TypeError("Expecting a Stock instance.")
        print(f"adding stock: {stock}")
        self.stocks.append(stock)

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()

        portdicts = parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float], **opts
        )

        for d in portdicts:
            print(d)
            stock = Stock(**d)

            self.append(stock)

        return self

    @property
    def total_cost(self):
        return sum(stock.cost for stock in self.stocks)

    def tabulate_shares(self):
        from collections import Counter

        total_shares = Counter()
        for stock in self.stocks:
            total_shares[stock.name] += stock.shares
        return total_shares

    if __name__ == "__main__":
        # smoke test
        from portfolio import Portfolio
        from stock import Stock

        with open("Data/portfolio.csv") as file:
            portfolio = Portfolio.from_csv(file)

            for stock in portfolio:
                print(f"Stocks: {stock}")
