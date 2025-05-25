def calculate_total_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

gradebook = {
    "Alice": [85, 90, 88],
    "Bob": [75, 80, 70],
    "Charlie": [95, 92, 90]
}

for student, marks in gradebook.items():
    total, avg = calculate_total_average(marks)
    print(f"{student} -> Total: {total}, Average: {avg:.2f}")
