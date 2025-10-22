import math

class Shape:
    def area(self):
        return "Maydon formulasi aniqlanmagan!"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, eni, buyi):
        self.eni = eni
        self.buyi = buyi
    
    def area(self):
        return self.eni * self.buyi


class Triangle(Shape):
    def __init__(self, asos, balandlik):
        self.asos = asos
        self.balandlik = balandlik
    
    def area(self):
        return 0.5 * self.asos * self.balandlik


shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 7)
]

for shape in shapes:
    print(shape.area())
