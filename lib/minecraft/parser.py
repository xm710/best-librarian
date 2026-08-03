from collections.abc import ItemsView
from typing import cast

from amulet_nbt import CompoundTag, IntTag

from lib.nbt.getter import fast_get_compound
from models.enchantmentModel import Enchantment
from models.itemModel import EnchantedBook, Item
from models.recipeModel import Recipe


def parse_enchanted_book_recipe(recipeNBT: CompoundTag):
    """
    解析附魔書交易
    """
    parsed_recipe = Recipe()
    parsed_recipe.buy = Item()
    parsed_recipe.sell = EnchantedBook()

    parsed_recipe.buy.namespace_name = "emerald"
    parsed_recipe.buy.count = recipeNBT.get_compound("buy").get_int("count").py_int

    parsed_recipe.sell.count = 1

    namespace_name_level_pairs = cast(
        ItemsView[str, IntTag],
        fast_get_compound(
            recipeNBT, ["sell", "components", "minecraft:stored_enchantments"]
        ).items(),
    )
    parsed_recipe.sell.enchantments = [
        Enchantment(namespace_name, level.py_int)
        for namespace_name, level in namespace_name_level_pairs
    ]

    return parsed_recipe


def parse_enchanted_book_recipes(recipeNBT_list: list[CompoundTag]):
    """
    解析多個附魔書交易
    """
    parsed_recipes = [parse_enchanted_book_recipe(recipe) for recipe in recipeNBT_list]

    return parsed_recipes
