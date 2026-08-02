class Recipe():
    def __init__(self):
        self.buy = None
        self.sell = None

    def __repr__(self):
        return f"buy: {self.buy}\tsell: {self.sell}"

class DisplayRecipe:
    def __init__(self):
        self.name = None
        self.level = None
        self.price = None
        self.is_treasure = None

        self.min_level = None
        self.max_level = None
        self.min_price = None
        self.max_price = None