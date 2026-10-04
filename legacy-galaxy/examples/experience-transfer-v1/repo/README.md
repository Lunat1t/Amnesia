# CSV importer fixture

`importers.py` provides independent price and quantity imports. Both accept CSV
text with a header and return a list of numbers. Changes should preserve CSV
quoting, row order, and errors for invalid nonempty numeric fields.
