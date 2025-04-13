from car import Car
from garage import Garage

c1 = Car("Toyota", "Corolla", 2022, 15000)
c2 = Car("Honda", "Civic", 2020, 8000)
c3 = Car("Tesla", "Model 3", 2023, 5000)

g = Garage()
g.add_car(c1)
g.add_car(c2)
g.add_car(c3)

g.show_all()
print("\nNew cars in the garage:")
g.new_cars()

print("\nTotal mileage:", g.total_mileage())
print("\nToyota cars:")
for car in g.filter_by_brand("Toyota"):
    car.info()
