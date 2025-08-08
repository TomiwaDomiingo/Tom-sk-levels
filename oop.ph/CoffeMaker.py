class CoffeMaker:
    def heatWater(self):
        print("Heating Water")

    def brew(self):
        print("Adding Water to the grounds")

    def filterCoffe(self):
        print("Filtering Coffe")

    def makeCoffe(self):
        print("Making Coffe")
        self.heatWater()
        self.brew()
        self.filterCoffe()

coffemaker = CoffeMaker()
coffemaker.makeCoffe()