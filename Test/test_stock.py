from stock import Stock

g = Stock("GOOG", 100, 123.45)


def test_init():
    assert g.name == "GOOG"
    assert g.shares == 100
    assert g.price == 123.45


def test_cost():
    assert g.cost == g.shares * g.price


def test_sell():
    assert g.sell(25) == 75
