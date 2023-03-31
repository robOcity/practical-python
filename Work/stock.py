# A class representing a stock its data and functionality


class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, num_shares: int):
        if self.shares - num_shares < 0:
            raise RuntimeError(
                f"You only have {self.shares:d}' available and can't sell {num_shares:d}"
            )
        self.shares = self.shares - num_shares
        return self.shares
