class Car:
    def __init__(self):
        self.engine = Engine()
        self.transmission = Transmission()
        self.brakes = Brakes()
        self.steering = Steering()

    def start(self):
        self.engine.start()
        self.transmission.shift('drive')

    def stop(self):
        self.brakes.apply()
        self.engine.stop()

    def turn_left(self):
        self.steering.turn_left()

    def turn_right(self):
        self.steering.turn_right()


class Engine:
    def start(self):
        print('Engine started')

    def stop(self):
        print('Engine stopped')


class Transmission:
    def shift(self, gear):
        print(f'Transmission shifted to {gear}')


class Brakes:
    def apply(self):
        print('Brakes applied')


class Steering:
    def turn_left(self):
        print('Turned left')

    def turn_right(self):
        print('Turned right')


# Client code
car = Car()
car.start()
car.turn_left()
car.turn_right()
car.stop()
