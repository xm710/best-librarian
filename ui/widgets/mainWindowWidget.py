from ui.widgets.baseWidget import BaseWidget
from ui.widgets.worldImportWidget import WorldImportWidget
from ui.widgets.searchVillagerWidget import SearchVillagerWidget
from ui.widgets.modifyLibrarianWidget import ModifyLibrarianWidget

from ui.generated.mainWindowGenerated import Ui_MainWindow

from services.worldService import WorldService
from services.villagerService import VillagerService
from services.librarianService import LibrarianService

class MainWindow(BaseWidget):
    ui: Ui_MainWindow

    def __init__(self):
        super().__init__(Ui_MainWindow())

        self.world_service = WorldService()
        self.villager_service = VillagerService(self.world_service)
        self.librarian_service = LibrarianService()
        
        self.worldImportWidget = WorldImportWidget(self.world_service)
        self.searchVillagerWidget = SearchVillagerWidget(self.villager_service, self.librarian_service)
        self.modifyLibrarianWidget = ModifyLibrarianWidget(self.librarian_service)

        self.combine_widgets()
        self.reset()
        
        self.searchVillagerWidget.setEnabled(False)
        self.modifyLibrarianWidget.setEnabled(False)

        self.bind_event()

    def combine_widgets(self):
        self.ui.WorldImportLayout.addWidget(self.worldImportWidget)
        self.ui.SearchVillagerLayout.addWidget(self.searchVillagerWidget)
        self.searchVillagerWidget.ui.modifyVillagerLayout.addWidget(self.modifyLibrarianWidget)

    def reset(self):
        self.worldImportWidget.reset()
        self.searchVillagerWidget.reset()
        self.modifyLibrarianWidget.reset()

    def bind_event(self):
        self.worldImportWidget.world_loaded.connect(
            self.on_world_loaded
        )
        self.searchVillagerWidget.ui.librarianSelectorComboBox.currentIndexChanged.connect(
            self.librarian_selector_combo_box_index_on_change
        )

    def closeEvent(self, event):
        self.world_service.close_world()

        event.accept()

    def on_world_loaded(self):
        self.searchVillagerWidget.setEnabled(True)

    def librarian_selector_combo_box_index_on_change(self):
        if (current_librarian := self.searchVillagerWidget.ui.librarianSelectorComboBox.currentData()):
            self.modifyLibrarianWidget.setEnabled(True)
            recipes = self.librarian_service.get_enchanted_book_recipes(current_librarian)
            display_recipes = [
                self.librarian_service.build_display_recipe(recipe) for recipe in recipes
            ]
            self.modifyLibrarianWidget.display_recipes(display_recipes)
            
        else:
            self.modifyLibrarianWidget.reset()
            self.modifyLibrarianWidget.setEnabled(False)