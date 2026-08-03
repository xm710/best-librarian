from PySide6.QtWidgets import QWidget

from services.appServices import AppServices
from ui.generated.searchVillagerGenerated import Ui_SearchVillager


class SearchVillagerWidget(QWidget):

    def __init__(self, services: AppServices):
        super().__init__()
        self.ui = Ui_SearchVillager()
        self.ui.setupUi(self)  # type: ignore[reportUnknownMemberType]

        self.librarians = None

        self.services = services

        self.bind_event()

    def reset(self):
        ui = self.ui

        self.librarians = None

        ui.posXSpinBox.setValue(0)
        ui.posYSpinBox.setValue(0)
        ui.posZSpinBox.setValue(0)
        ui.searchButton.setChecked(False)
        ui.librarianSelectorComboBox.clear()

    def bind_event(self):
        self.ui.searchButton.clicked.connect(self.search_button_on_click)

    def search_button_on_click(self):
        x = self.ui.posXSpinBox.value()
        y = self.ui.posYSpinBox.value()
        z = self.ui.posZSpinBox.value()

        villagers = self.services.villager_service.get_villagers_by_block(
            self.services.world_service.context.get_world(), x, y, z
        )
        self.librarians = self.services.librarian_service.get_librarians(villagers)
        self.ui.librarianSelectorComboBox.clear()
        for librarian in self.librarians:
            self.ui.librarianSelectorComboBox.addItem(
                self.services.librarian_service.format_display(librarian), librarian
            )
        self.ui.librarianSelectorComboBox.setCurrentIndex(-1)
