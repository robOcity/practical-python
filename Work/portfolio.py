# portfolio.py
#
# Has a collection of stocks and provides useful behaviors


class Portfolio:
    def __init__(self, stocks):
        self.stocks = stocks

    def __iter__(self):
        return self.stocks.__iter__()

    @property
    def total_cost(self):
        return sum([stock.cost for stock in self.stocks])

    def tabulate_shares(self):
        from collections import Counter

        total_shares = Counter()
        for stock in self.stocks:
            total_shares[stock.name] += stock.shares
        return total_shares
