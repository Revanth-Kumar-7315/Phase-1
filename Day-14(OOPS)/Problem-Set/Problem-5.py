# 5. Build a Shape class hierarchy with Circle, Square, and Triangle, each with a method to calculate area.

from abc import ABC, abstractmethod
import math

# Base abstract class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass


# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Square class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


# Triangle class
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height