from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QStringListModel

from ui.generated.modifyLibrarianGenerated import Ui_ModifyLibrarian

from lib.minecraft.enchantment import get_max_price, get_min_price

# type
from typing import cast

from PySide6.QtWidgets import QLineEdit, QSpinBox, QPushButton, QLayoutItem

from models.recipeModel import DisplayRecipe
from services.appServices import AppServices

class ModifyLibrarianWidget(QWidget):
    def __init__(self, services: AppServices):
        super().__init__()
        self.ui = Ui_ModifyLibrarian()
        self.ui.setupUi() # type: ignore[reportUnknownMemberType]

        self.enchantsListViewModel = QStringListModel([])
        self.ui.enchantsListView.setModel(self.enchantsListViewModel)

        self.services = services

        self.recipeLV1 = RecipeDataManager(
            self.ui.enchantmentNameLV1, self.ui.enchantmentLevelLV1, self.ui.enchantedBookPriceLV1
        )
        self.recipeLV2 = RecipeDataManager(
            self.ui.enchantmentNameLV2, self.ui.enchantmentLevelLV2, self.ui.enchantedBookPriceLV2
        )
        self.recipeLV3 = RecipeDataManager(
            self.ui.enchantmentNameLV3, self.ui.enchantmentLevelLV3, self.ui.enchantedBookPriceLV3
        )
        self.recipeLV4 = RecipeDataManager(
            self.ui.enchantmentNameLV4, self.ui.enchantmentLevelLV4, self.ui.enchantedBookPriceLV4
        )

        self.bind_event()

    def reset(self):
        ui = self.ui

        for i in range(ui.gridLayout.count()):
            layout_item = cast(QLayoutItem, ui.gridLayout.itemAt(i))
            cast(QPushButton, layout_item.widget()).setChecked(False)

        self.enchantsListViewModel.setStringList([])

        self.recipeLV1.reset()
        self.recipeLV2.reset()
        self.recipeLV3.reset()
        self.recipeLV4.reset()

        ui.saveButton.setChecked(False)

    def bind_event(self):
        self.ui.enchantmentLevelLV1.valueChanged.connect(
            self.recipeLV1.enchantment_level_on_change
        )
        self.ui.enchantmentLevelLV2.valueChanged.connect(
            self.recipeLV2.enchantment_level_on_change
        )
        self.ui.enchantmentLevelLV3.valueChanged.connect(
            self.recipeLV3.enchantment_level_on_change
        )
        self.ui.enchantmentLevelLV4.valueChanged.connect(
            self.recipeLV4.enchantment_level_on_change
        )

    def display_recipe(self, display_recipe: DisplayRecipe, librarian_level: int):
        recipt_data_manager = getattr(self, f"recipeLV{librarian_level}")
        recipt_data_manager.set(display_recipe)

    def display_recipes(self, display_recipes: list[DisplayRecipe]):
        self.reset()
        for librarian_level, display_recipe in enumerate(display_recipes, 1):
            self.display_recipe(display_recipe, librarian_level)
        

class RecipeDataManager():
    def __init__(self, enchantment_name: QLineEdit, enchantment_level: QSpinBox, enchanted_book_price: QSpinBox):
        self.enchantment_name = enchantment_name
        self.enchantment_level = enchantment_level
        self.enchanted_book_price = enchanted_book_price
        self.is_treasure = None

    def reset(self):
        self.is_treasure = None

        self.enchantment_name.clear()

        self.enchantment_level.setMinimum(0)
        self.enchantment_level.setValue(0)
        self.enchantment_level.setMaximum(0)

        self.enchanted_book_price.setMinimum(0)
        self.enchanted_book_price.setValue(0)
        self.enchanted_book_price.setMaximum(0)

    def set(self, display_recipe: DisplayRecipe):
        self.is_treasure = display_recipe.is_treasure

        self.enchantment_level.setMinimum(cast(int, display_recipe.min_level))
        self.enchantment_level.setMaximum(cast(int, display_recipe.max_level))
        self.enchanted_book_price.setMinimum(cast(int, display_recipe.min_price))
        self.enchanted_book_price.setMaximum(cast(int, display_recipe.max_price))

        self.enchantment_name.setText(cast(str, display_recipe.name))
        self.enchantment_level.setValue(cast(int, display_recipe.level))
        self.enchanted_book_price.setValue(cast(int, display_recipe.price))

    def enchantment_level_on_change(self):
        self.is_treasure = cast(bool, self.is_treasure)

        self.enchanted_book_price.setMinimum(
            get_min_price(self.enchantment_level.value(), self.is_treasure)
        )
        self.enchanted_book_price.setMaximum(
            get_max_price(self.enchantment_level.value(), self.is_treasure)
        )