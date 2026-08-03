from amulet_nbt import CompoundTag

from lib.nbt.getter import fast_get_compound
from lib.nbt.converter import int_items
from models.enchantmentModel import Enchantment
from models.itemModel import EnchantedBook, Item
from models.recipeModel import Recipe


def parse_enchanted_book_recipe(recipeNBT: CompoundTag) -> Recipe:
    """
    解析附魔書交易
    """
    buy = Item(
        "emerald",
        recipeNBT.get_compound("buy").get_int("count").py_int  # 取得綠寶石所需數量
    )
    
    namespace_name_level_compound = fast_get_compound(
        recipeNBT, ["sell", "components", "minecraft:stored_enchantments"]
    ) # 取得附魔書的附魔效果

    sell = EnchantedBook([
        Enchantment(namespace_name, level.py_int)
        for namespace_name, level in int_items(namespace_name_level_compound)
    ])

    parsed_recipe = Recipe(buy, sell)

    return parsed_recipe


def parse_enchanted_book_recipes(recipeNBT_list: list[CompoundTag]) -> list[Recipe]:
    """
    解析多個附魔書交易
    """
    parsed_recipes = [parse_enchanted_book_recipe(recipe) for recipe in recipeNBT_list]

    return parsed_recipes
