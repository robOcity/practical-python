from pprint import pprint
from fileparse import parse_csv

# TODO - create unit tests / integration tests


def print_test_header(desciption):
    print(f"\n{desciption}\n" + "{:->80}".format(""))


print_test_header('parse_csv("Data/portfolio.csv")')
pprint(parse_csv("Data/portfolio.csv"))

print_test_header('parse_csv("Data/portfolio.csv")')
pprint(parse_csv("Data/portfolio.csv", types=[str, int, float]))

print_test_header('parse_csv("Data/portfolio.csv", select=["price", "shares"])')
pprint(parse_csv("Data/portfolio.csv", select=["price", "shares"]))

print_test_header('parse_csv("Data/portfolio.dat", delimiter=" ")')
pprint(parse_csv("Data/portfolio.dat", delimiter=" "))

print_test_header(
    'parse_csv("Data/portfolio.dat", delimiter=" ", types=[str, int, float]))'
)
pprint(parse_csv("Data/portfolio.dat", delimiter=" ", types=[str, int, float]))
