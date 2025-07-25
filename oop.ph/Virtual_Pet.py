class VirtualPet:
   
color = "Brown"
legs = 4


def bark(self):
    print("Bark")


def display_color(self):
    print(self.color)


def display_legs(self):
    print(self.legs)


rocky = VirtualPet()
rocky.display_color()
rocky.display_legs()