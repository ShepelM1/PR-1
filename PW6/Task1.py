class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print("Engine started")


class Car(Vehicle):

    def __init__(self, model, brand):
        self.model = model

    def start_engine(self):
        print("Car engine started")


class Motorcycle(Vehicle):

    def __init__(self, type, brand):
        self.type = type

    def start_engine(self):
        print("Motorcycle engine started")


class ElectricCar(Car):

    def charge_battery(self):
        print("Battery charging")


class Garage:

    def __init__(self, vehicle_list):
        self.vehicle_list = vehicle_list

    def start_all_engines(self):
        [x.start_engine() for x in self.vehicle_list]


car = Car("BMW", "X5")
motorcycle = Motorcycle("Sport Bikes", "Honda")
electric_car = ElectricCar("Tesla", "Model 3")

garage = Garage([car, motorcycle, electric_car])
Garage.start_all_engines(garage)
