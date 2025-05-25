"""
name = public
_name = protected
__name = private


class Parent:
    def greet(self):
        print ("Hello from Parent")

class Child (Parent):
    def greet(self):
        print ("Hello from Child")
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

def sum1(a = 10, b = 20, *c):
    res = a + b
    for i in c:
        res += i
    return res

def sum2(a = 10, b = 20, **c):
    res = a + b
    for i in c.values():
        res += i
    return res
p1 = Person("John", 36)
p1.display()

print(sum1(11, 22, 10, 22, 34, 21))
print(sum2(a=11,b= 22,c= 10,d= 22, e=34, f=21))


class Student:
    def __init__(self):
        self.name = "Alice"     # public
        self._age = 20          # protected (convention)
        self.__marks = 90       # private (name mangled)

    def get_marks(self):
        return self.__marks

s = Student()
print(s.name)           # Accessible
# print(s._age)           # Accessible (not recommended)
# print(s.__marks)      # Error
print(s.get_marks())    # Correct way to access private data


class MyClass:
    """This is a sample class"""
    pass

print(MyClass.__doc__)      # "This is a sample class"
print(MyClass.__name__)     # "MyClass"
print(MyClass.__module__)   # "__main__"
