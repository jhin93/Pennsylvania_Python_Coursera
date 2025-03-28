class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getNameAge(self):
        return self.name, self.age
    
    def setNameAge(self, name, age):
        self.name = name
        self.age = age
    

person = Person("John", 20)
print(person.getNameAge())
person.setNameAge("Jane", 21)
print(person.getNameAge())
    
    