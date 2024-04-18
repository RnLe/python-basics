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
    def __init__(self, x: float, y: float):
        super().__init__()
        if x <= 0 or y <= 0: raise ValueError("x and y have to be positive floats or integers.")
        self.x = x
        self.y = y

    def get_area(self) -> float:
        return self.x * self.y
    
    def get_perimeter(self) -> float:
        return 2 * (self.x + self.y)
    
    def get_center(self):
        # Assume the center at the top left corner
        return (self.x/2, self.y/2)
    
class Circle(Geometry2D):
    def __init__(self, r: float):
        super().__init__()
        if r <= 0: raise ValueError("Radius has to be a positive float or integer.")
        self.r = r
        
    def get_area(self) -> float:
        return math.pi * self.r**2
    
    def get_perimeter(self) -> float:
        return 2*math.pi*self.r
    
    def get_center(self):
        # Assume the center already in the middle (draw the circle around it)
        return (0,0)
    
class Triangle(Geometry2D):
    types = {"equilateral": 0, "isosceles": 1, "scalene": 2}
    
    def __init__(self, type: str, length: float, length2: float = None, angle: float = None):
        """Generates a triangle object.

        Args:
            type (str): The type of the triangle. Can be "equilateral", "isosceles" or "scalene".
            length (float): The length of the first side.
            length2 (float, optional): The length of the second side (not the height!). Defaults to None.
            angle (float, optional): The angle between the two sides. Defaults to None.

        Raises:
            ValueError: If the length is not a positive float or integer.
        """        
        super().__init__()
        self.type = Triangle.types[type]
        self.length = length
        self.length2 = length2
        self.angle = angle
        
        if not isinstance(length, int) or not isinstance(length, float) or length <= 0: raise ValueError("Length has to be a positive float or integer.")
        
        # Further error detection..
            
    def get_area(self):
        if self.type == Triangle.types["equilateral"]:
            return math.sqrt(3)/4 * self.length**2
        elif self.type == Triangle.types["isosceles"]:
            return 1/2 * self.length * self.length2 * math.sin(self.angle)
        elif self.type == Triangle.types["scalene"]:
            return 1/2 * self.length * self.length2 * math.sin(self.angle)
        
    def get_perimeter(self):
        if self.type == Triangle.types["equilateral"]:
            return 3 * self.length
        elif self.type == Triangle.types["isosceles"]:
            return 2 * self.length + self.length2
        elif self.type == Triangle.types["scalene"]:
            return self.length + self.length2 + math.sqrt(self.length**2 + self.length2**2 - 2*self.length*self.length2*math.cos(self.angle))
        
    def get_center(self):
        return (0,0)