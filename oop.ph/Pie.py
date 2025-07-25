class Pie:
    def __init__(self, flavor, ingredients):
        self.flavor = flavor
        self.ingredients = ingredients

    def print_ingredients(self):
        for ingredient in self.ingredients:
            print(ingredient)

applePie = Pie('Apple', ["flour", 'eggs', 'apple', 'butter'])

applePie.print_ingredients()
