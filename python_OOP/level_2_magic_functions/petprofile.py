# 1_petprofile.py

class Petprofile:
    def __init__(self, name, age, tyype):
        self.name = name
        self.age = age
        self.tyype = tyype
    
    def __str__(self):
        return(f"Pet {self.name} is a {self.age}-year old {self.tyype}")
    
    def __repr__(self):
        return(f"Pet ('{self.name}', {self.age}, '{self.tyype}')")