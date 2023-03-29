# fileparse.py
#
# Exercise 3.3

import csv
from typing import List, Dict, Callable


def parse_csv(
    filename: str,
    select: List[str] = ["price", "name", "shares"],
    types: List[Callable] = [str, int, float],
) -> List[Dict[str, str]]:
    """
    Parses a CSV file into a list of records each represented as a dictionary.
    """
    records = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        records = [
            {
                name: type(value)
                for type, name, value in zip(types, header, row)
                if name in select
            }
            for row in rows
            if row
        ]
    return records
