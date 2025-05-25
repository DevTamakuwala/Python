students = [["jenil", 88], ["Blagandharv", 72], ["Suraj", 90], ["David", 72]]
scores = sorted(set(score for _, score in students))
second_lowest = scores[1]
result = sorted(name for name, score in students if score == second_lowest)
print("Second lowest:", second_lowest)
print("Students:", result)
