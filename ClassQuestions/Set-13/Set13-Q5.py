import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)

# Testing the method with two points
point1 = Point(3, 4)
point2 = Point(7, 1)

distance = point1.distance_to(point2)
print(f"The distance between the two points is: {distance:.2f}")
