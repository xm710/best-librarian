from models.itemModel import Item
from lib.minecraft.enchantment import get_min_price, get_max_price


class Recipe:
    def __init__(self, buy: Item, sell: Item) -> None:
        self.buy = buy
        self.sell = sell


class DisplayRecipe:
    def __init__(self, name: str, level: int, price: int, max_level: int, is_treasure: bool) -> None:
        self.name = name
        self.level = level
        self.price = price
        self.is_treasure = is_treasure

        self.min_level: int = 1
        self.max_level: int = max_level

        self.min_price: int = 0
        self.max_price: int = 0
        self.set_price_range()

    def set_price_range(self) -> None:
        """
        設定綠寶石所需數量上下限
        """
        self.min_price = get_min_price(self.level, self.is_treasure)
        self.max_price = get_max_price(self.level, self.is_treasure)