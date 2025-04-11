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

