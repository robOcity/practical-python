# follow.py

import os
import time


def follow(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line


if __name__ == "__main__":
    for line in follow("Data/stocklog.csv"):
        fields = line.split(",")
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f"{name:>10s} {price:>10.2f} {change:>10.2f}")
