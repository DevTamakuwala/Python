# 1. Dictionary with squares of numbers between 1 and 15
square_dict = {i: i**2 for i in range(1, 16)}
print("Square Dictionary:", square_dict)

# 2. Combine two dictionaries by adding values for common keys
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine dictionaries and add values for common keys
from collections import Counter
combined = Counter(d1) + Counter(d2)
print("Combined Dictionary:", combined)
