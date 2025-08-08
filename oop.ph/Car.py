class Car:
    wheels = 4
    doors = 4

    def start_engine(self):
        print("VROOM")
    def injectFuel(self):
        print("SPRAYING FUEL")

    def igniteFuel(self):
        print("Boom")

    def startEngine(self):
        self.on = True
        while self.on:
            self.injectFuel()
            self.igniteFuel()


my_car = Car()
my_car.start_engine()
print(my_car.wheels)