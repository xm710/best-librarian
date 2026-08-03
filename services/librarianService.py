from typing import cast

from amulet.api.entity import Entity
from amulet_nbt import CompoundTag, ListTag

from lib.minecraft.enchantment import get_enchantment_data_by_namespace_name
from lib.minecraft.parser import parse_enchanted_book_recipes
from models.itemModel import EnchantedBook
from models.recipeModel import DisplayRecipe, Recipe


class LibrarianService:
    def get_librarians(self, villagers: list[Entity]) -> list[Entity]:
        """
        從村民列表篩選出圖書管理員
        """
        return [
            villager
            for villager in villagers
            if villager.nbt.compound.get_compound("VillagerData")
            .get_string("profession")
            .py_str
            == "minecraft:librarian"
        ]

    def format_display(self, librarian: Entity) -> str:
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
                    librarian.nbt.compound.get_compound("VillagerData")
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

    def get_enchanted_book_recipes(self, librarian: Entity) -> list[Recipe]:
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

    def build_display_recipe(self, recipe: Recipe) -> DisplayRecipe:
        """
        產生用於UI介面的交易項目資料物件
        """
        recipe.sell = cast(EnchantedBook, recipe.sell)

        enchantment = recipe.sell.enchantments[0]
        data = get_enchantment_data_by_namespace_name(enchantment.namespace_name)

        name = data["name"]
        level = enchantment.level
        price = recipe.buy.count

        display_recipe = DisplayRecipe(name, level, price, data["max_level"], data["is_treasure"])

        return display_recipe
