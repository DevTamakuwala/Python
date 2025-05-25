# 7. Write a program to store employee details in a dictionary where:
# The keys are employee IDs.
# The values are dictionaries with .
# Allow users to retrieve employee details based on the ID.

employees = {}

num_employees = int(input("Enter the number of employees: "))

for _ in range(num_employees):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")

    employees[emp_id] = {
        "Name": name,
        "Age": age,
        "Department": department
    }

search_id = input("Enter Employee ID to search: ")
if search_id in employees:
    print("Employee Details:", employees[search_id])
else:
    print("Employee not found.")

