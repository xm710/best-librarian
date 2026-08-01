from ui.widgets.baseWidget import BaseWidget
from ui.generated.worldImportGenerated import Ui_WorldImport

class WorldImportWidget(BaseWidget):
    ui: Ui_WorldImport

    def __init__(self):
        super().__init__(Ui_WorldImport())

    def reset(self):
        ui = self.ui

        ui.levelFilePath.clear()
        ui.browseButton.setChecked(False)
        ui.loadButton.setChecked(False)