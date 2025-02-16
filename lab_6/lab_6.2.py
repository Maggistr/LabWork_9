class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Vehicle Make: {self.make}, Model: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make=make, model=model)
        self.fuel_type = fuel_type

    def get_info(self):
        super().get_info()
        return f"Car Make: {self.make}, Model: {self.model}, Fuel Type: {self.fuel_type}"


vehicle = Vehicle("Generic", "Model X")
print(vehicle.get_info())


car = Car("Toyota", "Corolla", "Petrol")
print(car.get_info())

