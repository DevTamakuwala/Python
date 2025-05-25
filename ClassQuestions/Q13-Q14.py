# 13 Demonstrate the following functions/methods which operates on dictionary in Python with suitable examples: clear (), get ( ), pop( ), copy( ), pop( ) ,keys( ) , values() ,items() 
class StudentRecord:
    def _init_(self):
        self.records = {}

    def add_student(self, admission_no, roll_no, name, marks):
        self.records[admission_no] = {
            "Roll Number": roll_no,
            "Name": name,
            "Marks": marks
        }

    def display_student(self, admission_no):
        student = self.records.get(admission_no)
        if student:
            print("\nStudent Details:")
            print(f"Admission Number: {admission_no}")
            for key, value in student.items():
                print(f"{key}: {value}")
        else:
            print("\nStudent not found!")

# Demonstration of dictionary methods
student_db = StudentRecord()
student_db.add_student(101, 1, "Alice", 85)
student_db.add_student(102, 2, "Bob", 90)
student_db.add_student(103, 3, "Charlie", 78)

print("\nOriginal Dictionary:")
print(student_db.records)

# get()
print("\nUsing get():", student_db.records.get(101))

# pop()
popped_student = student_db.records.pop(102, "Not Found")
print("\nUsing pop():", popped_student)

# copy()
copied_records = student_db.records.copy()
print("\nUsing copy():", copied_records)

# keys()
print("\nUsing keys():", student_db.records.keys())

# values()
print("\nUsing values():", student_db.records.values())

# items()
print("\nUsing items():", student_db.records.items())

# clear()
student_db.records.clear()
print("\nUsing clear():", student_db.records)


# 14 Create a Python program to create a dictionary which has a record of a student information: Admission number, Roll Number, Name and Marks. Display information on the basis of Admission number. 
class StudentRecord:
    def _init_(self):
        self.records = {}

    def add_student(self, admission_no, roll_no, name, marks):
        self.records[admission_no] = {
            "Roll Number": roll_no,
            "Name": name,
            "Marks": marks
        }

    def display_student(self, admission_no):
        student = self.records.get(admission_no)
        if student:
            print("\nStudent Details:")
            print(f"Admission Number: {admission_no}")
            for key, value in student.items():
                print(f"{key}: {value}")
        else:
            print("\nStudent not found!")

student_db = StudentRecord()

student_db.add_student(101, 1, "Alice", 85)
student_db.add_student(102, 2, "Bob", 90)
student_db.add_student(103, 3, "Charlie", 78)

admission_no = int(input("Enter Admission Number to search: "))
student_db.display_student(admission_no)