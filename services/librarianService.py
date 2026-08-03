from typing import cast

from amulet.api.entity import Entity
from amulet_nbt import CompoundTag, ListTag

from lib.minecraft.enchantment import (
    get_enchantment_data_by_namespace_name,
    get_max_price,
    get_min_price,
)
from lib.minecraft.parser import parse_enchanted_book_recipes
from models.itemModel import EnchantedBook, Item
from models.recipeModel import DisplayRecipe, Recipe


class LibrarianService:
    def get_librarians(self, villagers: list[Entity]):
        """
        從村民列表篩選出圖書管理員
        """
        return [
            villager
            for villager in villagers
            if villager.nbt.compound.get_compound("Villager")
            .get_string("profession")
            .py_str
            == "minecraft:librarian"
        ]

    def format_display(self, librarian: Entity):
        """
        格式化輸出圖書管理員資料
        """
        string: str = "\t".join(
            [
                (
                    librarian.nbt.compound.get_string("CustomName").py_str
                    if "CustomName" in librarian.nbt.compound
                    else librarian.base_name
                ),
                "lv: "
                + str(
                    librarian.nbt.compound.get_compound("Villager")
                    .get_int("level")
                    .py_int
                ),
                "UUID: "
                + " ".join(
                    map(str, librarian.nbt.compound.get_int_array("UUID").py_data)
                ),
            ]
        )

        return string

    def get_enchanted_book_recipes(self, librarian: Entity):
        """
        從圖書管理員資料解析出附魔書交易項目
        """
        recipes = parse_enchanted_book_recipes(
            [
                recipe
                for recipe in cast(ListTag[CompoundTag], librarian.nbt.compound.get_compound("Offers").get_list("Recipes").py_list)  # type: ignore[reportUnknownArgumentType]
                if recipe.get_compound("sell").get_string("id").py_str
                == "minecraft:enchanted_book"
            ]
        )

        return recipes

    def build_display_recipe(self, recipe: Recipe):
        """
        產生用於UI介面的交易項目資料物件
        """
        display_recipe = DisplayRecipe()

        recipe.buy = cast(Item, recipe.sell)
        recipe.sell = cast(EnchantedBook, recipe.sell)

        enchantment = recipe.sell.enchantments[0]

        data = get_enchantment_data_by_namespace_name(enchantment.namespace_name)

        display_recipe.name = data["name"]
        display_recipe.level = enchantment.level
        display_recipe.price = recipe.buy.count

        display_recipe.min_level = 1
        display_recipe.max_level = data["max_level"]

        display_recipe.min_price = get_min_price(
            display_recipe.level, data["is_treasure"]
        )
        display_recipe.max_price = get_max_price(
            display_recipe.level, data["is_treasure"]
        )

        display_recipe.is_treasure = data["is_treasure"]

        return display_recipe
