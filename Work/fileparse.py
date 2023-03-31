# fileparse.py
#
# Parses CSV data files returning portfolio and stock price data.

import csv
from typing import Any, Tuple, List, Dict, Callable, Union, TextIO


def parse_csv(
    file_handle: TextIO,
    select: List[str] = None,
    types: List[Callable] = None,
    delimiter: str = ",",
    has_headers: bool = True,
) -> Union[List[Dict[str, str]], List[Tuple[Any, ...]]]:
    """
    Parses a CSV file into a list of records as a list of dicts or tuples.
    """
    records = []
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(file_handle, delimiter=delimiter)
    if has_headers:
        header = next(rows)
        if not select:
            select = header
        if not types:
            types = [str for col in header]
        try:
            records = [
                {
                    name: type(value)
                    for type, name, value in zip(types, header, row)
                    if name in select
                }
                for row in rows
                if row
            ]
        except ValueError as ve:
            print("Couldn't convert data. Reason: ", ve)
            raise
    else:
        records = dict(
            [tuple([type(val) for type, val in zip(types, row)]) for row in rows if row]
        )

    return records
