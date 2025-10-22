

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.manufactured = year

    def show_info(self):
        return f"{self.brand} - {self.manufactured} yilda ishlab chiqarilgan."

class Car(Vehicle):
    def show_info(self):
        return f"{self.brand} avtomobili ({self.manufactured}) yilda ishlab chiqarilgan"

class Bike(Vehicle):
    def show_info(self):
        return f"{self.brand} mototsikli {self.manufactured}-yilda chiqqarilgan"

vehicles = [
    Car("Monza", 2021),
    Bike("Yamaha", 2018),
    Vehicle("BYD", 2023)
]

for v in vehicles:
    print(v.show_info())
