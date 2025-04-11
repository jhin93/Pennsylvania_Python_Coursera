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
    
# Step 3: Develop the class Triangle
# Triangle is a subclass of Polygon
# Triangle has two double fields: height and base
# Triangle has one constructor that initializes these fields from parameters
# Triangle overrides the method 'area' defined in Polygon to return the area of a triangle
# Triangle overrides the toString() method to return: "<type> area = <area>"

class Triangle(Polygon):
    def __init__(self, height, base):
        super().__init__("Triangle")
        self.height = height
        self.base = base

    def area(self):
        return 0.5 * self.height * self.base
    
    def __str__(self):
        return f"{self.type} area = {self.area()}"
    
