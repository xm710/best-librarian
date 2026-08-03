#type
from itemModel import Item, EnchantedBook

class Recipe():
    def __init__(self):
        self.buy : Item | None = None
        self.sell: Item | EnchantedBook | None = None

    def __repr__(self):
        return f"buy: {self.buy}\tsell: {self.sell}"

class DisplayRecipe:
    def __init__(self):
        self.name       : str  | None = None
        self.level      : int  | None = None
        self.price      : int  | None = None
        self.is_treasure: bool | None = None

        self.min_level: int | None = None
        self.max_level: int | None = None
        self.min_price: int | None = None
        self.max_price: int | None = None