import abc

class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self, input):
        """Method documentation"""
        return

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim
    
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = self.a + self.b
        print("Consider me implemented", perim)
        return perim
    
class Square(Rectangle):
    def __init__(self, a):
        self.a = a

    def calc_perimeter(self):
        perim = self.a + self.a
        print("Consider me implemented", perim)
        return perim


# Instances
triangle = Triangle(3, 4, 5)
rectangle = Rectangle(2, 4)
square = Square(3)

# Printed perimeters 
print("Perimeter of Triangle:", triangle.calc_perimeter())
print("Perimeter of Rectangle:", rectangle.calc_perimeter())
print("Perimeter of Square:", square.calc_perimeter())
