class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def compare(self, student):
        if self.marks > student.marks:
            return self
        else:
            return student

student1 = Student("Jenil", 80 )
student2 = Student("Dev", 75)

higher_marks_student = student1.compare(student2)

print(f"Student with higher marks name is {higher_marks_student.name} with {higher_marks_student.marks} marks")