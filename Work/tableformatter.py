# tableformatter.py
#
# Classes for formatting data as tables


class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplemented()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplemented()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format.
    """

    def headings(self, headers):
        print(" ".join([f"{header.capitalize():>10s}" for header in headers]))
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{str(d):>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Emit portfolio data as a in CSV format.
    """

    def headings(self, headers):
        print(headers)
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Emit portfolio data as an HTML table
    """

    def headings(self, headers):
        print(self.format_table_row(headers))

    def row(self, rowdata):
        print(self.format_table_row(rowdata))

    def format_table_row(self, data):
        return "<tr>" + "".join(["<td>" + d + "</td>" for d in data]) + "</tr>"


class FormatError(Exception):
    pass


def create_formatter(fmt):
    """
    Factory method for TableFormatters.
    """
    TableFormatter = None
    if fmt == "txt":
        return TextTableFormatter()
    elif fmt == "csv":
        return CSVTableFormatter()
    elif fmt == "html":
        return HTMLTableFormatter()
    else:
        raise FormatError(
            f"Cannot format as directed. No '{fmt}' formatter is available."
        )


def print_table(rows, columns, formatter):
    """
    Prints a table of Stocks as determined by the configured TableFormatter.
    """
    formatter.headings(columns)
    for row in rows:
        formatter.row([str(getattr(row, col)) for col in columns])
