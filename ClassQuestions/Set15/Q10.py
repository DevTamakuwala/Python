def separate_types(mixed_list):
    ints = []
    strings = []
    tuples = []

    for item in mixed_list:
        if isinstance(item, int):
            ints.append(item)
        elif isinstance(item, str):
            strings.append(item)
        elif isinstance(item, tuple):
            tuples.append(item)
    return ints, strings, tuples

data = [1, "hello", (1, 2), 42, "world", (3, 4)]
ints, strs, tups = separate_types(data)
print("Integers:", ints)
print("Strings:", strs)
print("Tuples:", tups)
