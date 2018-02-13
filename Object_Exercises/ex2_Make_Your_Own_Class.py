class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(car.year, car.make, car.model)

car = Vehicle("Nissan", "Leaf", 2015)

car.print_info()
