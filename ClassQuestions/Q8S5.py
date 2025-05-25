# 8. Create a dictionary where the keys are student names and the values are lists of their subject grades.
# Take dynamic input for multiple students and their grades.
# Retrieve and print the grades of a given student

students = {}

num_students = int(input("Enter the number of students: "))

for _ in range(num_students):
    name = input("Enter Student Name: ")
    grades = list(map(int, input("Enter grades separated by space: ").split()))

    students[name] = grades

search_name = input("Enter student name to search: ")
if search_name in students:
    print(f"Grades for {search_name}: {students[search_name]}")
else:
    print("Student not found.")

