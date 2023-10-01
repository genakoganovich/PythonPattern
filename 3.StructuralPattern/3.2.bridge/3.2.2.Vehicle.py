class Vehicle:
    def __init__(self, engine, name):
        self.engine = engine
        self.name = name

    def start(self):
        return f'{self.name}'


class VehicleBridge(Vehicle):
    def start(self):
        print(f"Starting {self.name} with Starting {self.engine.start()}")


class Engine:
    def start(self):
        return 'Engine'


class PetrolEngine(Engine):
    def start(self):
        return 'Petrol Engine'


class DieselEngine(Engine):
    def start(self):
        return 'Diesel Engine'


class ElectricEngine(Engine):
    def start(self):
        return 'Electric Engine'
