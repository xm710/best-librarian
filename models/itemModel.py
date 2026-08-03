from models.enchantmentModel import Enchantment


class Item:
    def __init__(self, namespace_name: str, count: int) -> None:
        self.namespace_name = namespace_name
        self.count = count


class EnchantedBook(Item):
    def __init__(self, enchantments: list[Enchantment]) -> None:
        super().__init__("minecraft:enchanted_book", 1)

        self.enchantments = enchantments
