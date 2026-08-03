from typing import cast

from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import QLayoutItem, QLineEdit, QPushButton, QSpinBox, QWidget

from lib.minecraft.enchantment import get_max_price, get_min_price
from models.recipeModel import DisplayRecipe
from services.appServices import AppServices
from ui.generated.modifyLibrarianGenerated import Ui_ModifyLibrarian


class ModifyLibrarianWidget(QWidget):
    def __init__(self, services: AppServices) -> None:
        super().__init__()
        self.ui = Ui_ModifyLibrarian()
        self.ui.setupUi(self)  # type: ignore[reportUnknownMemberType]

        self.enchantsListViewModel = QStringListModel([])
        self.ui.enchantsListView.setModel(self.enchantsListViewModel)

        self.services = services

        self.display_recipeLV1 = DisplayRecipeWidgetManager(
            self.ui.enchantmentNameLV1,
            self.ui.enchantmentLevelLV1,
            self.ui.enchantedBookPriceLV1,
        ) # 設定交易UI管理器
        self.display_recipeLV2 = DisplayRecipeWidgetManager(
            self.ui.enchantmentNameLV2,
            self.ui.enchantmentLevelLV2,
            self.ui.enchantedBookPriceLV2,
        )
        self.display_recipeLV3 = DisplayRecipeWidgetManager(
            self.ui.enchantmentNameLV3,
            self.ui.enchantmentLevelLV3,
            self.ui.enchantedBookPriceLV3,
        )
        self.display_recipeLV4 = DisplayRecipeWidgetManager(
            self.ui.enchantmentNameLV4,
            self.ui.enchantmentLevelLV4,
            self.ui.enchantedBookPriceLV4,
        )

        self.bind_event() # 開始監聽事件

    def reset(self) -> None:
        """
        重置元件
        """
        ui = self.ui

        for i in range(ui.gridLayout.count()): # 重置篩選按鈕
            layout_item = cast(QLayoutItem, ui.gridLayout.itemAt(i))
            cast(QPushButton, layout_item.widget()).setChecked(False)

        self.enchantsListViewModel.setStringList([]) # 重置附魔效果清單

        self.display_recipeLV1.reset() # 重置交易UI
        self.display_recipeLV2.reset()
        self.display_recipeLV3.reset()
        self.display_recipeLV4.reset()

        ui.saveButton.setChecked(False) # 重置儲存按鈕

    def bind_event(self) -> None:
        """
        監聽事件
        """
        self.ui.enchantmentLevelLV1.valueChanged.connect(
            self.display_recipeLV1.enchantment_level_on_change
        )
        self.ui.enchantmentLevelLV2.valueChanged.connect(
            self.display_recipeLV2.enchantment_level_on_change
        )
        self.ui.enchantmentLevelLV3.valueChanged.connect(
            self.display_recipeLV3.enchantment_level_on_change
        )
        self.ui.enchantmentLevelLV4.valueChanged.connect(
            self.display_recipeLV4.enchantment_level_on_change
        )

    def display_recipes(self, display_recipes: list[DisplayRecipe]) -> None:
        """
        在 UI 上顯示設定的交易資料
        """
        self.reset()
        for librarian_level, display_recipe in enumerate(display_recipes, 1):
            display_recipe_widget_manager: DisplayRecipeWidgetManager = getattr(self, f"display_recipeLV{librarian_level}")
            display_recipe_widget_manager.set(display_recipe)


class DisplayRecipeWidgetManager:
    def __init__(
        self,
        enchantment_name: QLineEdit,
        enchantment_level: QSpinBox,
        enchanted_book_price: QSpinBox,
    ) -> None:
        self.enchantment_name = enchantment_name
        self.enchantment_level = enchantment_level
        self.enchanted_book_price = enchanted_book_price
        self.is_treasure = None

    def reset(self):
        """
        重置元件
        """
        self.is_treasure = None

        self.enchantment_name.clear()

        self.enchantment_level.setMinimum(0)
        self.enchantment_level.setValue(0)
        self.enchantment_level.setMaximum(0)

        self.enchanted_book_price.setMinimum(0)
        self.enchanted_book_price.setValue(0)
        self.enchanted_book_price.setMaximum(0)

    def set(self, display_recipe: DisplayRecipe) -> None:
        """
        設定交易資料
        """
        self.is_treasure = display_recipe.is_treasure

        self.enchantment_level.setMinimum(display_recipe.min_level)
        self.enchantment_level.setMaximum(display_recipe.max_level)
        self.enchanted_book_price.setMinimum(display_recipe.min_price)
        self.enchanted_book_price.setMaximum(display_recipe.max_price)

        self.enchantment_name.setText(display_recipe.name)
        self.enchantment_level.setValue(display_recipe.level)
        self.enchanted_book_price.setValue(display_recipe.price)

    def enchantment_level_on_change(self) -> None:
        """
        當更改附魔等級時觸發 使價格上下限動態調整
        """
        self.is_treasure = cast(bool, self.is_treasure)

        self.enchanted_book_price.setMinimum(
            get_min_price(self.enchantment_level.value(), self.is_treasure)
        )
        self.enchanted_book_price.setMaximum(
            get_max_price(self.enchantment_level.value(), self.is_treasure)
        )