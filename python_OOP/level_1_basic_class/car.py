class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def info(self):
        print(f"{self.year} {self.brand} {self.model}, {self.mileage} km")
    
    def is_new(self):
        return self.year>=2021
    
    def needs_service(self):
        return self.mileage>10000