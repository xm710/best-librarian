from PySide6.QtWidgets import QApplication, QWidget

from ui.generated.mainWindowGenerated import Ui_MainWindow
from ui.generated.worldImportGenerated import Ui_WorldImport
from ui.generated.searchVillagerGenerated import Ui_SearchVillager
from ui.generated.modifyLibrarianGenerated import Ui_ModifyLibrarian

from typing import Any

def preview():

    def createWidget(UI: Any):
        widget = QWidget()
        ui = UI()
        ui.setupUi(widget)

        return widget, ui

    app = QApplication.instance() or QApplication([])

    mainWindowWidget, mainWindowUI = createWidget(Ui_MainWindow)
    worldImportWidget, _ = createWidget(Ui_WorldImport)
    searchVillagerWidget, searchVillagerUI = createWidget(Ui_SearchVillager)
    modifyLibrarianWidget, _ = createWidget(Ui_ModifyLibrarian)

    mainWindowUI.WorldImportLayout.addWidget(worldImportWidget)
    mainWindowUI.SearchVillagerLayout.addWidget(searchVillagerWidget)
    searchVillagerUI.modifyVillagerLayout.addWidget(modifyLibrarianWidget)

    mainWindowWidget.show()

    app.exec()


if __name__ == "__main__":
    preview()
