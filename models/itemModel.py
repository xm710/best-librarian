#type
from typing import List

from enchantmentModel import Enchantment

class Item():
    def __init__(self):
        self.namespace_name: str | None = None
        self.count         : int | None = None

    def __repr__(self):
        return f"namespace_name:{self.namespace_name} x{self.count}"

class EnchantedBook(Item):
    def __init__(self):
        super().__init__()

        self.namespace_name = "minecraft:enchanted_book"

        self.enchantments: List[Enchantment] = []

    def __repr__(self):
        enchantments_str = f"{[enchantment for enchantment in self.enchantments]}"

        return super().__repr__() + f" {enchantments_str}"