from pprint import pprint
import fileparse
import pytest


def parse_csv_invoker(filename, **opts):
    joined_opts = ", ".join(f"{k}={v}" for k, v in opts.items())
    cmd = f"parse_csv({filename}, {joined_opts})"
    records = None
    with open("./Work/" + filename, "rt") as file:
        try:
            records = fileparse.parse_csv(file, **opts)
        except Exception as e:
            pytest.fail(f"Cmd: {cmd} failed!\nException: {e}")
    pprint(records)
    return records


# comma delimited smoke tests
def test_parse_csv_del():
    records = parse_csv_invoker("Data/portfolio.csv", delimiter=",")
    assert any([bool(record) for record in records])


def test_parse_csv_del_types():
    records = parse_csv_invoker(
        "Data/portfolio.csv", delimiter=",", types=[str, int, float]
    )
    assert any([bool(record) for record in records])


def test_parse_csv_del_select():
    records = parse_csv_invoker(
        "Data/portfolio.csv", delimiter=",", select=["price", "shares"]
    )
    assert any([bool(record) for record in records])


def test_parse_csv_del_types_select():
    records = parse_csv_invoker(
        "Data/portfolio.csv",
        delimiter=",",
        types=[str, int, float],
        select=["price", "shares"],
    )
    assert any([bool(record) for record in records])


# space delimited smoke tests
def test_parse_dat_del():
    records = parse_csv_invoker("Data/portfolio.dat", delimiter=" ")
    assert any([bool(record) for record in records])


def test_parse_dat_del_types():
    records = parse_csv_invoker(
        "Data/portfolio.dat", delimiter=" ", types=[str, int, float]
    )
    assert any([bool(record) for record in records])


def test_parse_dat_del_select():
    records = parse_csv_invoker(
        "Data/portfolio.dat", delimiter=" ", select=["price", "shares"]
    )
    assert any([bool(record) for record in records])


def test_parse_dat_del_types_select():
    records = parse_csv_invoker(
        "Data/portfolio.dat",
        delimiter=" ",
        types=[str, int, float],
        select=["price", "shares"],
    )
    assert any([bool(record) for record in records])
