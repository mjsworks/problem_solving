class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"HI! my name is {self.name} and my age is {self.age}")