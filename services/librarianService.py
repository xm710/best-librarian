from lib.minecraft.parser import parse_enchantment_recipes
from lib.minecraft.enchantment import get_enchantment_data_by_namespace_name, get_max_price, get_min_price

from models.recipeModel import DisplayRecipe

class LibrarianService:
    def get_librarians(self, villagers):
        return self._filter_librarians(villagers)
    
    def _filter_librarians(self, villagers):
        return [
            villager
            for villager in villagers
            if villager.nbt["VillagerData"]["profession"].value == "minecraft:librarian"
        ]
    
    def format_display(self, librarian):
        string = "\t".join([
            librarian.nbt["CustomName"].value if "CustomName" in librarian.nbt else librarian.base_name,
            "lv: "+ str(librarian.nbt["VillagerData"]["level"].value),
            "UUID: "+ " ".join(map(str, librarian.nbt["UUID"].value))
        ])

        return string

    def get_enchanted_book_recipes(self, librarian):
        recipes = parse_enchantment_recipes(
            [
                recipe
                for recipe in librarian.nbt["Offers"]["Recipes"]
                if recipe["sell"]["id"].value == "minecraft:enchanted_book"
            ]
        )

        return recipes

    def build_display_recipe(self, recipe):
        display_recipe = DisplayRecipe()

        enchantment = recipe.sell.enchantments[0]

        data = get_enchantment_data_by_namespace_name(enchantment.namespace_name)

        display_recipe.name = data["name"]
        display_recipe.level = enchantment.level
        display_recipe.price = recipe.buy.count

        display_recipe.min_level = 1
        display_recipe.max_level = data["max_level"]

        display_recipe.min_price = get_min_price(display_recipe.level, data["is_treasure"])
        display_recipe.max_price = get_max_price(display_recipe.level, data["is_treasure"])

        display_recipe.is_treasure = data["is_treasure"]

        return display_recipe