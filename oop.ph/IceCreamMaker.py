class IceCreamMaker:
    def churn(self):
     print("Churning Cream")
    def freeze(self):
        print("Freezing Cream")

    def makeIceCream(self):

        self.churn()
        self.freeze()

iceCreamMaker = IceCreamMaker()
iceCreamMaker.makeIceCream()
