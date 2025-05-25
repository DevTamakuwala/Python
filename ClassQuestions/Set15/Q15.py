import statistics, math
def analyze(lst):
    return {
        'mean': statistics.mean(lst),
        'median': statistics.median(lst),
        'mode': statistics.mode(lst),
        'stdev': statistics.stdev(lst),
        'factorial_max': math.factorial(max(lst))
    }
print(analyze([1, 2, 2, 3, 4]))
