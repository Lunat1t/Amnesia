"""Independent verifier installed only after the agent finishes its task."""
import sys
from importers import import_prices, import_quantities

name = sys.argv[1]
fn = {'prices': import_prices, 'quantities': import_quantities}[name]
column = {'prices': 'price', 'quantities': 'quantity'}[name]
assert fn(f'{column},note\n0,z\n2,t\n') == [0, 2], 'zero and order'
assert fn(f'{column},note\n,empty\n"   ",space\n2,t\n') == [2], 'blank fields'
assert fn(f'{column},note\n" 2 ","comma, inside"\n') == [2], 'CSV quoting'
try:
    fn(f'{column}\nnot-a-number\n')
except ValueError:
    pass
else:
    raise AssertionError('invalid nonempty value must raise')
print(f'{name}: all checks passed')
