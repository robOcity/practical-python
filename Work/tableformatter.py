# tableformatter.py
#
# Classes for formatting data as tables


class TableFormatter:
    def headings(self, *headers):
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

    def headings(self, *headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{str(d):>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Emit portfolio as a in CSV format.
    """

    def headings(self, *headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))
