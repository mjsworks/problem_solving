## Object
in python, everything is object - integer, string, function or even classes.

an object is an instance of a class and it contains:
    1. Data - atreibute, field, state
    2. Behaviour - methods

it is like a real world thing. like a car. it has attribute(color, top speed) and behaviour(drive, brake).

## Class
a class is nothing but a blueprint for creating an object.

```
class Car:
    def __init__(self, color):
        self.color = color
    
    def drive(self):
        print(f"the {self.color} car is driving.")
```

here, __init__ is the constructor. it initialized the object.
self refers to the current object.
attribute like color is saved in each one of the object and will differ in objects.


### matering "self" keyowrd
self allows each object to keep its own state. omitting self means that the variable is treated locally and not tied to the object.