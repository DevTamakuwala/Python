class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def calculate(self):
        return self.length * self.width


    def compare(self, rectangle):
        if self.calculate() > rectangle.calculate():
            print(f"Object rectangle area is larger. Area is {self.calculate()}")
        else:
            print(f"Passed rectangle area is larger. Area is {rectangle.calculate()}")


rectangle1 = Rectangle(5, 55)
rectangle2 = Rectangle(13, 30)

rectangle1.compare(rectangle2)
rectangle2.compare(rectangle1)