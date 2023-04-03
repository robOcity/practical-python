# portfolio.py
#
# Has a collection of stocks and provides useful behaviors


class Portfolio:
    def __init__(self, stocks):
        self.stocks = stocks

    def __iter__(self):
        return self.stocks.__iter__()

    def __len__(self):
        return len(self.stocks)

    def __getitem__(self, index):
        return self.stocks[index]

    def __contains__(self, name):
        return any(stock.name == name for stock in self.stocks)

    @property
    def total_cost(self):
        return sum(stock.cost for stock in self.stocks)

    def tabulate_shares(self):
        from collections import Counter

        total_shares = Counter()
        for stock in self.stocks:
            total_shares[stock.name] += stock.shares
        return total_shares
