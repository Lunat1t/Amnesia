"""Small CSV import helpers used by two independent maintenance tasks."""
import csv
import io


def _rows(text):
    return csv.DictReader(io.StringIO(text))


def import_prices(text):
    return [float(row['price']) for row in _rows(text) if row['price']]


def import_quantities(text):
    return [int(row['quantity']) for row in _rows(text) if row['quantity']]
