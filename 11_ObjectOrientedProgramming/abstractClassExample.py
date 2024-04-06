from abc import ABC, abstractmethod

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
        return 