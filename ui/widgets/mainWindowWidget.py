from typing import cast

from amulet.api.entity import Entity
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QWidget

from services.appServices import AppServices
from ui.generated.mainWindowGenerated import Ui_MainWindow
from ui.widgets.modifyLibrarianWidget import ModifyLibrarianWidget
from ui.widgets.searchVillagerWidget import SearchVillagerWidget
from ui.widgets.worldImportWidget import WorldImportWidget


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # type: ignore[reportUnknownMemberType]

        self.services = AppServices() # 初始化服務

        self.worldImportWidget = WorldImportWidget(self.services) # 初始化 Widgets
        self.searchVillagerWidget = SearchVillagerWidget(self.services)
        self.modifyLibrarianWidget = ModifyLibrarianWidget(self.services)

        self.combine_widgets()

        self.reset()

        self.searchVillagerWidget.setEnabled(False)
        self.modifyLibrarianWidget.setEnabled(False)

        self.bind_event() # 開始監聽事件

    def combine_widgets(self) -> None:
        """
        組合 Widgets
        """
        self.ui.WorldImportLayout.addWidget(self.worldImportWidget)
        self.ui.SearchVillagerLayout.addWidget(self.searchVillagerWidget)
        self.searchVillagerWidget.ui.modifyVillagerLayout.addWidget(
            self.modifyLibrarianWidget
        )

    def reset(self) -> None:
        """
        重置所有元件
        """
        self.worldImportWidget.reset()
        self.searchVillagerWidget.reset()
        self.modifyLibrarianWidget.reset()

    def bind_event(self) -> None:
        """
        綁定事件
        """
        self.worldImportWidget.world_loaded.connect(self.on_world_loaded)
        self.searchVillagerWidget.ui.librarianSelectorComboBox.currentIndexChanged.connect(
            self.librarian_selector_combo_box_index_on_change
        )

    def closeEvent(self, event: QCloseEvent) -> None:
        """
        當關閉程式觸發 儲存並關閉世界
        """
        self.services.world_service.close_world()

        event.accept()

    def on_world_loaded(self) -> None:
        """
        當載入按鈕按下 並成功載入世界觸發 將 searchVillagerWidger 啟用 
        """
        self.searchVillagerWidget.setEnabled(True)

    def librarian_selector_combo_box_index_on_change(self) -> None:
        """
        當選擇 Combo Box 資料 或是 初始化清單 時觸發
        """
        if (
            current_librarian := self.searchVillagerWidget.ui.librarianSelectorComboBox.currentData()
        ):
            current_librarian = cast(Entity, current_librarian)
            self.modifyLibrarianWidget.setEnabled(True)
            enchanted_book_recipes = (
                self.services.librarian_service.get_enchanted_book_recipes(
                    current_librarian
                )
            )
            display_recipes = [
                self.services.librarian_service.build_display_recipe(recipe)
                for recipe in enchanted_book_recipes
            ]
            self.modifyLibrarianWidget.display_recipes(display_recipes) # 設定UI介面上顯示的交易
        else:
            self.modifyLibrarianWidget.reset() # 當沒有資料 則重置UI介面顯示的交易
            self.modifyLibrarianWidget.setEnabled(False)
