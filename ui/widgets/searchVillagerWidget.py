from ui.widgets.baseWidget import BaseWidget
from ui.generated.searchVillagerGenerated import Ui_SearchVillager

class SearchVillagerWidget(BaseWidget):
    ui: Ui_SearchVillager

    def __init__(self):
        super().__init__(Ui_SearchVillager())

    def reset(self):
        ui = self.ui

        ui.posX.setValue(0)
        ui.posY.setValue(0)
        ui.posZ.setValue(0)
        ui.searchButton.setChecked(False)
        ui.villagerSelector.clear()