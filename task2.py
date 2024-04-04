class Shape():
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Square(Shape):
    def __init__(self, width):
        self.width = width
    def area(self):
        return self.width ** 2

def print_area(shape):
    print(f"Площадь - {shape.area()}")

circle = Circle(5)
print_area(circle)

square = Square(7)
print_area(square)

rectangle = Rectangle(2, 3)
print_area(rectangle)
