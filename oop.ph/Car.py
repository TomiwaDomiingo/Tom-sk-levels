class Car:
    manufacturer = "Ferrari"
    model = 2029
    color = 'brown'

    def print_specs(self):
        print(self.manufacturer)
        print(self.model)
        print(self.color)


    def change_color(self, new_color):
        self.color = new_color
        print("Color is now", self.color)

car = Car()
print(car.color)
car.change_color("red")

"""
how to change the color
"""

"""
how to print usuing inheritance
"""
car = Car()
print(car.color)

