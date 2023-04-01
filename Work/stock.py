# stock.py
#
# A class representing a stock its data and related functionality.


class Stock:
    def __init__(
        self,
        name: str,
        shares: int,
        price: float,
        fmt=dict([("name", "s"), ("shares", "_d"), ("price", ".2f")]),
    ):
        self.name = name.upper()
        self.shares = shares
        self.price = price
        self.fmt = fmt

    def __repr__(self):
        return (
            f"Stock({self.name:{self.fmt.get('name')}}, "
            + f"{self.shares:{self.fmt.get('shares')}}, "
            + f"{self.price:{self.fmt.get('price')}})"
        )

    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, num_shares: int):
        if self.shares - num_shares < 0:
            raise RuntimeError(
                f"You only have {self.shares:d}' available and can't sell {num_shares:d}"
            )
        self.shares = self.shares - num_shares
        return self.shares
