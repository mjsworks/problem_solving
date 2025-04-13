from car import Car

class Garage:
    def __init__(self):
        self.cars = []
    
    def add_car(self, car):
        self.cars.append(car)
    
    def show_all(self):
        for car in self.cars:
            print(f"Brand - {car.brand}, Model - {car.model}")

    def new_cars(self):
        for car in self.cars:
            if car.is_new():
                print(f"Brand - {car.brand}, Model - {car.model}")
    
    def total_mileage(self):
        return sum(car.mileage for car in self.cars)
    
    def filter_by_brand(self, brand):
        return [car for car in self.cars if car.brand == brand]