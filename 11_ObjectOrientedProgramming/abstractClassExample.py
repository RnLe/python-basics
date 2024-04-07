from abc import ABC, abstractmethod
import math

class Geometry2D(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_area(self):
        pass
    
    @abstractmethod
    def get_perimeter(self):
        pass
    
    @abstractmethod
    def get_center(self):
        pass
    

class Rectangle(Geometry2D):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y
    
    def get_perimeter(self):
        return 2 * (self.x + self.y)
    
    def get_center(self):
        # Assume the center at the top left corner
        return (self.x/2, self.y/2)
    
class Circle(Geometry2D):
    def __init__(self, r):
        super().__init__()
        self.r = r
        
    def get_area(self):
        return math.pi * self.r**2
    
    def get_perimeter(self):
        return 2*math.pi*self.r
    
    def get_center(self):
        # Assume the center already in the middle (draw the circle around it)
        return (0,0)