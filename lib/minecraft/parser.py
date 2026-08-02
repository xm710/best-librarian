from models.recipeModel import Recipe
from models.itemModel import Item, EnchantedBook
from models.enchantmentModel import Enchantment

def parse_enchantment_recipe(recipe):
    parsed_recipe = Recipe()
    parsed_recipe.buy = Item()
    parsed_recipe.sell = EnchantedBook()

    parsed_recipe.buy.namespace_name = "emerald"
    parsed_recipe.buy.count = recipe["buy"]["count"].value

    parsed_recipe.sell.count = 1
    parsed_recipe.sell.enchantments = [
        Enchantment(namespace_name, level.value)
        for namespace_name, level in recipe["sell"]["components"]["minecraft:stored_enchantments"].items()
    ]

    return parsed_recipe
    
def parse_enchantment_recipes(recipes):
    parsed_recipes = [
        parse_enchantment_recipe(recipe)
        for recipe in recipes
    ]

    return parsed_recipes