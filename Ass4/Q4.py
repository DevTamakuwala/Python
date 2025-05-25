from collections import Counter

# Part 1: Dictionary with numbers and their squares
squares_dict = {x: x**2 for x in range(1, 16)}
print("Dictionary of squares (1 to 15):")
print(squares_dict)

print("\n-----------------------------\n")

# Part 2: Combine two dictionaries and add values for common keys
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = Counter(d1) + Counter(d2)

print("Combined dictionary with summed values:")
print(combined_dict)
