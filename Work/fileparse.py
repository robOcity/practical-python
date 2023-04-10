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
    silence_errors: bool = False,
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
        for row_num, row in enumerate(rows):
            try:
                if row:
                    records.append(
                        {
                            name: type(value)
                            for type, name, value in zip(types, header, row)
                            if name in select
                        }
                    )
            except ValueError as ve:
                if not silence_errors:
                    print(f"row {row_num}: Couldn't convert {row}")
                    print(f"Row {row_num}: Reason: {ve}")
                continue
    else:
        records = dict(
            [tuple([type(val) for type, val in zip(types, row)]) for row in rows if row]
        )
    return records
