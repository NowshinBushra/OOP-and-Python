from math import pi
class Shape:
    def __init__(self, name) -> None:
        self.name = name

class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, name, radius) -> None:
        self.radius = radius
        super().__init__(name)

    def area(self):
        return pi * self.radius*self.radius
    

rec_area = Rectangle('myRec', 5, 3)
circle_area = Circle('myCircle', 2)
print(rec_area.area())
print(circle_area.area())