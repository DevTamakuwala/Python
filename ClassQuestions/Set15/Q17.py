class Employee:
    def __init__(self, emp_id, name, salary):
        if salary < 0:
            raise ValueError("Salary can't be negative")
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department
    def display(self):
        super().display()
        print("Department:", self.department)

mgr = Manager(101, 'Rajeev', 70000, 'IT')
mgr.display()
