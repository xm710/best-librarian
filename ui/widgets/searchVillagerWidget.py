from ui.widgets.baseWidget import BaseWidget
from ui.generated.searchVillagerGenerated import Ui_SearchVillager

class SearchVillagerWidget(BaseWidget):
    ui: Ui_SearchVillager

    def __init__(self):
        super().__init__(Ui_SearchVillager())

    def reset(self):
        ui = self.ui

        ui.posXSpinBox.setValue(0)
        ui.posYSpinBox.setValue(0)
        ui.posZSpinBox.setValue(0)
        ui.searchButton.setChecked(False)
        ui.villagerSelectorComboBox.clear()