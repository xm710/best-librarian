from ui.widgets.baseWidget import BaseWidget
from ui.widgets.worldImportWidget import WorldImportWidget
from ui.widgets.searchVillagerWidget import SearchVillagerWidget
from ui.widgets.modifyLibrarianWidget import ModifyLibrarianWidget

from ui.generated.mainWindowGenerated import Ui_MainWindow

class MainWindow(BaseWidget):
    ui: Ui_MainWindow

    def __init__(self):
        super().__init__(Ui_MainWindow())
        
        self.worldImportWidget = WorldImportWidget()
        self.searchVillagerWidget = SearchVillagerWidget()
        self.modifyLibrarianWidget = ModifyLibrarianWidget()

        self.combineWidgets()
        self.reset()

    def combineWidgets(self):
        self.ui.WorldImportLayout.addWidget(self.worldImportWidget)
        self.ui.SearchVillagerLayout.addWidget(self.searchVillagerWidget)
        self.searchVillagerWidget.ui.modifyVillagerLayout.addWidget(self.modifyLibrarianWidget)

    def reset(self):
        self.worldImportWidget.reset()
        self.searchVillagerWidget.reset()
        self.modifyLibrarianWidget.reset()