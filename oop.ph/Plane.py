class Plane:
    def fly(self):
        print("Woosh")

class Jet(Plane):
    def invert(self):
        print("Inverted")


jet = Jet()
jet.fly()
jet.invert()
