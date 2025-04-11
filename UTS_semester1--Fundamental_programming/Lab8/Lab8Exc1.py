from abc import ABC, abstractmethod

# Step 1: Develop the Polygon class
# Polygon has one field: type
# Polygon has one constructor that initializes the field "type" from parameter
# Polygon has an abstract method 'area()' with no parameters and returns a double

class Polygon(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f"{self.type}"

# Step 2: Develop the class Square
# Square is subclass of Polygon
# Square has one field: side of type double
# Square has one constructor that initializes the field side from parameter
# Square overrides the method 'area' defined in Polygon to return the area of square
# Square overrides the toString() method to return: "<type> area = <area>"

class Square(Polygon):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side * self.side
    
    def __str__(self):
        return f"{self.type} area = {self.area()}"
    
