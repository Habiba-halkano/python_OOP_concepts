#class and object creation
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"The car make is: {self.make} , model is: {self.model} and year of manufacture is:{self.year}")
        return self.make, self.model, self.year

car1 = Car("Audi", "BMW", "2021")
print(car1.display_info())