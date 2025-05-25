employees = [
    {'name': 'Jenil', 'age': 28, 'salary': 50000},
    {'name': 'Dev', 'age': 35, 'salary': 75000},
    {'name': 'Sajjda', 'age': 32, 'salary': 60000}
]

def highest_salary(emp_list):
    return max(emp_list, key=lambda e: e['salary'])

def count_older_than_30(emp_list):
    return sum(1 for e in emp_list if e['age'] > 30)

print("Highest Salary:", highest_salary(employees))
print("Employees older than 30:", count_older_than_30(employees))
