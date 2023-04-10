from portfolio import Portfolio


def test_portfolio_cost():
    with open("Work/Data/portfolio.csv") as file_handle:
        portfolio = Portfolio.from_csv(file_handle)
        assert portfolio.total_cost == float(44671.15)


def test_tabulate_shares():
    with open("Work/Data/portfolio.csv") as file_handle:
        portfolio = Portfolio.from_csv(file_handle)
        tabulated_shares = portfolio.tabulate_shares()
        assert tabulated_shares["MSFT"] == 250
        assert tabulated_shares["CAT"] == 150
